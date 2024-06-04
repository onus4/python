import requests
from bs4 import BeautifulSoup

def get_google_search_results(query):
    # Define the Google search URL
    url = f"https://www.google.com/search?q={query}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the search result divs
        search_results = soup.find_all("div", class_="g")

        # Extract the titles and URLs of the top 10 results
        top_10_results = []
        for result in search_results[:10]:
            title = result.find("h3", class_="LC20lb").text
            link = result.find("a")["href"]
            top_10_results.append((title, link))

        return top_10_results

# Test the function
query = "web scraping with python"
results = get_google_search_results(query)
for i, (title, link) in enumerate(results, start=1):
    print(f"{i}. {title} - {link}")