from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})

for i in range(len(quotes)):
    print(f'{authors[i].text}: {quotes[i].text}')
# print(print(quotes))