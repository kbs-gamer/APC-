# Program 20: Extract file extensions from filenames in a given string
import re

text = "Files uploaded: report.pdf, data.csv, image.png, script.py, backup.tar.gz, archive.zip"

# Extract extensions preceded by a dot
extensions = re.findall(r"\.([a-zA-Z0-9]+)\b", text)

print("Text:", text)
print("Extracted file extensions:", extensions)
