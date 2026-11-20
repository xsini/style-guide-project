"""Check project-specific documentation structure without external services."""
from pathlib import Path
import re
import sys
import yaml

root = Path(__file__).resolve().parents[1]
config = yaml.safe_load((root / 'mkdocs.yml').read_text(encoding='utf-8'))

def nav_paths(items):
    result = set()
    for item in items:
        if isinstance(item, str):
            result.add(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    result.add(value)
                else:
                    result.update(nav_paths(value))
    return result

nav = nav_paths(config['nav'])
errors = []
files = list((root / 'docs').rglob('*.md'))
for file in files:
    rel = file.relative_to(root / 'docs').as_posix()
    text = file.read_text(encoding='utf-8')
    # Ignore code examples: their headings do not belong to the host page.
    prose = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text, flags=re.M | re.S)
    headings = re.findall(r'^# ', prose, flags=re.M)
    if len(headings) != 1:
        errors.append(f'{rel}: expected one H1, found {len(headings)}')
    if rel not in nav:
        errors.append(f'{rel}: missing from nav')
for rel in nav:
    if not (root / 'docs' / rel).is_file():
        errors.append(f'{rel}: nav target does not exist')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(files)} pages, one H1 per page, all nav targets present')
