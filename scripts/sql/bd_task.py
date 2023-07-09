import asyncio
from aiomysql import cursors
from conf.bd import conn


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

