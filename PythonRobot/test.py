
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.gamersky.com/"

print("第一种方法")
response1 = urllib.request.urlopen(url)

html = response1.read()

soup = BeautifulSoup(
    html,
    'html.parser',
    from_encoding='utf-8'
)

lists = soup.find_all('a')

for link in lists:
    print(link.name,link['href'],link.get_text())
    


























