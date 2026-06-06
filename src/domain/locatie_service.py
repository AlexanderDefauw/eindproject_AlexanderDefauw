

from src.data.locatiegegevens_opslagplaats import locatiegegevens_database
class locatieservice:

    def __init__(self):
        self.database = locatiegegevens_database()
    
    def locatie_toevoegen(self, laltidude, longitude, snelheid , atleet_id,afstand , trainings_nummer , time):
       
        self.database.locatie_toevoegen(atleet_id=atleet_id,trainings_id=trainings_nummer,laltidude=laltidude,longitude=longitude,snelheid=snelheid,afstand=afstand,tijd=time)
    
    def get_all(self):
        return None
    def get_training(self, atleet_id , trainings_id):
        x= self.database.get_training(atleet_id=atleet_id,trainings_id=trainings_id)
        return x
    
    def verwijder_meetpunten(self, atleet_id, trainings_id):
        self.database.verwijder_meetpunten(atleet_id=atleet_id,trainings_id=trainings_id)

    def laatste_data(self, atleet_id, trainings_id):
        data= self.database.get_training(atleet_id=atleet_id,trainings_id=trainings_id)
        laatste_data = data[-1]
        begintijd = data[0][7]
        return laatste_data,begintijd
    
    def verstrekentijd(self, atleet_id, trainings_id):
        training = self.get_training(atleet_id=atleet_id, trainings_id=trainings_id)
        verstrekentijd = (training[-1][-1] - training[0][-1])/60
        return verstrekentijd
    
    
        