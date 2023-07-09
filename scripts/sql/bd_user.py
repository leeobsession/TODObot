import asyncio
from aiomysql import cursors
from conf.bd import conn


async def save_user(id_message, name):
    sql = """UPDATE users 
    SET user = (%s)
    WHERE id_messag = (%s)"""
    val = (id_message, name)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()


async def check_user(id_message):
    sql = "SELECT id_messag FROM users WHERE id_messag = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id_message)
        result = await cursor.fetchall()
        for id_message in result:
            if id_message in result:
                return True
            else:
                return False

    


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
