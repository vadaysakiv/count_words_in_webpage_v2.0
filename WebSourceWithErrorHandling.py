# Import the 'requests' library for making HTTP requests
import requests

# Prompt the user to input an IP address and a port number
target = input("Enter the IP address: ")
port = input("Enter the port number: ")

# Construct the URL using the user-provided IP address and port number
page_url = f'http://{target}:{port}'

# Send an HTTP GET request to the constructed URL
resp = requests.get(page_url)

# Check if the HTTP response status code is not 200 (OK)
if resp.status_code != 200:
    # Print an error message and exit the script with a non-zero status code
    print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
    exit(1)

# Decode the response content from bytes to a string
html_str = resp.content.decode()

# Print the HTML content to the console
print(html_str)
