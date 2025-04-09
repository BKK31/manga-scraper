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

    genre_tags = card.find("span", class_="fdi-item fdi-cate")
    genres = [genre.text.strip() for genre in genre_tags.find_all("a")] if genre_tags else []

    latest_chapter_tag = card.find("div", class_="tab-content").find("div", class_="fdl-item")
    if latest_chapter_tag:
        chapter_link = latest_chapter_tag.find("a")
        chapter_title = chapter_link.text.strip()
        chapter_url = "https://mangareader.to" + chapter_link["href"]
    else:
        chapter_title = "N/A"
        chapter_url = "N/A"
    
    print(f"Title: {title}")
    print(f"URL: {full_url}")
    print(f"Thumbnail: {thumbnail_url}")
    print(f"Genres: {genres}")
    print(f"Latest Chapter: {chapter_title}")
    print(f"Chapter URL: {chapter_url}")
    print("-" * 50)
