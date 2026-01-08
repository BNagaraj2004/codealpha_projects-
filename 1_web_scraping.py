import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 51):
    try:
        print(f"Scraping page {page}")
        response = requests.get(BASE_URL.format(page), timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed on page {page}: {e}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        try:
            title = book.h3.a.get("title", "").strip()
            price = book.find("p", class_="price_color")
            price = price.text.strip() if price else "0"

            rating_tag = book.find("p", class_="star-rating")
            rating = rating_tag["class"][1] if rating_tag else "Zero"

            availability_tag = book.find("p", class_="instock availability")
            availability = availability_tag.text.strip() if availability_tag else "Unknown"

            all_books.append([title, price, rating, availability])

        except Exception as e:
            print("Error parsing book:", e)
            continue

    time.sleep(1)

df = pd.DataFrame(
    all_books,
    columns=["Title", "Price", "Rating", "Availability"]
)

df.to_csv("books_raw_data.csv", index=False, encoding="utf-8")

print("✅ Web scraping completed successfully.")
