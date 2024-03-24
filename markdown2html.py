#!/usr/bin/python3
import sys
import os
import markdown

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
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    main()

