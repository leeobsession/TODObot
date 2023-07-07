import asyncio
from aiomysql import cursors
from conf.bd import conn


async def save_random(date, task, id_message):
    sql = "INSERT INTO tasks (Date_task, task, user_id) VALUES (%s,%s,%s)"
    val = (date, task, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


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
