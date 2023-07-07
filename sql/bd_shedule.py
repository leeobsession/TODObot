import asyncio
from aiomysql import cursors
from conf.bd import conn


async def shed_user():
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

async def check_shedul(date, id_message):
    sql = "SELECT task FROM tasks WHERE user_id = (%s)"
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, id_message)
        result = await cursor.fetchall()
    cur.close()
    for date in result:
        if date in result:
            return True
        else:
            return False

async def show_shedul_task(date, id_message):
    sql = "SELECT task FROM tasks WHERE Date_task = (%s) AND user_id = (%s) "
    val = (date, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        result = await cursor.fetchall()
    cur.close()
    former = '\n\n'.join('      '.join(map(str, l)) for l in result)
    return former
    
