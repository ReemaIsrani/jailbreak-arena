from langchain.tools import Tool
from tools.base64_tool import decode_base64
from tools.search_tool import search

ALL_TOOLS = {
    "base64": decode_base64,
    "search": search
}

def get_tools_by_name(names):
    return [ALL_TOOLS[name] for name in names if name in ALL_TOOLS]