import os
from dotenv import load_dotenv

from anthropic import Anthropic


load_dotenv(override=True)

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=anthropic_api_key)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)
