import requests

# URL to fetch the city information
url = "https://ipinfo.io/loc"

# Sending a GET request to the URL
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    rt = response.text
    # Printing the content of the response
    print(rt)
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")
