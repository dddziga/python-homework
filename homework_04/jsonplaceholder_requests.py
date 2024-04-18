"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession
from loguru import logger

USERS_DATA_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_posts() -> list:
    logger.info(f"Fetch posts from {POSTS_DATA_URL}")

    async with ClientSession() as session:
        result = await fetch_json(session, POSTS_DATA_URL)

    logger.info("Fetched json from {!r}: {}", POSTS_DATA_URL, result)

    return result


async def fetch_users() -> list:
    logger.info(f"Fetch users from {USERS_DATA_URL}")

    async with ClientSession() as session:
        result = await fetch_json(session, USERS_DATA_URL)

    logger.info("Fetched json from {!r}: {}", USERS_DATA_URL, result)

    return result



