"""Stub implementation for sandbox client - sandbox disabled in minimal version."""

from typing import Optional


class SandboxClientStub:
    """Stub implementation for sandbox client."""

    def __init__(self):
        self.sandbox = None

    async def create(self, config=None):
        """Stub: Sandbox not available in minimal version."""
        raise NotImplementedError("Sandbox is not available in the minimal version of OpenManus")

    async def read_file(self, path: str) -> str:
        """Stub: Sandbox not available."""
        raise NotImplementedError("Sandbox is not available in the minimal version of OpenManus")

    async def write_file(self, path: str, content: str):
        """Stub: Sandbox not available."""
        raise NotImplementedError("Sandbox is not available in the minimal version of OpenManus")

    async def run_command(self, cmd: str, timeout: Optional[int] = None) -> str:
        """Stub: Sandbox not available."""
        raise NotImplementedError("Sandbox is not available in the minimal version of OpenManus")


# Global sandbox client instance
SANDBOX_CLIENT = SandboxClientStub()
