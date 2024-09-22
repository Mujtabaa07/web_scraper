import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['article_db']
collection = db['article_titles']

def scrape_titles():
    url = 'https://example.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('h2', class_='article-title')
    for title in titles:
        collection.insert_one({'title': title.get_text()})

if __name__ == '__main__':
    scrape_titles()