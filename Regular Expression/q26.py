# Program 26: Extract DOI identifiers, publication years, email addresses, and URLs from research paper references
import re

references = """
References:
1. Vaswani et al. (2017). "Attention Is All You Need." NeurIPS 2017. DOI: 10.48550/arXiv.1706.03762. Available at: https://arxiv.org/abs/1706.03762. Contact: vaswani@google.com.
2. LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444. DOI: 10.1038/nature14539. Visit: http://www.nature.com/articles/nature14539. Email: yann@cs.nyu.edu.
3. Goodfellow, I. et al. (2014). Generative Adversarial Nets. NIPS 2014. DOI: 10.1145/3422622. Url: https://papers.nips.cc/paper/5423. Inquiries: contact-nips@mit.edu.
"""

# Regex patterns
doi_pattern = r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b"
year_pattern = r"\b(19\d{2}|20\d{2})\b"
email_pattern = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b"
url_pattern = r"https?://[^\s,)]+"

dois = re.findall(doi_pattern, references)
years = sorted(set(re.findall(year_pattern, references)))
emails = re.findall(email_pattern, references)
urls = re.findall(url_pattern, references)

print("--- Extracted Information from Research References ---")
print("DOIs:", dois)
print("Publication Years:", years)
print("Email Addresses:", emails)
print("URLs:", urls)
