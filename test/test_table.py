from mysql.connector import cursor
from conf.bd import conn


def random_task(id, task):
    db = conn()
    cur = db.cursor()
    sql = "INSERT INTO random_task (id, task) VALUES (%s,%s)"
    val = (id, task)
    result = cur.execute(sql, val)
    return db.commit()   
