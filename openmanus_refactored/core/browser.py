import json
from typing import TYPE_CHECKING, Optional

from openmanus_refactored.core.logger import logger

if TYPE_CHECKING:
    from openmanus_refactored.core.agent import BaseAgent


class BrowserContextHelper:
    def __init__(self, agent: "BaseAgent"):
        self.agent = agent
        self._current_base64_image: Optional[str] = None

    async def get_browser_state(self) -> Optional[dict]:
        """Get current browser state from browser tool if available."""
        # For minimal version, browser functionality is optional
        # Return None if browser tool is not available
        return None

    async def format_next_step_prompt(self) -> str:
        """Format browser state into prompt. Returns empty string for minimal version."""
        # For minimal version, we don't add browser context
        return ""

    async def cleanup_browser(self):
        """Cleanup browser resources if any."""
        pass
