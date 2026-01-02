# OpenManus - Refactored

A minimal AI agent framework focused on core functionality.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the agent
python openmanus_refactored/run.py --prompt "Your task here"

# Or run interactively
python openmanus_refactored/run.py
```

## Configuration

Copy the config template from the original project:

```bash
cp config/config.example.toml config/openmanus_config.toml
```

Edit the config file to add your API keys and settings.

## Project Structure

```
openmanus_refactored/
├── core/           # Core agent framework
│   ├── agent.py         # Base agent class
│   ├── manus.py         # Manus agent implementation
│   ├── llm.py           # LLM client
│   ├── config.py        # Configuration management
│   ├── logger.py        # Logging utilities
│   └── schema.py        # Data models
├── tools/          # Essential tools
│   ├── base.py          # Base tool class
│   ├── tool_collection.py  # Tool management
│   ├── str_replace_editor.py  # File editing
│   ├── file_operators.py     # File operations
│   ├── bash.py          # Shell command execution
│   └── python_execute.py     # Python code execution
├── utils/          # Utility functions
├── run.py          # Main entry point
└── requirements.txt
```

## Key Features

- **Minimal Design**: Only core functionality, no bloat
- **Tool-Based Architecture**: Extensible tool system
- **Multi-LLM Support**: Works with OpenAI, Anthropic, and more
- **File Operations**: Read, write, and edit files
- **Code Execution**: Safe Python execution
- **Shell Commands**: Execute terminal commands

## Usage Examples

```bash
# Simple task
python openmanus_refactored/run.py --prompt "List all Python files in current directory"

# Complex task with more steps
python openmanus_refactored/run.py --prompt "Analyze the codebase and summarize" --max-steps 20

# Interactive mode
python openmanus_refactored/run.py
```

## Migration from Original Project

This refactored version removes:
- Multilingual documentation (README_zh.md, README_ko.md, etc.)
- Examples directory
- Test files
- Assets and media
- GitHub workflows
- Protocol definitions
- Alternative sandbox implementations
- Multi-agent flow system
- Some specialized tools

The core functionality remains intact and fully functional.

## License

Same as the original OpenManus project.
