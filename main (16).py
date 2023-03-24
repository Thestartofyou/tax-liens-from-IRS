import requests
from bs4 import BeautifulSoup

# Define the URL for the IRS's tax lien search page
url = 'https://www.irs.gov/pub/irs-drop/n-20-18.csv'

# Send a request to the URL and get the CSV response
response = requests.get(url)
csv_data = response.content.decode('utf-8')

# Parse the CSV data using the built-in `csv` module
import csv
reader = csv.reader(csv_data.splitlines())

# Iterate through each row of the CSV data and look for tax liens
for row in reader:
    # Check if the row contains information about a tax lien
    if 'lien' in row[0].lower():
        # Print the information about the tax lien
        print('Tax lien found:', row)

