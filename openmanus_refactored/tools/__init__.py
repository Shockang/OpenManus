from .base import BaseTool, ToolFailure, ToolResult
from .tool_collection import ToolCollection
from .terminate import Terminate

# Try to import optional tools, use stubs if not available
try:
    from .create_chat_completion import CreateChatCompletion
except ImportError:
    from .base import BaseTool

    class CreateChatCompletion(BaseTool):
        """Stub for CreateChatCompletion - not available in minimal version"""
        name = "create_chat_completion"
        description = "Create chat completion (not available in minimal version)"
        parameters = {"type": "object", "properties": {}}

        async def run(self, **kwargs):
            from .base import ToolResult
            return ToolResult(output="", error="CreateChatCompletion not available in minimal version")

__all__ = [
    "BaseTool",
    "ToolFailure",
    "ToolResult",
    "ToolCollection",
    "Terminate",
    "CreateChatCompletion",
]
