import urllib.request as libreq
import requests

url = 'http://export.arxiv.org/api/query'
search_query = input("Search: ")
params = {
    'search_query': 'all:electron',   # Search query, e.g., 'all:electron' searches all fields for 'electron'
    'id_list': '1234.5678,2345.6789', # Comma-separated list of arXiv IDs to retrieve specific articles
    'start': 0,                      # Specifies the starting point of results to fetch (for pagination)
    'max_results': 10,               # Limits the number of results returned
    'sortBy': 'submittedDate',       # Sorts results by criteria ('relevance', 'lastUpdatedDate', 'submittedDate')
    'sortOrder': 'descending',       # Order of the results ('ascending', 'descending')
    'cat': 'physics:cond-mat',       # Category to search within, e.g., 'physics:cond-mat' for Condensed Matter
}
response = requests.get(url, params=params)
if response.status_code == 200:
    print(response.text)
else:
    print("Failed to retrieve data:", response.status_code)

#with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
#    r = url.read()
#print(r)
