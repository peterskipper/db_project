import sqlite3 as lite
import pandas as pd

cities = (('Los Angeles', 'CA'), 
    ('San Francisco', 'CA'),
    ('Seattle', 'WA'),
    ('Houston', 'TX'),
    ('Dallas', 'TX'),
    ('Boston', 'MA'))

weather = (('Los Angeles', 'June'),
    ('San Francisco', 'July'),
    ('Seattle', 'July'),
    ('Houston', 'August'),
    ('Dallas', 'July'),
    ('Boston', 'August'))

con = lite.connect('starter_db.db')

with con:
    cur = con.cursor()
    cur.execute("drop table if exists cities")
    cur.execute("drop table if exists weather")
    cur.execute("create table cities (name text, state text)")
    cur.execute("create table weather (city text, wmonth text)")
    cur.executemany("insert into cities values(?,?)", cities)
    cur.executemany("insert into weather values(?,?)", weather)
    cur.execute("select city, state, wmonth from cities inner join weather on name = city")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

resp = 'blah'
while resp.lower() not in ['june', 'july', 'august']:
    resp = raw_input("Which warmest month would you like data on? "
        "\nChoose June, July or August ")

selection = df[df["wmonth"] == resp.capitalize()]

answer =[]
for _ , row in selection.iterrows():
    answer.append(row.tolist())

#import pdb
#pdb.set_trace()
print "The cities that are warmest in {} are: ".format(resp.capitalize())
for ans in answer:
    print ", ".join(ans[:-1])
