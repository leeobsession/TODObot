import asyncio
from aiomysql import cursors
from conf.bd import conn


async def get_random(id):
    sql = "SELECT task FROM random_task WHERE id = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id)
        result = await cursor.fetchall()
    cur.close()
    for elem in result:
        r = ''.join(elem)
    return r


async def get_sport(id):
    sql = "SELECT task FROM task_sport WHERE id = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id)
        result = await cursor.fetchall()
    cur.close()
    for elem in result:
        r = ''.join(elem)
    return r


async def get_home(id):
    sql = "SELECT task FROM task_home WHERE id = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id)
        result = await cursor.fetchall()
    cur.close()
    for elem in result:
        r = ''.join(elem)
    return r


async def get_hobby(id):
    sql = "SELECT task FROM task_hobby WHERE id = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id)
        result = await cursor.fetchall()
    cur.close()
    for elem in result:
        r = ''.join(elem)
    return r
