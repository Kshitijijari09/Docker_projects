import requests

URL = 'http://www.imdb.com/chart/top'

def main():
    # Send an HTTP GET request to the URL
    response = requests.get(URL)

    # Check if the request was successful (status code 200 indicates success)
    if response.status_code == 200:
        # Print the content of the response (HTML content of the page)
        print(response.text)
    else:
        print(f"Failed to fetch the page. Status Code: {response.status_code}")

if __name__ == '__main__':
    main()