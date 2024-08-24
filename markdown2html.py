#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    exit(1)

# Open the markdown file and read the content
with open(markdown_file, "r") as file:
    lines = file.readlines()

# Function to convert a line to an HTML heading if it matches the Markdown heading syntax
def convert_to_html_heading(line):
    # Check for the level of the heading by counting the number of leading '#'
    stripped_line = line.lstrip()
    heading_level = len(stripped_line) - len(stripped_line.lstrip('#'))
    
    if 1 <= heading_level <= 6:  # If the heading level is between 1 and 6
        content = stripped_line[heading_level:].strip()
        return f"<h{heading_level}>{content}</h{heading_level}>"
    else:
        return line

# Convert each line in the Markdown file to HTML if it is a heading
html_lines = [convert_to_html_heading(line) for line in lines]

# Write the converted content to the output HTML file
with open(output_file, "w") as file:
    file.write("\n".join(html_lines))

exit(0)
