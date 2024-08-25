import sys
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    sys.stderr.write("Missing " + input_file + "\n")
    sys.exit(1)

# Convert Markdown to HTML and save to output_file

sys.exit(0)