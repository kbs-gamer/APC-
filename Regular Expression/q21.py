# Program 21: Remove HTML tags, extra whitespace, and unwanted punctuation from a text document
import re

html_doc = """
<div>
    <h1>Welcome to   Python & Data Science!!</h1>
    <p>This is a <b>sample</b> document with    extra spaces, tags, and punctuation (like @#$%, etc.).</p>
</div>
"""

# 1. Remove HTML tags
no_html = re.sub(r"<[^>]+>", " ", html_doc)

# 2. Remove unwanted punctuation (keep alphanumeric characters and whitespace)
no_punct = re.sub(r"[^\w\s]", "", no_html)

# 3. Normalize multiple whitespace into single space and strip
clean_text = re.sub(r"\s+", " ", no_punct).strip()

print("Original HTML Document:\n", html_doc)
print("\nCleaned Text:\n", clean_text)
