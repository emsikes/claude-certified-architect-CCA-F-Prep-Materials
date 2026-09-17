from __future__ import annotations

import json
import sys
from typing import Any

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("ShopAssistMCP")


CUSTOMERS: dict[str, dict[str, Any]] = {
    "alex@example.com": {
        "customer_id": "CUS-1001",
        "email": "alex@example.com",
        "name": "Alex Morgan",
        "account_status": "active"
    }
}

ORDERS: dict[str, dict[str, Any]] = {
    "ORD-12345678": {
        "order_id": "ORD-12345678",
        "customer_id": "CUS-1001",
        "status": "delivered",
        "delivered_days_ago": 12,
        "total": 89.99,
        "currency": "USD",
    },
    "ORD-87654321": {
        "order_id": "ORD-87654321",
        "customer_id": "CUS-1001",
        "status": "delivered",
        "delivered_days_ago": 45,
        "total": 149.99,
        "currency": "USD",
    },
}


@mcp.tool()
def get_customer_by_email(email: str) -> dict:
    """01_api_requests.ipynb
    Find a customer profile by email address.

    Use this when the user provides and email address but no verified customer ID.
    Returns customer identity, account status, and customer ID.
    Do not use this tool to look up a specific order.`
    """
    normalized_email = email.strip().lower()
    customer = CUSTOMERS.get(normalized_email)

    if not customer:
        return {
            "isError": False,
            "customer": None,
            "message": "No customer was found for this email address.",
        }

    return {
        "isError": False,
        "customer": customer,
    }


@mcp.tool()
def lookup_order_by_id(order_id: str, customer_id: str) -> dict:
    """
    Retrieve a specific order by order ID for a verified customer.

    Use this only when you have an order ID and a verified customer ID.
    Do not use this tool with an email address instead of customer_id.
    Returns order status, delivery age, total amount, and currency.
    """

    normalized_order_id = order_id.strip().upper()

    if not normalized_order_id.startswith("ORD-"):
        return {
            "isError": True,
            "errorCategory": "validation",
            "isRetryable": False,
            "customerMessage": "The order ID does not look valid.  Please check the order number and try again.  Orders start with 'ORD-'...",
            "developerMessage": "Order ID must start with 'ORD-'",
        }

    order = ORDERS.get(normalized_order_id)

    if not order:
        return {
            "isError": False,
            "order": None,
            "message": "No order was found with this order ID."
        }

    if order["customer_id"] != customer_id:
        return {
            "isError": True,
            "errorCategory": "permission",
            "isRetryable": False,
            "customerMessage": "I can't access this order with the current account information.",
            "developerMessage": "Order does not belong to the authenticated customer."
        }

    return {
        "isError": False,
        "order": order
    }


@mcp.tool()
def check_refund_eligibility(order: dict) -> dict:
    """
    Check whether an order is eligible for an automatic refund.

    This tool checks policy only.
    It does not process the refund.
    Use process_refund only after this tool confirms eligibility.
    """
    if order["status"] != "delivered":
        return {
            "isError": True,
            "errorCategory": "business",
            "isRetryable": False,
            "customerMessage": "This order is not eligible for an automatic refund because it has not been delivered.",
            "developerMessage": "Refund denied because order status is not delivered",
        }

    if order["delivered_days_ago"] > 30:
        return {
            "isError": True,
            "errorCategory": "business",
            "isRetryable": False,
            "customerMessage": "This order is outside the 30-day return window, so I cannot process this request automatically.",
            "developerMessage": "Refund denied delivery date is outside the 30-day policy window.",
        }

    return {
        "isError": False,
        "eligible": True,
        "reason": "Order is within the 30-day return window."
    }


@mcp.tool()
def process_refund(order_id: str, amount: float, reason: str) -> dict:
    """
    Submit an automatic refund for an eligible order.

    Use this tool only after check_refund_eligibility confirms the order is eligible.
    This tool performs the refund action.
    """
    if amount <= 0:
        return {
            "isError": True,
            "errorCategory": "validation",
            "isRetryable": False,
            "customerMessage": "This refund amount must be greater than zero.",
            "developerMessage": "Refund amount was less than or equal to zero.",
        }

    return {
        "isError": False,
        "refund": {
            "refund_id": "REF-555000",
            "order_id": order_id,
            "amount": amount,
            "status": "submitted",
            "reason": reason,
        },
    }


@mcp.tool()
def create_human_escalation(customer_id: str, order_id: str | None, reason: str, summary: str) -> dict:
    """
    Create a human escalation ticket.

    Use this when automation should stop, such as permission issues, policy exceptions,
    conflicting cstomer information, or high-risk cases.
    """
    return {
        "isError": False,
        "escalation": {
            "ticket_id": "TCK-9001",
            "customer_id": customer_id,
            "order_id": order_id,
            "reason": reason,
            "status": "open",
        },
    }


if __name__ == "__main__":
    mcp.run()
