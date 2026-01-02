import logging
import os
import sys

# Standard Python logger for minimal version
ENV_MODE = os.getenv("ENV_MODE", "LOCAL")

# Create logger
logger = logging.getLogger("openmanus")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Formatter
if ENV_MODE.lower() == "local":
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
else:
    formatter = logging.Formatter('%(message)s')

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

__all__ = ["logger"]
