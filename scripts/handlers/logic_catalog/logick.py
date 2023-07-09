from datetime import date, timedelta, datetime
import random

def form_date(us_date):
    d = us_date[0:2]
    m = us_date[3:5]
    y = us_date[6:]
    fulldat = f'{y}-{m}-{d}'
    new_date = date.fromisoformat(fulldat)
    return new_date

def convert_tuple(c_tuple): 
    str='' 
    for i in c_tuple: 
        str=str+i 
    return str 

def random_data(data):
    rand_num = random.randrange(0, 30)
    new_date = data.today() + timedelta(days=rand_num)
    return new_date
