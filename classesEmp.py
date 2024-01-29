from abc import ABC, abstractmethod
from datetime import datetime
import json

class IR:
    def __init__(self):
        self.tranches = [0,30000, 50000, 60000, 80000, 180000]
        self.tauxIR = [0,10, 20, 30, 34, 38]

    def geIR(self,salaire):
        salaireAnnuel = salaire * 12
        for i in range(5,-1,-1):
            if salaireAnnuel > self.tranches[i]:
                return  self.tauxIR[i] / 100
 


class IEmploye(ABC):
    @abstractmethod
    def age(self):
        pass 
    @abstractmethod
    def anciennete(self):
        pass
    @abstractmethod
    def dateRetrait(self,ageRetrait):
        pass


#from IEmployeFile import IEmploye
class Employe(IEmploye,IR,ABC):
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase):
        self._mtle = mtle
        self._nom = nom       
        self._dateNaissance = dateNaissance
        self._dateEmbuche = dateEmbuche
        self._salaireBase = salaireBase
    
    def mtle(self):
        return self._mtle 
    
    @property
    def nom(self):
        return self._nom 
    @nom.setter
    def nom(self,nom):
        self._nom= nom

    @property
    def dateNaissance(self):
        return self._dateNaissance 
    @dateNaissance.setter
    def dateNaissance(self,dateNaissance):
        self._dateNaissance= dateNaissance

    @property
    def dateEmbuche(self):
        return self._dateEmbuche 
    @dateEmbuche.setter
    def dateEmbuche(self,dateEmbuche):
        self._dateEmbuche= dateEmbuche

    @property
    def salaireBase(self):
        return self._salaireBase 
    @salaireBase.setter
    def salaireBase(self,salaireBase):
        self._salaireBase= salaireBase

    def age(self):
        todayDate = datetime.date.today()
        dateformat = "%d/%m/%Y"
        d = datetime.strptime(self.dateNaissance,dateformat)
        age = todayDate.year - d.year
        return age
    
    def dateRetrait(self, ageRetrait):
        dateformat = "%d/%m/%Y"
        d = datetime.strptime(self.dateNaissance,dateformat)
        return d - datetime.strptime(ageRetrait+"/01/"+"01")
        
    def anciennete(self):
        dateformat = "%d/%m/%Y"
        d = datetime.strptime(self.dateEmbuche,dateformat)

        todayDate = datetime.date.today()
        anc = todayDate.year - d.year
        return anc
    
    def isAncienneteGreaterthan20year(self):
        if self.anciennete() > 20:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self._mtle} - {self._nom} - {self._dateNaissance} - {self._dateEmbuche} - {self._salaireBase} "

    # def __eq__(self,e):
    #     if self._mtle == e.mtle:
    #         return True
    #     else :
    #         return False
        

    def getDataFromJSON(self,fileName): 
        try:
            with open(fileName, 'r') as file:
                data = json.load(file)
            return data
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def serialize_datetime(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def addDataToJson(self,data,fileName):  
        with open(fileName,"w") as f:
            json.dump(data,f,default=self.serialize_datetime,indent=2 )

    @abstractmethod
    def salaireAPayer(self):
        pass 

# form EmployeFile import Employe
class Formature(Employe):
    fileName = "formateurs.json"
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, heurSup):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self._heurSup = heurSup
        self._tariSup = 70

    @property
    def heurSup(self):
        return self._heurSup
    @heurSup.setter
    def heurSup(self,h):
        self._heurSup = h

    @property
    def tarifSup(self):
        return self._tarifSup

    def __str__(self):
        return f"{self.__str__()} - {self.heurSup} - {self.tarifSup}"

    def salaireAPayer(self):
        salaireNet = (self._salaireBase + self.heurSup * self.tarifSup ) * (1-self.geIR(self._salaireBase))
        return salaireNet
    
    def addFormateurToJSON(self):
        
        formsData = self.getDataFromJSON(Formature.fileName)
        
        newForm = {"matricule": self._mtle, 
                   "nom": self._nom, 
                   "date naissance": self._dateNaissance, 
                   "date embuche": self._dateEmbuche,
                   "salaire base": self._salaireBase,
                   "heur sup": self.heurSup}
        formsData.append(newForm)

        self.addDataToJson(formsData,Formature.fileName)

    def deleteForamteurFromJSON(self,FormteurID):
        formsData = self.getDataFromJSON(Formature.fileName)

        formsData = [record for record in formsData if record["matricule"] != FormteurID]

        self.addDataToJson(formsData,Formature.fileName)
   
    def findFormateurInJSON(self,FormateurID):
        formsData = self.getDataFromJSON(Formature.fileName)
        for record in formsData:
            if record["matricule"] == FormateurID:
                return record
        return None
    
    def updateFormateurInJSON(self,formateurID):
        self.deleteForamteurFromJSON(formateurID)
        self.addFormateurToJSON()
        



    def getAllFarmateurs(self):
        data = self.getDataFromJSON(Formature.fileName)
        return data

# form EmployeFile import Employe
class Agent(Employe):
    fileName = "agents.json"
    def __init__(self, mtle, nom, dateNaissance, dateEmbuche, salaireBase, primeRespo):
        super().__init__(mtle, nom, dateNaissance, dateEmbuche, salaireBase)
        self.primeRespo = primeRespo
        

    def salaireAPayer(self):
        salaireNet = (self._salaireBase + self.primeRespo) * (1 - self.geIR(self._salaireBase))
        return salaireNet

    def addAgentToJSON(self):
        agentsData = self.getDataFromJSON(Agent.fileName)
        newAgent = {"matricule": self._mtle, 
                   "nom": self._nom, 
                   "date naissance": self._dateNaissance, 
                   "date embuche": self._dateEmbuche,
                   "salaire base": self._salaireBase,
                   "prime respo": self.primeRespo}
        agentsData.append(newAgent)
        self.addDataToJson(agentsData, Agent.fileName)
    

    def deleteAgentFromJSON(self,agentID):
        agentsData = self.getDataFromJSON(Agent.fileName)

        agentsData = [record for record in agentsData if record["matricule"] != agentID]

        self.addDataToJson(agentsData, Agent.fileName)

    
    def findAgentInJSON(self,agentID):
        agentsData = self.getDataFromJSON(Agent.fileName)
       
        for record in agentsData:
            if record["matricule"] == agentID:
                return record
        return None
 
    def updateAgentInJSON(self,formateurID):
        self.deleteAgentFromJSON(formateurID)
        self.addAgentToJSON()

    def getAllAgents(self):
        agentsData = self.getDataFromJSON(Agent.fileName)
        return agentsData