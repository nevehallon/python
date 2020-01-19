import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com")

#print(result.status_code)

#print(result.headers)

src = result.content

soup = BeautifulSoup(src, 'lxml')

#print(soup.encode("utf-8"))

links = soup.find_all("a")
#print(links)
#print("\n")

for link in links:
    if "Gmail" in link.text:
        print(link)
        print(link.attrs['href'])
