import requests
from lxml import html

def get_html_headers(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    headers = tree.xpath("//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
    headers = [header.text_content().strip() for header in headers]
    return headers

# Example usage
url = input("Enter a URL: ")
headers = get_html_headers(url)

# Print all HTML headers
if headers:
    print("HTML Headers:")
    for header in headers:
        print(header)
else:
    print("No HTML headers found.")