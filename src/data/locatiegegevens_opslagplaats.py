import sqlite3
import os

class locatiegegevens_database:
    def __init__(self) -> None:
        self.DB_PATH = os.path.join(os.path.dirname(__file__), 'runninglabs.db')
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        self.maak_database()
    def maak_database(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
     
        c.execute('''
        CREATE TABLE IF NOT EXISTS meetpunten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            atleet_id INTEGER,
            trainings_nummer INTEGER,
            laltidude FLOAT,
            longitude FLOAT,
            snelheid FLOAT,
            afstand FLOAT,
            time INTEGER
                  
        )
        ''')
        conn.commit()
        conn.close()

    def locatie_toevoegen(self, atleet_id, trainings_id,laltidude, longitude, snelheid, afstand, tijd ):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO meetpunten (atleet_id, trainings_nummer, laltidude, longitude, snelheid,afstand,time ) VALUES (?, ?, ?, ?,?,?,?)",
        (atleet_id, trainings_id,laltidude,longitude,snelheid,afstand,tijd))
        conn.commit()
        conn.close()
    def verwijder_meetpunten(self,atleet_id,trainings_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("DELETE FROM meetpunten WHERE atleet_id = {} AND trainings_nummer = {}".format(atleet_id,trainings_id))
        conn.commit()
        conn.close()

    def get_training(self, atleet_id, trainings_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM meetpunten WHERE atleet_id = {} AND trainings_nummer = {}".format(atleet_id,trainings_id))
        y = c.fetchall()
        conn.commit()
        conn.close()
        return y
    
