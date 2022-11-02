import aiohttp
from .config import url, user, password


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, auth=aiohttp.BasicAuth(user, password)) as response:
            return await response.json()
