import aiohttp
import asyncio
import sqlite3

# Ma'lumotlar bazasini yaratish va ulanish
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Jadval yaratish (agar u mavjud bo'lmasa)
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                birthday TEXT NOT NULL,
                phone TEXT NOT NULL)"""
               )
conn.commit()


def save_user(user):
    cursor.execute("""INSERT OR REPLACE INTO users (id, firstName, lastName, birthday, phone)
    VALUES (?, ?, ?, ?, ?)""", (user['id'], user['firstName'], user['lastName'], user['birthDate'], user['email']))
    conn.commit()


async def req_users():
    url = 'https://dummyjson.com/users'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            users = data['users']
            for user in users:
                save_user(user)


async def main():
    await req_users()


asyncio.run(main())

conn.close()
