# Import necessary libraries
import requests  # For making HTTP requests
import re        # For regular expressions
from bs4 import BeautifulSoup  # For parsing HTML

# Define the URL of the web page you want to fetch
PAGE_URL = 'http://target:port'

# Define a function to fetch HTML content from a given URL
def get_html_of(url):
    # Send an HTTP GET request to the specified URL
    resp = requests.get(url)

    # Check if the HTTP response status code is not 200 (OK)
    if resp.status_code != 200:
        # Print an error message and exit the script with a non-zero status code
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    # Decode the response content from bytes to a string and return it
    return resp.content.decode()

# Call the get_html_of function to fetch the HTML content of the web page
html = get_html_of(PAGE_URL)

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Get the raw text content from the HTML (stripped of HTML tags)
raw_text = soup.get_text()

# Use regular expressions to find all words in the raw text
all_words = re.findall(r'\w+', raw_text)
