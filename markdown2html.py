#!/usr/bin/python3
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as md_file:
        md_lines = md_file.readlines()

    html_content = ""
    for line in md_lines:
        stripped_line = line.strip()
        if stripped_line.startswith('#'):
            # Determine the heading level based on the number of '#' symbols
            heading_level = stripped_line.count('#')
            # Remove the '#' symbols and leading/trailing whitespace
            heading_text = stripped_line.lstrip('#').strip()
            # Generate the HTML heading tag
            html_content += f"<h{heading_level}>{heading_text}</h{heading_level}>\n"
        else:
            # For non-heading lines, simply add them as is
            html_content += line

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    main()

