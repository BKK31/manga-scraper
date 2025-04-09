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


manga_cards = soup.find_all("div", class_="item item-spc")

for card in manga_cards:
    print("")
    title_tag = card.find("h3", class_="manga-name").find("a")
    title = title_tag.text.strip()

    relative_url = title_tag["href"]
    full_url = "https://mangareader.to" + relative_url

    thumbnail_tag = card.find("a", class_="manga-poster").find("img")
    thumbnail_url = thumbnail_tag["src"]
