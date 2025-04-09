import requests
from bs4 import BeautifulSoup

manga_name = input("Enter the manga name: ")
search_url = f"https://mangapill.com/quick-search?q={manga_name}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("a", class_="grid-cols-1 bg-card rounded p-3")

manga_list = []

print("\nSearch Results:\n")
for index, result in enumerate(results, start=1):
    title = result.find("div", class_="font-black").text.strip()
    eng_title = result.find("div", class_="text-sm text-secondary").text.strip()
    link = "https://mangapill.com" + result["href"]
    img_tag = result.find("img")
    image_url = img_tag["src"] if img_tag else "No image"

    manga_list.append({
        "title": title,
        "english_title": eng_title,
        "link": link,
        "image": image_url
    })

    print(f"{index}. {title} ({eng_title})")

choice = int(input("\nEnter the number of the manga you want to select: "))
selected_manga = manga_list[choice - 1]

print('Fetching chapters\n')

manga_url = selected_manga['link']
response = requests.get(manga_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

chapter_section = soup.find("div", id="chapters")
chapter_links = chapter_section.find_all("a", href=True)

print(f"\nFound {len(chapter_links)} chapters:\n")

for chapter in chapter_links:
    chapter_title = chapter.text.strip()
    chapter_url = "https://mangapill.com" + chapter["href"]
    print(f"{chapter_title} -> {chapter_url}")
