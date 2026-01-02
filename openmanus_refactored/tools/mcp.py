"""Stub implementation for MCP clients - MCP integration disabled in minimal version."""

from typing import Dict, List
from pydantic import Field


class MCPClients:
    """Stub implementation for MCP clients management."""

    def __init__(self):
        self.clients: Dict = {}

    async def connect_stdio(self, command: str, server_id: str, args: List[str] = None):
        """Stub: MCP not available in minimal version."""
        pass

    async def connect_sse(self, url: str, server_id: str):
        """Stub: MCP not available in minimal version."""
        pass

    async def get_tools(self) -> List:
        """Stub: Return empty list as MCP is not available."""
        return []

    async def cleanup(self):
        """Stub: No cleanup needed."""
        pass


class MCPClientTool:
    """Stub implementation for MCP client tool."""

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return "mcp_tool_stub"

    @property
    def description(self) -> str:
        return "MCP tool (not available in minimal version)"
