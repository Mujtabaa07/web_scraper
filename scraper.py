import requests
from bs4 import BeautifulSoup
import os
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up command-line arguments
parser = argparse.ArgumentParser(description='Web scraper for article titles.')
parser.add_argument('url', type=str, help='The URL of the website to scrape')
parser.add_argument('output_file', type=str, help='The output file to save the titles')
args = parser.parse_args()

# Create output directory if it doesn't exist
output_dir = os.path.dirname(args.output_file)
os.makedirs(output_dir, exist_ok=True)

# Send a GET request to fetch the page content
try:
    response = requests.get(args.url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.RequestException as e:
    logging.error(f"Failed to retrieve the webpage: {e}")
    exit(1)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles on the page
titles = soup.find_all('h3', class_='gs-c-promo-heading__title')

try:
    # Open a file to save the titles
    with open(args.output_file, 'w') as file:
        file.write("Article Titles:\n")
        
        # Write each title to the file
        for i, title in enumerate(titles, 1):
            file.write(f"{i}. {title.text}\n")
    
    logging.info(f"Titles saved to {args.output_file}")
except PermissionError as e:
    logging.error(f"PermissionError: {e}")
    logging.error("Please check the file permissions and try again.")
    exit(1)