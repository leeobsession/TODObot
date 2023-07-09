import asyncio
from aiomysql import cursors
from conf.bd import conn


async def yes_delit(task, id_message):
    sql = "DELETE FROM tasks WHERE task = (%s) AND user_id = (%s) "
    val = (task, id_message)
    cur = await conn()
    async with cur.cursor() as cursor:
        await cursor.execute(sql, val)
        await cur.commit()
    cur.close()