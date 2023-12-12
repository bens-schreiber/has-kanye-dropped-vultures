from asyncio import sleep
import asyncio
import requests
from bs4 import BeautifulSoup
import datetime

import requests
from bs4 import BeautifulSoup

import os

SPOTIFY_URL = "https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x"
KEY_WORDS = ["Album", "Vultures"]

DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")


def post_to_discord():
    payload = {"content": "Kanye dropped Vultures! @everyone"}
    requests.post(DISCORD_WEBHOOK, data=payload)


async def fetch(url) -> str:
    response = requests.get(url)
    return response.text


def check_for_album(soup) -> bool:
    for tag in soup.find_all("span"):
        if all(word in tag.text for word in KEY_WORDS):
            return True
    return False


def log_result(album_dropped) -> None:
    print(datetime.datetime.now().time(), end=": ")
    print(
        "VULTURES DROPPED!!!!!" if album_dropped else "Kanye has not dropped Vultures."
    )


async def main():
    while True:
        response = await fetch(SPOTIFY_URL)
        soup = BeautifulSoup(response, "html.parser")
        album_dropped = check_for_album(soup)
        log_result(album_dropped)
        if album_dropped:
            post_to_discord()
        await sleep(5)


asyncio.run(main())
