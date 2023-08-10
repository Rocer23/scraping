import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/page/'

data_quotes = {}

for i in range(1, 11):
    response = requests.get(url + str(i) + "/")

    with open(f"pages/page_{i}.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    with open(f"pages/page_{i}.html", "r", encoding='utf-8') as file:
        page_data = file.read()

    soup = BeautifulSoup(page_data, "lxml")

    quotes = soup.find_all('span', class_="text")
    authors = soup.find_all('small', class_="author")

    for j in range(len(quotes)):
        quote = quotes[j].text[1:-1]
        author = authors[j].text

        if author not in data_quotes:
            data_quotes[author] = [quote]
        else:
            data_quotes[author] = data_quotes[author] + [quote]

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data_quotes, file, ensure_ascii=False, indent=4)
