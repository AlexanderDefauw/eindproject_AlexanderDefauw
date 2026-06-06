
from src.data.trainings_opslagplaats import training_DataBase
from src.domain.locatie_service import locatieservice
from src.domain.module_service import module_service
import datetime
class trainingservice:

    def __init__(self):
        self.database = training_DataBase()
        self.locatie_service = locatieservice()
        self.module_service =  module_service()
    def get_all(self,):
        data = self.database.get_all()
        return data
    def bestaat_training(self, atleet_id, trainings_id):
        training =self.database.get_training(atleet_id=atleet_id,trainings_id=trainings_id)
        if training ==  []:
            return False
        else:
            return True
    
    def maak_training_aan(self, atleet_id, trainings_id,datum):
        self.database.insert_training(atleet_id=atleet_id, trainings_id=trainings_id,datum=datum)
        
    def get_last_trainings_id(self, atleet_id):
        try:
            nummer = self.database.get_last_trainings_id(atleet_id=atleet_id)
            nummer = nummer[0][0]
        except:
            nummer = 0
        return nummer

    def verwijder_training(self, trainings_id, atleet_id):
       
        self.locatie_service.verwijder_meetpunten(atleet_id=atleet_id, trainings_id=trainings_id)

        y = self.database.verwijder_training(atleet_id=atleet_id, trainings_id=trainings_id)
   
        #self.database.verwijder_training(atleet_id=atleet_id,trainings_id=trainings_id)

    def meetpunten_toevoegen(self, laltidude, longitude, snelheid , atleet_id, api_key,afstand , trainings_nummer , time):
        
        if api_key == "tPmAT5Ab3j7F9":
            try:
                self.check_geldigheid(laltidude=laltidude, longitude=longitude,snelheid=snelheid,atleet_id=atleet_id, afstand=afstand,trainings_nummer=trainings_nummer,time= time)
            except:
                
                raise ValueError("ERROR")
            if self.bestaat_training(atleet_id=atleet_id, trainings_id=trainings_nummer) == True:
                self.locatie_service.locatie_toevoegen(laltidude=laltidude, longitude=longitude, snelheid=snelheid , atleet_id=atleet_id,afstand=afstand , trainings_nummer=trainings_nummer , time=time)
               
            else:
                x = datetime.datetime.now()
                datum = x.strftime("%x")
                self.maak_training_aan(atleet_id=atleet_id,trainings_id=trainings_nummer,datum=datum)
                self.locatie_service.locatie_toevoegen(laltidude=laltidude, longitude=longitude, snelheid=snelheid , atleet_id=atleet_id, afstand=afstand , trainings_nummer=trainings_nummer , time=time)
          
            
        else:
            raise ValueError("ERROR")
       
    def get_modules(self):
        modules = self.module_service.get_modules()
        return modules
    
    def ledstatus(self, module_id):
        modules = self.module_service.get_ledstatus(module_id)
        return modules[0]

    def update_ledstatus(self, module_id, led_status):
        self.module_service.update_ledstatus(ID=module_id, ledstatus=led_status)

    def get_data(self, atleet_id):
        trainings_id = self.database.get_last_trainings_id(atleet_id=atleet_id)
        trainings_id = trainings_id[0][0]
        laatste_data,begintijd = self.locatie_service.laatste_data(atleet_id=atleet_id, trainings_id=trainings_id)
        return laatste_data,begintijd
    
    def get_traingen_user(self, atleet_id):
        trainingen = self.database.get_atleet_training(atleet_id=atleet_id)
        return trainingen
    
    def check_geldigheid(self,laltidude, longitude, snelheid , atleet_id,afstand , trainings_nummer , time):
        
           
            laltidude = laltidude.strip()
            longitude = longitude.strip()
            snelheid = snelheid.strip()
            atleet_id = atleet_id.strip()
            afstand = afstand.strip()
            trainings_nummer = trainings_nummer.strip()
            time = time.strip()
            if  not laltidude or not longitude  or not snelheid  or not atleet_id or not afstand  or not trainings_nummer  or not time:
                raise ValueError("ERROR")
            try: 
                laltidude=float(laltidude)
                longitude=float(longitude)
                snelheid=float(snelheid)
                atleet_id=int(atleet_id)
                afstand=float(afstand)
                trainings_nummer=float(trainings_nummer)
                time=str(time)
            
            except:

                raise ValueError("ERROR")