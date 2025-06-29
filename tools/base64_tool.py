import base64
from langchain.agents import tool

@tool
def decode_base64(encoded_string: str) -> str:
    """Decodes a base64-encoded string."""
    try:
        decoded = base64.b64decode(encoded_string.encode("utf-8")).decode("utf-8")
        return decoded
    except Exception as e:
        return f"Error decoding string: {e}"
