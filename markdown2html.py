#!/usr/bin/python3
"""Markdown to HTML converter"""
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

markdown_file = sys.argv[1]
output = sys.argv[2]

if not os.path.isfile(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    exit(1)

with open(markdown_file, "r") as file:
    content = file.readlines()

def parse_line(line):
    """Parses a line of Markdown and converts to HTML."""
    line = line.strip()
    if line.startswith('#'):
        heading_level = len(line) - len(line.lstrip('#'))
        if 1 <= heading_level <= 6:
            heading_content = line[heading_level:].strip()
            return f"<h{heading_level}>{heading_content}</h{heading_level}>"
    return None  # Ignore non-heading lines

html_lines = [parse_line(line) for line in content if parse_line(line)]

with open(output, "w") as html_file:
    html_file.write("\n".join(html_lines))

exit(0)
