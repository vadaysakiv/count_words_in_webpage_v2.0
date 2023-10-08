# Import the 'requests' library for making HTTP requests
import requests

# Prompt the user to input an IP address and a port number
target = input("Enter the IP address: ")
port = input("Enter the port number: ")

# Construct the URL using the user-provided IP address and port number
page_url = f'http://{target}:{port}'

# Define a function to fetch the HTML content from a given URL
def get_html_of(url):
    # Send an HTTP GET request to the specified URL
    resp = requests.get(url)

    # Check if the HTTP response status code is not 200 (OK)
    if resp.status_code != 200:
        # Print an error message and exit the script with a non-zero status code
        print(f'HTTP status code of {resp.status_code}')
        exit(1)

    # Decode the response content from bytes to a string and return it
    return resp.content.decode()

# Call the 'get_html_of' function to fetch and print the HTML content from the constructed URL
print(get_html_of(page_url))
