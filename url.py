import string
import random

url_mapping = {}  # Dictionary to store the URL mappings

def generate_short_url():
    characters = string.ascii_letters + string.digits  # Generate a combination of letters and digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # Generate a 6-character short URL
    return short_url

def shorten_url(original_url):
    short_url = generate_short_url()
    url_mapping[short_url] = original_url
    return short_url

def expand_url(short_url):
    if short_url in url_mapping:
        return url_mapping[short_url]
    else:
        return None

# Example usage:
original_url = "https://www.example.com"
shortened_url = shorten_url(original_url)
print("Shortened URL:", shortened_url)

expanded_url = expand_url(shortened_url)
print("Expanded URL:", expanded_url)
