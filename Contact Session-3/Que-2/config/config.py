import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="username",
    password="Abcd1234"
)

my_cursor = conn.cursor()

class DB_REQUEST:   
    def Insert(arg):
        sql = f"INSERT INTO TODO_LIST(ID,LIST) VALUE ('{arg}')"
        my_cursor.execute(sql)
        conn.commit()
        
    def Delete(arg):
        sql = f"DELETE FROM TODO_LIST WHERE ID = '{arg}'"
        my_cursor.execute(sql)
        conn.commit
        
    def LoadList():
        sql = "SELECT * FROM TODO_LIST"
        res = my_cursor.execute(sql)
        return res