import os
import re

view_path = r'ipo_app\views.py'

with open(view_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find templates
templates_used = set(re.findall(r'[\'"]([a-zA-Z0-9_-]+\.html)[\'"]', content))

existing_templates = []
for root, dirs, files in os.walk('ipo_app'):
    for file in files:
        if file.endswith('.html'):
            existing_templates.append(file)

missing = [t for t in templates_used if t not in existing_templates]

print('Missing templates:', missing)
