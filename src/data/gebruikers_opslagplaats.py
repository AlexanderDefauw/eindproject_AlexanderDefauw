import sqlite3
import os
class gebruikers_database:
    
    def __init__(self) -> None:
        self.DB_PATH = os.path.join(os.path.dirname(__file__), 'runninglabs.db')
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        self.maak_database()
    def maak_database(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
       
        
        
        c.execute('''
        CREATE TABLE IF NOT EXISTS gebruikers (
            atleet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            gebruikersnaam UNIQUE,
            voornaam STRING,
            achternaam STRING,
            geboortedatum TEXT
            
        )
        ''')
        

        
        
        
        
        conn.commit()
        conn.close()
        
       
      

   
    def get_atleet_id(self, gebruikersnaam):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT atleet_id FROM gebruikers WHERE gebruikersnaam = '{}'".format(gebruikersnaam))
        id = c.fetchall()
        return id
    
    def get_all_gebruikers(self):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM gebruikers")
        gebruikers = c.fetchall()
        return gebruikers
    
   

    def get_atleet_naam(self, atleet_id):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("SELECT gebruikersnaam FROM gebruikers WHERE atleet_id = {}".format(atleet_id))
        gebruikersnaam = c.fetchall()
        return gebruikersnaam
    
    def voeg_gebruiker_toe(self, gebruikersnaam, voornaam, achternaam, geboortedatum):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO gebruikers (gebruikersnaam, voornaam, achternaam, geboortedatum) VALUES ( ?, ?, ? , ?)",
        (gebruikersnaam, voornaam, achternaam, geboortedatum))
        conn.commit()
        conn.close()
    
    def verwijder_gebruiker(self, gebruikersnaam):
        conn = sqlite3.connect(self.DB_PATH)
        c = conn.cursor()
        c.execute("DELETE FROM gebruikers WHERE gebruikersnaam = '{}'".format(gebruikersnaam))
        conn.commit()
        conn.close()

    





    
    

