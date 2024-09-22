import os
from collections import Counter
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up command-line arguments
parser = argparse.ArgumentParser(description='Analyze word frequency in article titles.')
parser.add_argument('input_file', type=str, help='The input file with article titles')
args = parser.parse_args()

# Check if the input file exists
if not os.path.exists(args.input_file):
    logging.error(f"Input file {args.input_file} does not exist.")
    exit(1)

# Load the titles from the file
with open(args.input_file, 'r') as file:
    data = file.read()

# Split the titles into words and count word occurrences
words = data.split()
word_count = Counter(words)

# Print the most common words
logging.info("Most common words in article titles:")
for word, count in word_count.most_common(10):
    logging.info(f"{word}: {count}")