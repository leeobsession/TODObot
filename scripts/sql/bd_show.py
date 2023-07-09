import asyncio
from aiomysql import cursors
from conf.bd import conn


async def check_task(date, id_message):
    sql = "SELECT Date_task, task FROM tasks WHERE Date_task = (%s) AND user_id = (%s) "
    val = (date, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        result = await cursor.fetchall()
    cur.close()
    former = '\n\n'.join('      '.join(map(str, l)) for l in result)
    return former

async def check_all_task(id_message):
    sql = "SELECT Date_task, task FROM tasks WHERE user_id = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id_message)
        result = await cursor.fetchall()
    cur.close()
    former = '\n\n'.join('      '.join(map(str, l)) for l in result)
    return former

async def key_day_task(date, id_message):
    sql = "SELECT task FROM tasks WHERE Date_task = (%s) AND user_id = (%s) "
    val = (date, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        result = await cursor.fetchall()
    cur.close()
    lst = []
    for x in result:
        for y in x:
            lst.append(y)
    return lst

async def key_all_task(id_message):
    sql = "SELECT task FROM tasks WHERE user_id = (%s) "
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id_message)
        result = await cursor.fetchall()
    cur.close()
    lst = []
    for x in result:
        for y in x:
            lst.append(y)
    return lst