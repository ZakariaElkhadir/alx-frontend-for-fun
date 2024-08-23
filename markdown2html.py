#!/usr/bin/python3
import sys
import os


if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

markdown_file = sys.argv[1]
output = sys.argv[2]

if not os.path.isfile(markdown_file):
    print("Missing <filename>", file=sys.stderr)
    exit(1)

with open(markdown_file, "r") as file:
    content = file.readlines()


content_mark = "good"
header = {
    "#": lambda: f"<h1>{content_mark}</h1>",
    "##": lambda: f"<h2>{content_mark}</h2>",
    "###": lambda: f"<h3>{content_mark}</h3>",
    "####": lambda: f"<h4>{content_mark}</h4>",
    "#####": lambda: f"<h5>{content_mark}</h5>",
    "######": lambda: f"<h6>{content_mark}</h6>",
}
for line in content:
    # strip to remove trailing and whitespaces
    line = line.strip()
    if line in header:
        print(header[line]())

exit(0)
