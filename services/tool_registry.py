from services.tools.calculator import calculate
from services.tools.web_search import web_search


TOOLS = {
    "calculator": {
        "func": calculate,
        "description": "Perform basic arithmetic calculations",
        "args": ["expression"]
    },
    
    "web_search": {
        "func": web_search,
        "description": "Search the web for information",
        "args": ["query"]
    }
}
