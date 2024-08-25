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

def parse_line(line, in_list):
    """Parses a line of Markdown and converts to HTML."""
    line = line.strip()
    
    # Handling headings
    if line.startswith('#'):
        heading_level = len(line) - len(line.lstrip('#'))
        if 1 <= heading_level <= 6:
            heading_content = line[heading_level:].strip()
            return f"<h{heading_level}>{heading_content}</h{heading_level}>", in_list
    
    # Handling unordered lists
    if line.startswith('-'):
        list_item = line[1:].strip()
        if not in_list:
            in_list = True
            return f"<ul>\n<li>{list_item}</li>", in_list
        else:
            return f"<li>{list_item}</li>", in_list
    
    # Close the list if there was a previous list and now there's no list item
    if in_list:
        in_list = False
        return f"</ul>\n{line}", in_list

    return line, in_list

with open(markdown_file, "r") as file:
    content = file.readlines()

html_lines = []
in_list = False

for line in content:
    parsed_line, in_list = parse_line(line, in_list)
    if parsed_line:
        html_lines.append(parsed_line)

# Close any open lists at the end of the file
if in_list:
    html_lines.append("</ul>")

with open(output_file, "w") as html_file:
    html_file.write("\n".join(html_lines))

exit(0)
