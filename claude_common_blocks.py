""" 
content is a list of blocks, and on current models the first one is often a ThinkingBlock, not a TextBlock.

Why it's intermittent

With adaptive thinking, Claude decides whether and how much to think on each request, and at lower effort settings it may skip thinking entirely on easy inputs. Your earlier prompt was simple enough that Claude answered directly, so content[0] happened to be text. "I want to return my order" is ambiguous — no order ID, no reason, unclear whether policy applies — so Claude thought first, and content[0] became a thinking block.
"""


def text_of(message) -> str:
    """Concatenate all text blocks, ignoring thinking and tool_use."""
    return "".join(b.text for b in message.content if b.type == "text")


def tool_calls(message) -> list:
    """All tool_use blocks — may be more than one (parallel tool use)."""
    return [b for b in message.content if b.type == "tool_use"]


def thinking_of(message) -> str:
    return "".join(b.thinking for b in message.content if b.type == "thinking")
