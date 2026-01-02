# OpenManus Refactoring - Shared Task Notes

## Current Status

**Iteration**: 1
**Date**: 2026-01-02
**Goal**: Refactor the entire project into Python scripts, removing non-essential code and documentation

## What Was Done

### 1. Created Refactored Structure
A new `openmanus_refactored/` directory was created with the following structure:

```
openmanus_refactored/
├── core/               # Core agent framework
│   ├── agent.py             # Base agent class
│   ├── manus.py             # Manus agent implementation
│   ├── toolcall_agent.py    # Tool-calling agent base
│   ├── llm.py               # LLM client
│   ├── config.py            # Configuration management
│   ├── logger.py            # Logging utilities
│   └── schema.py            # Data models
├── tools/              # Essential tools
│   ├── base.py              # Base tool class
│   ├── tool_collection.py   # Tool management
│   ├── str_replace_editor.py # File editing
│   ├── file_operators.py    # File operations
│   ├── bash.py              # Shell execution
│   └── python_execute.py    # Python execution
├── run.py              # Main entry point
├── requirements.txt    # Simplified dependencies
└── README.md           # Basic documentation
```

### 2. Updated All Imports
- Created and ran `fix_imports.py` script to update all imports from `app.*` to `openmanus_refactored.*`
- All files now use the new import structure

### 3. Created Essential Scripts
- `run.py`: Main entry point for running the agent
- `requirements.txt`: Simplified dependency list (removed unnecessary packages)
- `README.md`: Basic documentation for the refactored version
- `cleanup_project.py`: Script to remove non-essential files from original project

## What Still Needs to Be Done

### Immediate Next Steps

1. **Fix Import Dependencies**
   - The refactored files still have dependencies on removed modules (sandbox, prompt, etc.)
   - Need to either:
     - Copy missing dependencies (prompt templates)
     - Remove functionality that depends on removed modules
     - Create stub implementations

2. **Test the Refactored Code**
   - Test basic agent execution
   - Verify all imports work correctly
   - Test tool functionality
   - Fix any runtime errors

3. **Handle Missing Modules**
   The following are referenced but not copied:
   - `app/prompt/*.py` - Prompt templates for different agents
   - `app/utils/*.py` - Utility functions
   - `app/exceptions.py` - Custom exceptions

4. **Configuration Management**
   - Need to update config file references
   - Ensure config loading works with new structure

5. **Optional: Remove Original Files**
   - Run `cleanup_project.py` to remove non-essential files
   - Decide whether to keep original structure alongside refactored version

### Known Issues

1. **Sandbox Dependencies**: Many files import `from app.sandbox.client import SANDBOX_CLIENT` which doesn't exist in refactored version
   - Solution: Either remove sandbox calls or create a stub implementation

2. **Prompt Templates**: Agent implementations use prompt templates from `app/prompt/`
   - Need to copy these or integrate them into agent classes

3. **Tool Dependencies**: Some tools depend on removed search tools
   - May need to update tool_collection.py to handle missing tools

4. **Utils**: File operations depend on `app/utils/files_utils.py`
   - Need to copy this file

## Architecture Decisions

### What Was Kept
- Core agent framework (base, manus, toolcall)
- Essential tools (file operations, bash, python execution)
- LLM client with multi-provider support
- Configuration management
- Logging system
- Data schemas

### What Was Removed
- All documentation (multilingual READMEs, examples)
- Test files
- Assets and media
- GitHub workflows
- Protocol definitions
- Multi-agent flow system
- Sandbox implementation
- MCP integration
- Browser automation tools
- Search tools
- Chart visualization
- Alternative agents (browser, data_analysis, mcp, sandbox_agent, swe)

## Testing Checklist

When continuing this work:

- [ ] Fix all import errors in refactored code
- [ ] Test basic agent execution: `python openmanus_refactored/run.py --prompt "test"`
- [ ] Verify file operations work
- [ ] Verify bash tool works
- [ ] Verify python execution works
- [ ] Test with real LLM API
- [ ] Run cleanup script (if desired)
- [ ] Update main README to point to refactored version

## File Locations

- **Refactored Code**: `/Users/shockang/code/github/OpenManus/openmanus_refactored/`
- **Cleanup Script**: `/Users/shockang/code/github/OpenManus/cleanup_project.py`
- **Import Fix Script**: `/Users/shockang/code/github/OpenManus/openmanus_refactored/fix_imports.py`

## Notes for Next Developer

1. The refactored version is in `openmanus_refactored/` and is separate from the original code
2. All imports have been updated but some dependencies are missing
3. The main entry point is `openmanus_refactored/run.py`
4. Before testing, ensure you have a valid config file with API keys
5. The cleanup script is safe to run - it asks for confirmation first
6. Consider whether you want to remove the original files or keep them for reference

## Completion Criteria

The refactoring is complete when:
- All imports in `openmanus_refactored/` work without errors
- The agent can run a simple task successfully
- All core tools are functional
- Documentation is updated
- Original non-essential files are removed (optional)
