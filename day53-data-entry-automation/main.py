import requests
from bs4 import BeautifulSoup

form = "https://forms.gle/WosYG7M1nX7sXtF2A"
zillow = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
request_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": "_ga_VL41109FEB=GS1.2.1697883261.1.0.1697883261.0.0.0; _ga=GA1.2.1547385837.1697883260; _gid=GA1.2.1276959317.1697883260; PHPSESSID=2c0de8a3934cf44d1081c1ebe13d1ea3",
    "X-Forwarded-For": "211.229.11.55",
    "referer": "https://www.google.com/",
}

# Get a webpage
webpage = requests.get(url=zillow, headers=request_header).text
soup = BeautifulSoup(webpage, "html.parser")

# Find links
links = soup.find_all(name="a", class_="property-card-link")
raw_links = [link["href"] for link in links]
links_1 = [f"https://www.zillow.com{link}" for link in raw_links if "zillow" not in link]
links_2 = [link for link in raw_links if "zillow" in link]
link_list = []
link_list = [link_list.append(link) for link in links_1 + links_2 if link not in link_list]

# Find prices
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
price_list = [price.text.replace("+", "/").split("/")[0] for price in prices]

# Find addresses
addresses = soup.find_all(name="address")
