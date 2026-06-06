'''
imports doen
'''
from flask import Flask, render_template, request, redirect, url_for, flash
from src.domain.locatie_service import locatieservice
from archief.locatiegegevens_repository import locatiegegevens_repository
from src.domain.trainings_service import trainingservice
from src.domain.Gebruiker_service import gebruikerservice
from src.domain.module_service import module_service
import os
import datetime
def create_app():
    app = Flask(__name__,
                template_folder="templates",
                static_folder="static")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY","dev-sleutel")
    locatie_service = locatieservice()
    Trainings_service = trainingservice()
    gebruiker_service = gebruikerservice()
    moduleservice = module_service()
    x = datetime.datetime.now()
    @app.route("/")
    def root():
        return redirect(url_for("dashboard"))

    @app.route("/user/gebruiker" , methods=["POST"])
    def gebruiker():
        '''
        Wanneer de gebruiker naar /user/gebruiker gaat zullen de trainingen van een bepaalde gebruiker getoond worden.
        '''
        atleet_id = request.form.get("atleet_id")
        naam = request.form.get("naam")
        atleet_id = gebruiker_service.get_atleet_id(gebruikersnaam=naam)
        trainingen = Trainings_service.get_traingen_user(atleet_id=atleet_id)
    
        return render_template("user/gebruiker.html", trainingen = trainingen, naam=naam)

    @app.route("/admin/trainingen")
    def trainingen():
        '''
        wanneer een admin naar het tablat trainingen gaat zullen alle trainingen getoond die ze eventueel kunnen verwijderen.
        '''
        
        data = Trainings_service.get_all()
        return render_template("admin/alltrainingen.html" , data = data)
    @app.route("/admin/modules")
    def modules():
       
        modules = moduleservice.get_modules()
        
        return render_template("admin/all_modules.html" , modules = modules)
    @app.route("/user/bekijk_training" , methods=["POST"])
    def bekijk_training():
        atleet_id = request.form.get("atleet_id")
        trainings_id = request.form.get("trainings_id")
        gebruikersnaam = request.form.get("naam")
        
        gebruikersnaam = gebruiker_service.get_gebruikersnaam(atleet_id=atleet_id)
        data = locatie_service.get_training(atleet_id=atleet_id,trainings_id=trainings_id)
        teller = 0
        gemiddeldesnelheid = 0
        verstreken_tijd = locatie_service.verstrekentijd(atleet_id=atleet_id,trainings_id=trainings_id)
        data_x = []
        data_y = []
        for d in data:
   
            gemiddeldesnelheid+= float(d[5])
           
            data_x.append(float(d[6]))
            data_y.append(float(d[5]))
            teller+=1
        gemiddeldesnelheid = gemiddeldesnelheid/teller
        round(gemiddeldesnelheid, 2)


        return render_template("/user/bekijk_training.html" , data = data ,gebruikersnaam= gebruikersnaam,gemiddeldesnelheid=round(gemiddeldesnelheid, 2) , data_x = data_x, data_y = data_y, verstreken_tijd = round(verstreken_tijd, 2))
    
    @app.route("/user/dashboard")
    def dashboard():
        gebruikers = gebruiker_service.get_gebruikers()
        
        return render_template("/user/index.html" , gebruikers = gebruikers)
        
    @app.route("/admin/locatie/toevoegen" , methods=["POST"])
    def locatie_toevoegen():
        
        api_key:str = request.form.get("api_key","0")
        laltidude:str = request.form.get("lann","0")
        longitude:str = request.form.get("longal","0")
        snelheid:str = request.form.get("snelheid","0")
        atleet_id:str = request.form.get("atleet_id","")
        
        afstand:str = request.form.get("afstand","0")
        Loopmodule = request.form.get("loopmodule","0")
        trainings_nummer:str = request.form.get("trainings_nummer","")
        time:str = request.form.get("time","0")
        
        
        try:
            Trainings_service.meetpunten_toevoegen(laltidude = laltidude, longitude=longitude, snelheid=snelheid , atleet_id= atleet_id, api_key = api_key,afstand = afstand, trainings_nummer = trainings_nummer, time= time)
            moduleservice.postmodule(atleet_id=atleet_id,module_id=Loopmodule)
        except ValueError as e:
           
            if str(e) != "ERROR":
                flash("SUCCES", "success")
            else:
                flash(str(e), "error")
        return redirect(url_for("dashboard"))
    @app.route("/admin/locatie/traings_id" , methods=["POST"])
    def trainings_id():
        gebruikersnaam = request.form.get("naam")
        id = gebruiker_service.get_atleet_id(gebruikersnaam=gebruikersnaam)
        if id == "ERROR":
            return render_template("/admin/getter.html" , data = ["ERROR"])
        else:
            trainings_id = Trainings_service.get_last_trainings_id(atleet_id=id)
            data = [id ,',', trainings_id]
            
            return render_template("/admin/getter.html" , data = data)
        

    @app.route("/admin/verwijder_training" , methods=["POST"])
    def verwijder_training():
        atleet_id = request.form.get("atleet_id")
        trainings_id = request.form.get("trainings_id")
        Trainings_service.verwijder_training(atleet_id=atleet_id, trainings_id=trainings_id)
        flash("success", "success")
        return redirect(url_for("trainingen"))

    @app.route("/admin/ledstatus" , methods=["POST"])
    def ledstatus():
        try:
            module_id = request.form.get("module_id")
            data = Trainings_service.ledstatus(module_id=module_id)
            return render_template("/admin/getter.html" , data = data)
        except:
            return render_template("/admin/getter.html" , data = "0")
    
    @app.route("/admin/ledstatus/update" , methods=["POST"])
    def update_ledstatus():
        module_id = request.form.get("module_id")
        led_status = request.form.get("led_status")
        Trainings_service.update_ledstatus(module_id=module_id,led_status=led_status)
        return redirect(url_for("modules"))

    @app.route("/admin/getdata" , methods=["POST"])
    def get_data():
        atleet_id = request.form.get("atleet_id")
        data,begintijd = Trainings_service.get_data(atleet_id=atleet_id)
        return render_template("/admin/getterdata.html" , data = data, begintijd=begintijd)
    
    @app.route("/admin/gebruikers")
    def gebruikers():
        
        gebruikers = gebruiker_service.get_gebruikers()
        
        return render_template("/admin/gebruikers.html" , gebruikers = gebruikers)
    @app.route("/admin/gebruiker/toevoegen", methods=["POST"])
    def gebruiker_toevoegen():
        
        gebruikersnaam = request.form.get("gebruikersnaam")
        voornaam = request.form.get("voornaam")
        achternaam = request.form.get("achternaam")
        geboortedatum = request.form.get("geboortedatum")
        try:
            gebruiker_service.voeg_gebruiker_toe(gebruikersnaam=gebruikersnaam,voornaam=voornaam,achternaam=achternaam,geboortedatum=geboortedatum)
        except ValueError as e:
            flash(str(e), "error")
        return redirect(url_for("gebruikers"))
    
    @app.route("/admin/gebruiker/verwijderen", methods=["POST"])
    def gebruiker_verwijderen():
        gebruikersnaam = request.form.get("naam")
        gebruiker_service.verwijder_gebruiker(gebruikersnaam=gebruikersnaam)
        return redirect(url_for("gebruikers"))
    
    @app.route("/admin/module/verwijder", methods=["POST"])
    def module_verwijderder():
        ID = request.form.get("ID")
        moduleservice.verwijder_module(ID=ID)
        return redirect(url_for("modules"))
    @app.route("/admin/module/toevoegen", methods=["POST"])
    def voeg_module_toe():
        ID = request.form.get("ID")
        try:
            moduleservice.voeg_module_toe(ID=ID)
        except ValueError as e:
            flash(str(e), "error")
        return redirect(url_for("modules"))
    
    @app.route("/admin/getloopmodule", methods=["POST"])
    def get_loopmodule():
        atleet_id = request.form.get("atleet_id")
        try:
            id = moduleservice.get_module_id(atleet_id)
            if id == []:
                id = -1
            else:
               id= id[0][0]
        except ValueError as e:
            id = -1
        return render_template("/admin/getter.html" , data = [id])
    
    @app.route("/admin/getloopmodulebylist", methods=["POST"])
    def get_loopmodulebylist():
        Loopmodule = request.form.get("loopmodule", "0")
        return render_template("/admin/getter.html" , data = Loopmodule)
    @app.route("/admin/eindetraining", methods=["POST"])
    def einde_training():
        module_id = request.form.get("id")
        
        try:
            moduleservice.postmodule(atleet_id=0,module_id=module_id)
        except ValueError as e:
            pass
        return redirect(url_for("modules"))
    

    return app
