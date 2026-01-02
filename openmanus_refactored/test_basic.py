#!/usr/bin/env python3
"""
Basic test script for OpenManus refactored version.
Tests core functionality without requiring an LLM API key.
"""
import asyncio
import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openmanus_refactored import Manus
from openmanus_refactored.tools.str_replace_editor import StrReplaceEditor
from openmanus_refactored.tools.bash import Bash
from openmanus_refactored.tools.python_execute import PythonExecute


async def test_agent_initialization():
    """Test that the agent can be instantiated."""
    print("=" * 80)
    print("TEST 1: Agent Initialization")
    print("=" * 80)

    try:
        agent = Manus()
        print(f"✓ Agent class can be instantiated")
        print(f"✓ Agent has max_steps: {agent.max_steps}")
        print(f"✓ Agent has {len(agent.available_tools.tools)} tools:")
        for tool in agent.available_tools.tools:
            print(f"  - {tool.name}: {tool.description}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_str_replace_editor():
    """Test StrReplaceEditor tool."""
    print("\n" + "=" * 80)
    print("TEST 2: StrReplaceEditor Tool")
    print("=" * 80)

    try:
        editor = StrReplaceEditor()
        result = await editor.execute(
            command="view",
            path="/Users/shockang/code/github/OpenManus/openmanus_refactored/README.md"
        )
        print(f"✓ StrReplaceEditor.view() works")
        print(f"  - Returned {len(result)} characters")
        print(f"  - First 100 chars: {result[:100]}...")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_python_execute():
    """Test PythonExecute tool."""
    print("\n" + "=" * 80)
    print("TEST 3: PythonExecute Tool")
    print("=" * 80)

    try:
        python_tool = PythonExecute()
        result = await python_tool.execute(
            code='print("Hello from Python tool!"); result = 2 + 2; print(f"2 + 2 = {result}")'
        )
        print(f"✓ PythonExecute works")
        print(f"  - Output: {result}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_bash():
    """Test Bash tool."""
    print("\n" + "=" * 80)
    print("TEST 4: Bash Tool")
    print("=" * 80)

    try:
        bash = Bash()
        result = await bash.execute(command='echo "Hello from Bash tool!"')
        print(f"✓ Bash works")
        output = result.output if hasattr(result, "output") else result
        print(f"  - Output: {output}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run all tests."""
    print("\n" + "=" * 80)
    print("OpenManus Refactored - Basic Functionality Tests")
    print("=" * 80)
    print("\nThese tests verify core functionality without requiring an LLM API key.\n")

    results = []

    # Run all tests
    results.append(await test_agent_initialization())
    results.append(await test_str_replace_editor())
    results.append(await test_python_execute())
    results.append(await test_bash())

    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("\n✓ All tests PASSED! The refactored OpenManus is working correctly.")
        print("\nNext steps:")
        print("1. Add an LLM API key to config/openmanus_config.toml")
        print("2. Test with a real task: python -m openmanus_refactored.run --prompt 'Your task'")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) FAILED. Please check the errors above.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
