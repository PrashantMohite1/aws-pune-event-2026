from openai import OpenAI
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

client = OpenAI()

MODEL = "gpt-6-astra"

# Our tool: ordinary Python code
def check_website():
    request = Request(
        "https://example.com",
        headers={"User-Agent": "DevOpsAgentDemo/1.0"}
    )

    try:
        with urlopen(request, timeout=5) as response:
            return f"HTTP {response.status}"
    except HTTPError as error:
        return f"HTTP {error.code}"
    except URLError as error:
        return f"Connection failed: {error.reason}"


# Tell the AI what tool is available
tools = [
    {
        "type": "function",
        "name": "check_website",
        "description": "Check the health of the demo website.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    }
]

instructions = (
    "You are a DevOps assistant. "
    "Use the website-checking tool to check the demo website. "
    "Explain the result clearly."
)

# 1. Ask the AI to handle the task
response = client.responses.create(
    model=MODEL,
    instructions=instructions,
    input="Check whether the demo website is running.",
    tools=tools,
    tool_choice="required"
)

# 2. Find the tool call requested by the AI
calls = [
    item for item in response.output
    if item.type == "function_call"
]

if not calls:
    print(response.output_text)
else:
    call = calls[0]

    # 3. Execute our actual Python function
    if call.name == "check_website":
        result = check_website()
    else:
        raise ValueError(f"Unknown tool: {call.name}")

    print("Actual tool result:", result)

    # 4. Give the result back to the AI
    final_response = client.responses.create(
        model=MODEL,
        instructions=instructions,
        previous_response_id=response.id,
        input=[
            {
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": result
            }
        ],
        tools=tools,
        tool_choice="none"
    )

    # 5. Display the AI's explanation
    print(final_response.output_text)