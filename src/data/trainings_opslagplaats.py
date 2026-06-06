import sqlite3
import os
class training_DataBase:
    
    def __init__(self) -> None:
        self.DB_PATH = os.path.join(os.path.dirname(__file__), 'runninglabs.db')
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        self.maak_database()
    def maak_database(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
       
        
        c.execute('''
        CREATE TABLE IF NOT EXISTS trainingen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum TEXT DEFAULT 0,
            filepath TEXT UNIQUE,
            atleet_id INTEGER,
            trainings_nummer INTEGER
        )
        ''')
       
      
        
    

        
        
        
        
        conn.commit()
        conn.close()
        

       
      
       
    def get_all(self):
       
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM trainingen") 
        x= c.fetchall()
        conn.commit()
        conn.close()
  
        return x
   

    def insert_training(self, trainings_id, atleet_id,datum):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
    
        filepath = f"{atleet_id}_{trainings_id}"
        c.execute("INSERT OR IGNORE INTO trainingen (datum, filepath, atleet_id, trainings_nummer) VALUES (?, ?, ?, ?)",
        (datum, filepath, atleet_id, trainings_id))
        conn.commit()
        conn.close()
        
        
    def get_training(self, trainings_id, atleet_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        filepath = f"{atleet_id}_{trainings_id}"
        c.execute("SELECT * FROM trainingen WHERE filepath='{}'".format(filepath))
        y = c.fetchall()
        conn.commit()
        conn.close()
       
        return y
    def get_last_trainings_id(self,atleet_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        
        c.execute("SELECT trainings_nummer FROM trainingen WHERE atleet_id={} ORDER BY id DESC LIMIT 1".format(atleet_id))
        y = c.fetchall()
        conn.commit()
        conn.close()
        return y
    
    def verwijder_training(self, atleet_id, trainings_id):
        
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        filepath = f"{atleet_id}_{trainings_id}"
        

      
        c.execute("DELETE FROM trainingen WHERE atleet_id = {} AND trainings_nummer = {}".format(atleet_id,trainings_id))
        conn.commit()
        conn.close()
        
 
    def get_atleet_training(self, atleet_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM trainingen WHERE atleet_id = {}".format(atleet_id))
        trainingen = c.fetchall()
        return trainingen

