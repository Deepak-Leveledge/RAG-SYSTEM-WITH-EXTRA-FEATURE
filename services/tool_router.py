import os
import json
import google.generativeai as genai
from services.tool_registry import TOOLS

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3-pro-preview")


def execute_tool(question: str):
    tool_decision = select_tool(question)

    if not tool_decision:
        return None

    tool_name = tool_decision["tool"]
    arguments = tool_decision.get("arguments", {})

    tool_info = TOOLS.get(tool_name)
    if not tool_info:
        return None

    try:
        result = tool_info["func"](**arguments)
        return {
            "answer": f"Tool used: {tool_name}\nResult: {result}",
            "sources": []
        }
    except Exception:
        return {
        "answer": "Tool {tool_name}execution failed. Falling back to general response.",
        "sources": []
    }

def select_tool(question: str) -> dict | None:
    """
    Decide which tool to use and extract arguments.
    Returns:
    {
      "tool": "calculator",
      "arguments": { "expression": "12500 * 0.18" }
    }
    """

    tool_descriptions = "\n".join([
        f"- {name}: {info['description']} | args: {info['args']}"
        for name, info in TOOLS.items()
    ])

    prompt = f"""
You are a tool selector AI.

Available tools:
{tool_descriptions}

Given the user question, choose the correct tool and arguments.

Rules:
- Use ONLY the available tools
- Respond ONLY in valid JSON
- Do NOT explain anything

User question:
{question}

JSON response:
""".strip()

    try:
        response = model.generate_content(prompt)
        data = json.loads(response.text)

        tool_name = data.get("tool")

        if tool_name not in TOOLS:
            return None

        return data

    except Exception:
        return None
