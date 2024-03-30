#!/usr/bin/python3
import sys
import re

def convert_headings(markdown_text):
    """
    Converts Markdown headings to HTML.
    """
    # Regular expression to match Markdown headings
    heading_pattern = re.compile(r'^(#{1,6})\s+(.*)$')
    
    html_lines = []
    for line in markdown_text.split('\n'):
        match = heading_pattern.match(line)
        if match:
            # Extract the heading level and text
            level = len(match.group(1))
            text = match.group(2)
            # Convert to HTML heading tag
            html_line = f'<h{level}>{text}</h{level}>\n'
            html_lines.append(html_line)
        else:
            # If not a heading, keep the line as is
            html_lines.append(line + '\n')
    
    return ''.join(html_lines)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        markdown_text = f.read()
    
    html_text = convert_headings(markdown_text)
    
    with open(output_file, 'w') as f:
        f.write(html_text)

if __name__ == "__main__":
    main()

