import requests
from bs4 import BeautifulSoup

manga_name = input("Enter the manga name: ")

search_url = f"https://mangareader.to/search?keyword={manga_name}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(search_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.text)

