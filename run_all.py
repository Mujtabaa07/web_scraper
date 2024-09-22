import os
import logging
import requests
from bs4 import BeautifulSoup
from collections import Counter
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

url = config['url']
output_file = config['output_file']

# Create output directory if it doesn't exist
output_dir = os.path.dirname(output_file)
os.makedirs(output_dir, exist_ok=True)

# Function to scrape titles
def scrape_titles(url, output_file):
    logging.info("Scraping titles...")
    try:
        response = requests.get(url)
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
        with open(output_file, 'w') as file:
            file.write("Article Titles:\n")
            
            # Write each title to the file
            for i, title in enumerate(titles, 1):
                file.write(f"{i}. {title.text}\n")
        
        logging.info(f"Titles saved to {output_file}")
    except PermissionError as e:
        logging.error(f"PermissionError: {e}")
        logging.error("Please check the file permissions and try again.")
        exit(1)

# Function to analyze titles
def analyze_titles(input_file):
    logging.info("Analyzing titles...")
    if not os.path.exists(input_file):
        logging.error(f"Input file {input_file} does not exist.")
        exit(1)

    # Load the titles from the file
    with open(input_file, 'r') as file:
        data = file.read()

    # Split the titles into words and count word occurrences
    words = data.split()
    word_count = Counter(words)

    # Print the most common words
    logging.info("Most common words in article titles:")
    for word, count in word_count.most_common(10):
        logging.info(f"{word}: {count}")

# Run the scraper
scrape_titles(url, output_file)

# Run the analyzer
analyze_titles(output_file)