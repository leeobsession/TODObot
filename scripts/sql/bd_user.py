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


async def update_user(id_message, name):
    sql = """UPDATE users 
    SET user = (%s)
    WHERE id_messag = (%s)"""
    val = (id_message, name)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


async def get_id(id_message):
    sql = "SELECT id_messag FROM users WHERE id_messag = (%s) "
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id_message)
        result = await cursor.fetchall()
    cur.close()
    for elem in result:
        for b in elem:
            return b


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


async def save_date(date, id_message):
    sql = "INSERT INTO tasks (Date_task, user_id) VALUES (%s,%s)"
    val = (date, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


async def save_task(task, id_message, date):
    sql = """UPDATE tasks 
    SET task = (%s)
    WHERE user_id = (%s) AND Date_task = (%s)"""
    val = (task, id_message, date)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


async def save_random(task, date, id_message):
    sql = "INSERT INTO tasks (task, Date_task, user_id) VALUES (%s,%s,%s)"
    val = (task, date, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


async def yes_delit(task, id_message):
    sql = "DELETE FROM tasks WHERE task = (%s) AND user_id = (%s) "
    val = (task, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()