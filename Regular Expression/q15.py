# Program 15: Extract all hashtags from a social media post
import re

text = "Loving the journey of learning #Python and #MachineLearning! Stay focused #APC2026 #CodingLife."

hashtags = re.findall(r"#\w+", text)

print("Original Text:", text)
print("Extracted Hashtags:", hashtags)
