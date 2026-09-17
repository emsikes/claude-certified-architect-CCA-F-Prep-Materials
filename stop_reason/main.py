import os
import asyncio
from anthropic import AsyncAnthropic, DefaultAioHttpClient
import os
from dotenv import load_dotenv

load_dotenv(override=True)


async def main() -> None:
    tools = [
        "name": "add_two_numbers",
        "description": "Use this tool to add two numbers together"
    ]
    async with AsyncAnthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        http_client=DefaultAioHttpClient(),
    ) as client:
        message = await client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, Claude",
                }
            ],
            model="claude-haiku-4-5-20251001",
        )
        print(message.content)


asyncio.run(main())
