from src.data.module_opslagplaats import module_DataBase
class module_service:
    def __init__(self):
        self.database = module_DataBase()
    def get_modules(self):
        modules = self.database.get_all_modules()
        return modules
    def verwijder_module(self, ID):
        self.database.verwijder_module(ID=ID)

    def get_ledstatus(self, ID):
        return self.database.get_ledstatus(ID)
    def voeg_module_toe(self,ID):
        ID = ID.strip()
        if not ID:
            raise ValueError("ID mag niet leeg zijn")
        self.database.voeg_module_toe(ID=ID)

    def get_module_id(self,atleet_ID):
       
        return self.database.get_module_id(atleet_id=atleet_ID)
    
    def postmodule(self,atleet_id, module_id):
        self.database.post_module_id(atleet_id=atleet_id,module_id=module_id)
    
    def update_ledstatus(self,ID , ledstatus):
         self.database.update_ledstatus(module_id=ID,led_status=ledstatus)