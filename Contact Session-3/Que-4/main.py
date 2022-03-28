import os
import re
import psycopg2

os.chdir(os.getcwd() + "\Que-4") # Que-4 = name of folder

with open(r"baby2008 (1).html","r") as baby_file:       
    read_baby_file = baby_file.read()
    # if search for <td></td>
    res = re.findall(r'<td>[A-Z]?[a-z]+</td>',read_baby_file)

baby_names = []
for i in res:
    baby_names.append(i[4: len(i) - 5]) # removes the tags ie <td>&</td> then appends to baby_names

## print individual names
# for i in baby_names:
#     print(i)

### inserting to a table
# make connection to the db
con = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="username",
    password="Abcd1234"
)

con_cursor = con.cursor()
for names in baby_names:
    # before execution a table Que_4 with column baby_names must have been created in a db
    con_cursor.execute("INSERT INTO Que_4('baby_names') VALUES (f'{names}')")

con_cursor.close()
con.close()

