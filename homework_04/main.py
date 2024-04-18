"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
import jsonplaceholder_requests
from models import Post, User, engine, Session
from models.base import Base


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(users_data: list[User], db_session: AsyncSession) -> list[User]:
    users = [
        User(item["name"], item["username"], item["email"])
        for item in users_data
    ]
    async with db_session.begin():
        db_session.add_all(users)
    return users


async def create_posts(posts_data: list[Post], db_session: AsyncSession) -> list[Post]:
    posts = [
        Post(item["userId"], item["title"], item["body"])
        for item in posts_data
    ]
    async with db_session.begin():
        db_session.add_all(posts)
    return posts


async def async_main():
    # Создание таблицы
    await create_table()
    users_data, posts_data = await asyncio.gather(
        jsonplaceholder_requests.fetch_users(),
        jsonplaceholder_requests.fetch_posts(),
    )
    await create_users(users_data, Session())
    await create_posts(posts_data, Session())


if __name__ == '__main__':
    print(engine)
    asyncio.run(async_main())

