#!/usr/bin/env python3
import os
import re

templates_dir = "/Users/chinmay/Desktop/DPDP/esahamati/docs/templates"

square_icon = '<i data-lucide="square" style="display:inline-block; vertical-align:text-bottom; width: 1em; height: 1em; margin-right: 4px;"></i>'
square_icon_middle = '<i data-lucide="square" style="display:inline-block; vertical-align:middle; width: 1em; height: 1em;"></i>'
barchart_icon = '<i data-lucide="bar-chart-3" style="display:inline-block; vertical-align:text-bottom; width: 1.2em; height: 1.2em; margin-right: 4px;"></i>'

emoji_checkbox = '☐'
emoji_chart = '📊'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = False
    
    # Replace patterns
    
    # 1. In table cells with just ☐ (centered or not)
    # Pattern: <td...>☐</td> with text-align: center
    content = re.sub(
        r'<td([^>]*)style="[^"]*text-align:\s*center[^"]*"[^>]*>' + emoji_checkbox + r'</td>',
        lambda m: '<td' + m.group(1) + '>' + square_icon_middle + '</td>',
        content
    )
    
    # 2. In table cells with just ☐ (any position)
    content = re.sub(
        r'<td([^>]*)>' + emoji_checkbox + r'</td>',
        lambda m: '<td' + m.group(1) + '>' + square_icon_middle + '</td>',
        content
    )
    
    # 3. In tracker-status divs: <div class="tracker-status">☐ Not Started</div>
    content = re.sub(
        r'<div class="tracker-status">' + emoji_checkbox + r'\s+([^<]+)</div>',
        lambda m: '<div class="tracker-status">' + square_icon + ' ' + m.group(1) + '</div>',
        content
    )
    
    # 4. In list items: <li>☐ text...
    content = re.sub(
        r'<li>' + emoji_checkbox + r'\s+([^<]+)</li>',
        lambda m: '<li>' + square_icon + ' ' + m.group(1) + '</li>',
        content
    )
    
    # 5. In list items with text after: <li>text ☐ text...
    content = re.sub(
        r'<li>([^<]*)' + emoji_checkbox + r'\s+([^<]+)</li>',
        lambda m: '<li>' + m.group(1) + square_icon + ' ' + m.group(2) + '</li>',
        content
    )
    
    # 6. In strong tags: <strong>☐ VALID...
    content = re.sub(
        r'<strong>' + emoji_checkbox + r'\s+([^<]+)</strong>',
        lambda m: '<strong>' + square_icon + ' ' + m.group(1) + '</strong>',
        content
    )
    
    # 7. For checkbox pairs like "☐ 0  ☐ 1" in tables
    content = re.sub(
        r'' + emoji_checkbox + r'\s+0\s+' + emoji_checkbox + r'\s+1',
        lambda m: square_icon_middle + ' 0 ' + square_icon_middle + ' 1',
        content
    )
    
    # 8. In text with space after (general fallback for ☐ followed by space and text)
    # This handles patterns like "☐ Reviewed" not caught above
    content = re.sub(
        r'' + emoji_checkbox + r'\s+(\S)',
        lambda m: square_icon + ' ' + m.group(1),
        content
    )
    
    # 9. Replace 📊 emoji
    content = content.replace(emoji_chart, barchart_icon)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Get all HTML files
html_files = [os.path.join(templates_dir, f) for f in os.listdir(templates_dir) if f.endswith('.html')]

modified_count = 0
for filepath in sorted(html_files):
    if process_file(filepath):
        modified_count += 1
        print(f"Modified: {os.path.basename(filepath)}")

print(f"\nTotal files modified: {modified_count}")