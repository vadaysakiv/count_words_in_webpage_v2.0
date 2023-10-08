import requests
import re
from bs4 import BeautifulSoup

# Define the URL to scrape
PAGE_URL = 'http://target:port'

# Function to retrieve HTML content from a URL
def get_html_of(url):
    # Send an HTTP GET request to the specified URL
    resp = requests.get(url)

    # Check if the response status code is 200 (OK)
    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    # Decode the response content and return it as a string
    return resp.content.decode()

# Function to count word occurrences in a list
def count_occurrences_in(word_list):
    word_count = {}

    # Loop through the words in the list
    for word in word_list:
        # Check if the word is already in the word_count dictionary
        if word not in word_count:
            # If not, add it with a count of 1
            word_count[word] = 1
        else:
            # If it exists, increment its count
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count

# Function to extract all words from a web page
def get_all_words_from(url):
    # Get the HTML content from the URL
    html = get_html_of(url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extract plain text from the HTML
    raw_text = soup.get_text()

    # Use regular expression to find all words in the text
    return re.findall(r'\w+', raw_text)

# Function to get the top words with the highest occurrences
def get_top_words_from(all_words):
    # Count word occurrences
    occurrences = count_occurrences_in(all_words)

    # Sort word occurrences in descending order
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

# Get all words from the web page
all_words = get_all_words_from(PAGE_URL)

# Get and print the top 10 words with the highest occurrences
top_words = get_top_words_from(all_words)
for i in range(10):
    print(top_words[i][0])
