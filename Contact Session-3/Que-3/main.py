import psycopg2
from dataclasses import dataclass

# setting the connection
con = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="username",
    password="Abcd1234"
)

cursor = con.cursor()

@dataclass
class crud_operatons:
    # def __init__(arg):
    #     pass
    
    @staticmethod
    def create() -> str:
        sql = """CREATE TABLE contact_session3 (id INT SERIAL PRIMARY KEY,que_1 VARCHAR(200) NOT NULL, 
                 que_2 VARCHAR(100) NOT NULL, que_3 VARCHAR(100) NOT NULL)"""
        cursor.execute(sql)
        cursor.close()
        con.close()
        return "success"
    
    @staticmethod
    def read() -> dict:
        sql = "SELECT * FROM contact_sesson3"
        res = cursor.fetchall(sql)
        return res
    
    @staticmethod
    def update():
        sql = """ UPDATE contact_session3 
                  SET que-2 = 'something'
                  WHERE id = 'someid' 
                                        """
        cursor.execute(sql)
        cursor.close()
        con.close()
    
    @staticmethod
    def delete():
        sql = " DROP TABLE contact_session3"
        cursor.execute(sql)
        cursor.close()
        con.close()

crud_operatons.create()