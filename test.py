import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

async def field_info(field_link):              # async - to make outer function coroutine
    text = await get_text(field_link)          # await - to get result from async funcion
    soup = BeautifulSoup(text, 'lxml')
    anchor = soup.findAll("a")
    content = anchor.string
    print(text)

async def main():
    links = ["https://www.mediamatters.org/", "https://www.politico.com/tipsheets/morning-money", "https://www.bloomberg.com/markets/economics"]

    scraped_info = asyncio.gather(*[
        field_info(link)
        for link
        in links
    ])  # do multiple field_info coroutines concurrently (parallely)

asyncio.run(main())
