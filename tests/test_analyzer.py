import unittest
from analyzer import analyze_titles

class TestAnalyzer(unittest.TestCase):
    def test_analyze_titles(self):
        titles = ["Title 1", "Title 2", "Title 3"]
        word_count = analyze_titles(titles)
        self.assertIsInstance(word_count, dict)
        self.assertGreater(len(word_count), 0)

if __name__ == '__main__':
    unittest.main()