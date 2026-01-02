"""Stub implementation for BrowserUseTool - browser automation disabled in minimal version."""

from openmanus_refactored.tools.base import BaseTool, ToolResult


class BrowserUseTool(BaseTool):
    """
    Stub implementation of BrowserUseTool.
    Browser automation is not available in the minimal version.
    """

    name: str = "browser_use"
    description: str = "Browser automation tool (not available in minimal version)"
    parameters: dict = {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "description": "The browser action to perform (not implemented)",
            }
        },
    }

    async def run(self, action: str = "") -> ToolResult:
        """Return error indicating browser tool is not available."""
        return ToolResult(
            output="",
            error="Browser automation is not available in the minimal version of OpenManus",
        )
