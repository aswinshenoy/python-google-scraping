import requests		# Requests required to obtain webpage
import bs4		# BS4 required to parse webpage

print("GOOGLE SCRAPING USING PY3 AND BS4 \n")

#User Can Enter Search Query
query = input("ENTER SEARCH QUERY: ")

url = "https://google.co.in/search?q=" + query;

# Gets response from the server
response = requests.get(url)

# Response text from server is parsed using bs4
soup = bs4.BeautifulSoup(response.text,'lxml')

# Titles of results are found (Assumed that Google put h3 only on result titles)
titles = soup.find_all("h3")

print("\nDISPLAYING FIRST PAGE RESULT TITLES FOR " + query + "\n")

x = 0; # counter variable
for title in titles: #loop to display titles
	x=x+1 # counter updated
	print( str(x) + ". " + title.get_text() )


