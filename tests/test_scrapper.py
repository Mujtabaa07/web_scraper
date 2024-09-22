import unittest
from scraper import scrape_titles

class TestScraper(unittest.TestCase):
    def test_scrape_titles(self):
        url = 'https://www.bbc.com/news'
        titles = scrape_titles(url)
        self.assertIsInstance(titles, list)
        self.assertGreater(len(titles), 0)

if __name__ == '__main__':
    unittest.main()