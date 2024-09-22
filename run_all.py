import os
import subprocess
import time

# Start MongoDB
print("Starting MongoDB...")
subprocess.Popen(["mongod", "--dbpath", "data/db", "--logpath", "data/log/mongodb.log"])

# Wait for MongoDB to start
time.sleep(5)

# Run the scraper
print("Running scraper...")
os.system("python scraper.py")

# Run the analyzer
print("Running analyzer...")
os.system("python analyzer.py")

# Run the Flask application
print("Starting Flask application...")
os.system("python app.py")