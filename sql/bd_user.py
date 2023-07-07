import asyncio
from aiomysql import cursors
from conf.bd import conn


async def save_user(id_message, name):
    sql = "INSERT INTO users (id_messag, user) VALUES (%s,%s)"
    val = (id_message, name)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


async def check_user():
    sql = "SELECT id_messag FROM users"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql)
        result = await cursor.fetchall()
    cur.close()
    lst = []
    for x in result:
        for y in x:
            lst.append(y)
    return lst


async def get_name(id_message):
    sql = "SELECT user FROM users WHERE id_messag = (%s) "
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id_message)
        result = await cursor.fetchall()
    cur.close()
    for elem in result:
        r = ''.join(elem)
    return r
