#!usr/bin/env python3

#importing python built-in module

import re 


Text= """Hello team,

Please contact us at support@elytica.com for more details.
You can also visit our site at https://www.elytica.com or https://elevatetech.elytica.org/page for updates.
For inquiries, call (+250) 789-221-439, or (+250)-795-520-704.
To process payments, we accept credit cards such as 1234 5678 9012 3456 and 1234-5678-9012-3456.
Our office hours are from 08:00 to 17:30 or book appointments at 9:30 AM.
Some HTML samples:
<p>Welcome to our platform!</p>
<img src="image.jpg" alt="description">
We are trending on social media! Follow #Techinnovate and #ElevateTech to stay updated.
Our premium package costs $19.99, and the full bundle is available for $1,234.56.
mv HACKATHON.py regex-data-extractor.py
python regex-data-extractor.py
Regards,
The Team
"""

# Regex patterns
regex= {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "url": r"https?://[^\s]+\b",
    "phone": r"\(?\+250\)?[-\s]?\d{3}-\d{3}-\d{3}\b",
    "credit_card": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "time": r"\b(?:[01]\d|2[0-3]):[0-5]\d\b|\b(?:0?[1-9]|1[0-2])\s?(?:AM|PM)\b",
    "html_tags": r"<[^>]+>",
    "hashtag": r"#\w+",
    "currency": r"\$\d+(?:,\d{3})*(?:\.\d{2})?"
}
    

# functions to search and print matches 
# using findall  
def regex_pattern(label, regex, text):
    matches = re.findall(regex, text)
    print(f"{label}:")
    if matches:
        for match in matches:
            print(match)
    print()  # Blank line between sections

regex_pattern("Email addresses", regex["email"], Text)
regex_pattern("URLs", regex["url"], Text)
regex_pattern("Phone numbers", regex["phone"], Text)
regex_pattern("Time", regex["time"], Text)
regex_pattern("HTML tags", regex["html_tags"], Text)
regex_pattern("Hashtags", regex["hashtag"], Text)
regex_pattern("Currency amounts", regex["currency"], Text)
regex_pattern("Credit card numbers", regex["credit_card"], Text)

