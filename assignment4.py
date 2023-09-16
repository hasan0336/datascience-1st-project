import re
# Raw Text: Extract all valid Pakistani phone numbers from a given text.
text = """Please contact me at 0301-1234567 or 042-35678901 for further details."""
pattern = r"\b03\d{2}-\d{7}\b|\b0\d{2}-\d{7,8}"
print(re.findall(pattern,text))

#  Extract all Pakistani CNIC (Computerized National Identity Card) numbers from a given text.
text2= """My CNIC is 12345-6789012-3 and another one is 34567-8901234-5."""

pattern2 = r"\b\d{5}-\d{7}-\d{1}\b"
print(re.findall(pattern2,text2))

# Identify and extract Urdu words from a mixed English-Urdu text.
textmixed= """یہ sentence میں کچھ English words بھی ہیں۔"""
urduPatter = r"[\u0600-\u06FF]+"

print(re.findall(urduPatter,textmixed))

#Raw Text: Find and extract dates in the format DD-MM-YYYY from a given text.
datetext = """The event will take place on 15-08-2023 and 23-09-2023."""
datePattern = r"\b\d{2}-\d{2}-\d{4}\b"
print(re.findall(datePattern,datetext))

#Raw Text: Extract all URLs from a text that belong to Pakistani domains.
urlText = "Visit http://www.example.pk or https://website.com.pk for more information."

urlPattern = r"\bf{2}\b"
print(re.findall(urlPattern,urlText))

#Raw Text: The product costs PKR 1500, while the deluxe version is priced at Rs. 2500.
pattern = r'(PKR|Rs\.)\s*(\d+)'
matches = re.findall(pattern, text)
amounts = [int(match[1]) for match in matches]
print(amounts)

#Raw Text: کیا! آپ, یہاں؟
cleaned_text = re.sub(r'[^\w\s]', '', rp)
print(cleaned_text)


#Raw Text: Lahore, Karachi, Islamabad, and Peshawar are major cities of Pakistan.
cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Multan", "Quetta", "Faisalabad", "Rawalpindi", "Sialkot", "Gujranwala"]
pattern = r'\b(?:' + '|'.join(cities) + r')\b'
matches = re.findall(pattern, text)
print(matches)



#Raw Text: I saw a car with the number plate LEA-567 near the market.
pattern = r'\b[A-Z]{3}-\d{3}\b'
matches = re.findall(pattern, text)
print(matches)