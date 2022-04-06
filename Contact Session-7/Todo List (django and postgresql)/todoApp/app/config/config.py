from ast import Str
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="username",
    password="Abcd1234"
)

my_cursor = conn.cursor()

class DB_REQUEST:   
    def addList(self, todoname, arg:str) -> None:
        sql = f"INSERT INTO TODO_LIST(TODO_ID, LIST) VALUE ('{todoname}','{arg}')"
        my_cursor.execute(sql)
        conn.commit() 
        conn.close()
        
    def deleteList(arg):
        sql = f"DELETE FROM TODO_LIST WHERE ID = '{arg}'"
        my_cursor.execute(sql)
        conn.commit()
        conn.close()
        
    def loadList(self, todoname):
        sql = f"SELECT * FROM TODO_LIST WHERE TODO_ID = '{todoname}'"
        res = my_cursor.execute(sql)
        return res
    
    def addTodo(self, todo):
        sql = f"INSERT INTO TODO(TODO) VALUE ('{todo}')"
        my_cursor.execute(sql)
        conn.commit() # commit request
        conn.close() # close db
    
    def deleteTodo(self, arg):
        sql = f"DELETE FROM TODO WHERE TODO = '{arg}'"
        my_cursor.execute(sql)
        conn.commit()
        my_cursor.close()
        conn.close()
        
    def loadTodo():
        sql = "SELECT * FROM TODO"
        res = my_cursor.execute(sql)
        return res
        