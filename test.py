from asyncio import sleep
import asyncio
import requests
from bs4 import BeautifulSoup
import datetime

import requests
from bs4 import BeautifulSoup

SPOTIFY_URL = "https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x"
KEY_WORDS = ["Album", "Donda"]


async def fetch(url) -> str:
    response = requests.get(url)
    return response.text


def check_for_album(soup) -> bool:
    for tag in soup.find_all("span"):
        if all(word in tag.text for word in KEY_WORDS):
            return True
    return False


def log_check(check) -> None:
    print(datetime.datetime.now().time(), end=": ")
    album_dropped = check()
    print("Album dropped!" if album_dropped else "No album dropped yet.")


async def main():
    while True:
        response = await fetch(SPOTIFY_URL)
        soup = BeautifulSoup(response, "html.parser")
        log_check(lambda: check_for_album(soup))
        await sleep(5)


asyncio.run(main())
