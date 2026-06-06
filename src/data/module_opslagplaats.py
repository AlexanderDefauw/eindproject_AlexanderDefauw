import sqlite3
import os
class module_DataBase:
    
    def __init__(self) -> None:
        self.DB_PATH = os.path.join(os.path.dirname(__file__), 'runninglabs.db')
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        self.maak_database()
    def maak_database(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
       
        c.execute('''
        CREATE TABLE IF NOT EXISTS modules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Status INTEGER DEFAULT 0,
            atleet_id INTEGER DEFAULT 0
        
        )
        ''')
        
        conn.commit()
        conn.close()
        

    def verwijder_module(self,ID):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("DELETE FROM modules WHERE id = {}".format(ID))
        conn.commit()
        conn.close()

    def voeg_module_toe(self,ID):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO modules (id, status) VALUES  (?,?)",
            (ID, 4))
        except:
            raise ValueError("Module bestaat al of ongeldige module id")
        conn.commit()
        conn.close()

    def get_module_id(self, atleet_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        try:
            c.execute("SELECT id FROM modules WHERE atleet_id = {}".format(atleet_id))
            ID = c.fetchall()
        except:
            conn.commit()
            conn.close()
            raise ValueError("Atleet niet verbonden aan een module")
            
        conn.commit()
        conn.close()
        return ID
    
    
    def post_module_id(self, atleet_id, module_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        try:
            c.execute("UPDATE modules SET atleet_id = {} WHERE id= {}".format(atleet_id,module_id))
        except:
            conn.commit()
            conn.close()
            raise ValueError("ERROR")
        conn.commit()
        conn.close()

    def get_ledstatus(self, module_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT status FROM modules WHERE id={}".format(module_id))
        y = c.fetchall()
        conn.commit()
        conn.close()
        return y
    
    def update_ledstatus(self, module_id, led_status):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE modules SET status = {} WHERE id= {}".format(led_status,module_id))
        conn.commit()
        conn.close()

    def get_all_modules(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM modules") 
        x= c.fetchall()
        conn.commit()
        conn.close()
  
        return x