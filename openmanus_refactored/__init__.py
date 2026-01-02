"""
OpenManus - A minimal AI agent framework

Refactored version focused on core functionality.
"""

__version__ = "1.0.0"

from .core.agent import BaseAgent
from .core.manus import Manus
from .core.llm import LLM
from .core.config import Config
from .core.schema import AgentState, Memory, Message
from .core.logger import logger

__all__ = [
    "BaseAgent",
    "Manus",
    "LLM",
    "Config",
    "AgentState",
    "Memory",
    "Message",
    "logger",
]
