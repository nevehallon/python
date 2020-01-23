import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://www.whitehouse.gov/briefings-statements/")
        soup = BeautifulSoup(html, 'lxml')
        for post_text in soup.findAll("h2", {'class': 'briefing-statement__title'}):
            a_tag = post_text.find('a')
            content = a_tag.string
            print(content)

if __name__ == '__main__':
    asyncio.run(main())
