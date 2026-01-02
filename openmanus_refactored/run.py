#!/usr/bin/env python3
"""
OpenManus - Main entry point
Run AI agent with a prompt
"""
import argparse
import asyncio
import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openmanus_refactored import Manus, logger


async def main():
    """Main entry point for OpenManus agent"""
    parser = argparse.ArgumentParser(
        description="OpenManus - A minimal AI agent framework"
    )
    parser.add_argument(
        "--prompt", type=str, required=False, help="Input prompt for the agent"
    )
    parser.add_argument(
        "--max-steps", type=int, default=10, help="Maximum execution steps (default: 10)"
    )
    args = parser.parse_args()

    try:
        # Create and initialize Manus agent
        logger.info("Initializing OpenManus agent...")
        agent = await Manus.create()

        # Set max steps if provided
        if args.max_steps:
            agent.max_steps = args.max_steps

        # Get prompt from command line or interactive input
        prompt = args.prompt if args.prompt else input("Enter your prompt: ")

        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return

        logger.info("Processing your request...")
        result = await agent.run(prompt)

        logger.info("Request processing completed.")
        print("\n" + "="*80)
        print("RESULT:")
        print("="*80)
        print(result)

    except KeyboardInterrupt:
        logger.warning("\nOperation interrupted by user.")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Cleanup
        try:
            await agent.cleanup()
        except:
            pass


if __name__ == "__main__":
    asyncio.run(main())
