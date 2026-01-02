#!/usr/bin/env python3
"""
Script to clean up non-essential files and directories from the project.

WARNING: This will DELETE files and directories. Use with caution!
"""
import os
import shutil

# Files and directories to remove
ITEMS_TO_REMOVE = [
    # Documentation files
    "README_zh.md",
    "README_ko.md",
    "README_ja.md",
    "CODE_OF_CONDUCT.md",
    ".github/PULL_REQUEST_TEMPLATE.md",

    # Directories
    "examples",
    "tests",
    "assets",
    "protocol",
    "app/daytona",
    "app/flow",
    "app/prompt",
    "app/sandbox",
    "app/mcp",
    "app/tool/chart_visualization",
    "app/tool/search",
    "app/tool/sandbox",

    # Alternative entry points
    "run_flow.py",
    "run_mcp.py",
    "run_mcp_server.py",
    "sandbox_main.py",

    # AWS specific (optional)
    "app/bedrock.py",

    # Alternative agents (optional)
    "app/agent/browser.py",
    "app/agent/data_analysis.py",
    "app/agent/mcp.py",
    "app/agent/sandbox_agent.py",
    "app/agent/swe.py",

    # Optional tools
    "app/tool/ask_human.py",
    "app/tool/browser_use_tool.py",
    "app/tool/computer_use_tool.py",
    "app/tool/crawl4ai.py",
    "app/tool/create_chat_completion.py",
    "app/tool/mcp.py",
    "app/tool/planning.py",
    "app/tool/terminate.py",
    "app/tool/web_search.py",
]

def remove_item(path):
    """Remove a file or directory"""
    if not os.path.exists(path):
        print(f"  Skipping (not found): {path}")
        return False

    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"  Removed file: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"  Removed directory: {path}")
        return True
    except Exception as e:
        print(f"  Error removing {path}: {e}")
        return False

def main():
    """Main cleanup function"""
    print("="*80)
    print("OpenManus Cleanup Script")
    print("="*80)
    print("\nThis script will remove the following non-essential items:")
    print("\n".join(f"  - {item}" for item in ITEMS_TO_REMOVE))

    response = input("\nAre you sure you want to continue? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Cleanup cancelled.")
        return

    print("\nStarting cleanup...")
    removed_count = 0

    for item in ITEMS_TO_REMOVE:
        if remove_item(item):
            removed_count += 1

    print(f"\nCleanup complete! Removed {removed_count} items.")
    print("\nNOTE: The refactored version is in the 'openmanus_refactored' directory.")
    print("You can now use that as the main project.")

if __name__ == "__main__":
    main()
