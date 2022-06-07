import requests
from bs4 import BeautifulSoup

url1 = "https://www.uuu.com.tw/"
response = requests.get(url1)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.title.text)
videos = soup.find('section', {'id': "Video"})
videoLinks = videos.find_all('a')

for v in videoLinks:
    print(v)
