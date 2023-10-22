import requests
from bs4 import BeautifulSoup
from amazoncaptcha import AmazonCaptcha

product_url = "https://www.amazon.com/dp/B078JLKCG4?ref_=cm_sw_r_cp_ud_dp_ZJENTZCKVF7F3B0RK50C"
request_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": "_ga_VL41109FEB=GS1.2.1697883261.1.0.1697883261.0.0.0; _ga=GA1.2.1547385837.1697883260; _gid=GA1.2.1276959317.1697883260; PHPSESSID=2c0de8a3934cf44d1081c1ebe13d1ea3",
    "X-Forwarded-For": "211.229.11.55",
    "referer": "https://www.google.com/",
}

response = requests.get(url=product_url, headers=request_header)
soup = BeautifulSoup(response.content, "html.parser")

# captcha_img = str(soup.select("div div div img")).split("\"")[1]
# captcha = AmazonCaptcha.fromlink(captcha_img)
# solution = captcha.solve()
#
# response = requests.get(url=product_url, headers=request_header)
# soup = BeautifulSoup(response.content, "html.parser")

print(soup)
