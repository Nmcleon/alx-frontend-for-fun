#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.
"""

import sys
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_text = md_file.read()
            html_text = markdown.markdown(markdown_text)
            with open(output_file, 'w') as out_file:
                out_file.write(html_text)
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
        
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)

if __name__ == "__main__":
    main()

