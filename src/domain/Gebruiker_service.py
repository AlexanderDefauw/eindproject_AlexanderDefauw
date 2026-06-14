
from data.gebruikers_opslagplaats import gebruikers_database
class gebruikerservice:

    def __init__(self):
        self.Data_base = gebruikers_database()
    
    def get_atleet_id(self, gebruikersnaam):
        try:
            atleet_id = self.Data_base.get_atleet_id(gebruikersnaam=gebruikersnaam)
            atleet_id = atleet_id[0][0]
        except:
            atleet_id = "ERROR"
        return atleet_id

    def get_gebruikers(self):
        gebruikers = self.Data_base.get_all_gebruikers()
        return gebruikers
    
    def get_gebruikersnaam(self,atleet_id):
        gebruikersnaam = self.Data_base.get_atleet_naam(atleet_id=atleet_id)
        
        return gebruikersnaam[0][0]
    
    def voeg_gebruiker_toe(self, gebruikersnaam, voornaam, achternaam, geboortedatum):
        if not gebruikersnaam or not voornaam or not achternaam or not geboortedatum:
            raise ValueError("Alle velden moeten ingevuld zijn")
        if voornaam.isalpha() == False:
            raise ValueError("voornaan mag alleen uit letters bestaan")
        if achternaam.isalpha() == False:
            raise ValueError("achternaam mag alleen uit letters bestaan")
        try:
            self.Data_base.voeg_gebruiker_toe(gebruikersnaam=gebruikersnaam,voornaam=voornaam,achternaam=achternaam,geboortedatum=geboortedatum)
        except:
            raise ValueError("er is een fout opgelopen bij het toevoegen van de gebruiker")
    def verwijder_gebruiker(self,gebruikersnaam):
        self.Data_base.verwijder_gebruiker(gebruikersnaam=gebruikersnaam)