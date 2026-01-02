#!/usr/bin/env python3
"""
Script to update imports in refactored files
"""
import os
import re

def update_imports(file_path):
    """Update imports in a Python file"""
    with open(file_path, 'r') as f:
        content = f.read()

    original_content = content

    # Replace app imports with openmanus_refactored imports
    content = re.sub(r'from app\.', 'from openmanus_refactored.', content)
    content = re.sub(r'import app\.', 'import openmanus_refactored.', content)

    # Specific replacements
    content = re.sub(r'from openmanus_refactored\.schema', 'from openmanus_refactored.core.schema', content)
    content = re.sub(r'from openmanus_refactored\.config', 'from openmanus_refactored.core.config', content)
    content = re.sub(r'from openmanus_refactored\.logger', 'from openmanus_refactored.core.logger', content)
    content = re.sub(r'from openmanus_refactored\.llm', 'from openmanus_refactored.core.llm', content)
    content = re.sub(r'from openmanus_refactored\.agent\b', 'from openmanus_refactored.core.agent', content)
    content = re.sub(r'from openmanus_refactored\.tool', 'from openmanus_refactored.toolssss', content)
    content = re.sub(r'from openmanus_refactored\.sandbox', 'from openmanus_refactored.utils.sandbox', content)
    content = re.sub(r'from openmanus_refactored\.utils', 'from openmanus_refactored.utils', content)
    content = re.sub(r'from openmanus_refactored\.prompt', 'from openmanus_refactored.core.prompt', content)

    lines = content.split('\n')
    filtered_lines = []
    skip_next = False
    for i, line in enumerate(lines):
        filtered_lines.append(line)

    content = '\n'.join(filtered_lines)

    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    return False

def process_directory(directory):
    """Process all Python files in directory"""
    updated_count = 0
    for root, dirs, files in os.walk(directory):
        # Skip __pycache__ and .venv
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.venv', '.git']]

        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if update_imports(file_path):
                    print(f'Updated: {file_path}')
                    updated_count += 1

    print(f'\nTotal files updated: {updated_count}')

if __name__ == '__main__':
    process_directory('openmanus_refactored')
