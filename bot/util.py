import aiohttp

from config import MEME_API_KEY


async def get_meme_url():
    url = "https://api.apileague.com/retrieve-random-meme?keywords=rocket"

    headers = {
        'x-api-key': MEME_API_KEY
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('url')
            else:
                return f"Error: {response.status}"
