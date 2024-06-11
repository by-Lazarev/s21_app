# crawl.py

import httpx
import asyncio
import sys
import json

BASE_URL = "http://localhost:8888/api/v1/tasks/"

async def send_urls(urls):
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json={"urls": urls})
        response.raise_for_status()
        data = response.json()
        return data["id"]

async def fetch_task_status(task_id):
    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(f"{BASE_URL}{task_id}")
            response.raise_for_status()
            data = response.json()
            if data["status"] == "ready":
                return data
            await asyncio.sleep(1)

async def main(urls):
    try:
        task_id = await send_urls(urls)
        print(f"\nTask ID: {task_id}")

        result = await fetch_task_status(task_id)
        print("Task completed.")
        for item in result["result"]:
            print(f"{item['status_code']}\t{item['url']}")
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred: {exc}")
    except httpx.RequestError as exc:
        print(f"Request error occurred: {exc}")
    except json.JSONDecodeError:
        print("Failed to decode response as JSON.")
        print(f"Response text: {exc.response.text}")

if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Usage: python crawl.py <URL1> <URL2> ...")
        sys.exit(1)

    asyncio.run(main(urls))

