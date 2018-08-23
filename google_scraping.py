import requests		# Requests required to obtain webpage
import bs4		# BS4 required to parse webpage

#Title Text Block
print("GOOGLE SCRAPING USING PY3 AND BS4 \n")

#Accepts Search Keywords from the User
keyword = input("ENTER SEARCH KEYWORDS: ")

#Setting Query Parameters for Search 
params = [('q',keyword)]

#Google Search URL
url = "https://google.co.in/search"

# Gets response from the server for the search query
response = requests.get(url=url, params=params)

# Response text from server is parsed using bs4
soup = bs4.BeautifulSoup(response.text,'lxml')

# Titles of results are found (Assumed that Google put h3 only on result titles)
titles = soup.find_all("h3")

#Result is Displayed

print("\nDISPLAYING FIRST PAGE RESULT TITLES FOR " + keyword + "\n")

x = 0; # counter variable
for title in titles: #loop to display titles
	x=x+1 # counter updated
	print( str(x) + ". " + title.get_text() )
