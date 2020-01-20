import requests
from bs4 import BeautifulSoup
import asyncio

async def trade_spider1(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.whitehouse.gov/briefings-statements/page/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll("h2", {'class': 'briefing-statement__title'}):
            await asyncio.sleep(0)
            a_tag = link.find('a')
            await asyncio.sleep(0)
            content = a_tag.string
            print(content + str(page))
        page += 2
    await asyncio.sleep(0)

async def trade_spider2(max_pages):
    page = 2
    while page <= max_pages:
        url = "https://www.whitehouse.gov/briefings-statements/page/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll("h2", {'class': 'briefing-statement__title'}):
            await asyncio.sleep(0)
            a_tag = link.find('a')
            await asyncio.sleep(0)
            content = a_tag.string
            print(content + str(page))
        page += 2
    await asyncio.sleep(0)

async def main(max_pages):
    task1 = asyncio.create_task(trade_spider1(max_pages))
    task2 = asyncio.create_task(trade_spider2(max_pages))

    await asyncio.gather(task1, task2)

asyncio.run(main(7))