import asyncio
import httpx
import logging 

logger = logging.getLogger(__name__ )


class Requester():
    def __init__(self):
        self.data = {
            "file_id": "AgACAgIAAxkBAAMzauiy9ScZaMMAAWeb4VByilzquf5BAAJlIWsbolNBS4zZp7bu5BEkAQADAgADeQADPQQ",
            "file_unique_id": "AQADZSFrG6JTQUt-",
            "width": 960,
            "height": 1280,
            "file_size": 88595,
        }
        
        self.url = "http://127.0.0.1:8000/api/v1/new_photo"

    async def postToBackEnd(self) -> None:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=self.url,
                json=self.data
                )
            print(response)

            logger.info(f"Код ответа от {self.url}: {response.status_code}\n{response.json()}")

async def main():
    req = Requester()
    await req.postToBackEnd()
    
if __name__ == "__main__":
    asyncio.run(main())