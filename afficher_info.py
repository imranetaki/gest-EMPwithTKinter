import tkinter as tk
from tkinter import ttk
from employeeClasses import *
class clsShowEmpInfo(tk.Toplevel):
    def setHeading(table,empType):
        table.heading("mtle", text="matricule",anchor="center")
        table.heading("nom", text="nom")
        table.heading("dateNaissance", text="date Naissance")
        table.heading("dateEmbuche", text="date Embuche")
        table.heading("salaireBase", text="salaire Base",anchor="center")
        if empType == "f":
            table.heading("heurSup", text="heur Sup",anchor="center")
        else:
            table.heading("primeRespo", text="prime Respo",anchor="center")

    def setColumns(table,empType):
        table.column("mtle", anchor="center")
        table.column("nom", anchor="center")
        table.column("dateNaissance", anchor="center")
        table.column("dateEmbuche", anchor="center")
        table.column("salaireBase", anchor="center")

        if empType =="f":
            table.column("heurSup", anchor="center")
        else :
            table.column("primeRespo", anchor="center")

    def fillTable(table,empType): 
        if empType == "f":
            empEmpty = Formature(" "," "," "," ",0,0)
            formateursData = empEmpty.getAllFarmateurs()
            
            for i, emp in enumerate(formateursData):
                table.insert("", "end", f"formateur{i+1}", text="", values=(emp["matricule"],emp["nom"], emp["date naissance"], emp["date embuche"], emp["salaire base"], emp["heur sup"]))

        else:
            empEmpty = Agent(" "," "," "," ",0,0)
            agentsData = empEmpty.getAllAgents()
            for i, emp in enumerate(agentsData):
                table.insert("", "end", f"agent{i+1}", text="", values=(emp["matricule"],emp["nom"], emp["date naissance"], emp["date embuche"], emp["salaire base"], emp["prime respo"]))


        
    def setUpTable(top,empType):
        if empType =="f":
            table = ttk.Treeview(top, columns=("mtle","nom", "dateNaissance", "dateEmbuche","salaireBase","heurSup"), show="headings")
        else :
            table = ttk.Treeview(top, columns=("mtle","nom", "dateNaissance", "dateEmbuche","salaireBase","primeRespo"), show="headings")

        clsShowEmpInfo.setHeading(table,empType)
        clsShowEmpInfo.setColumns(table,empType)
       
        clsShowEmpInfo.fillTable(table,empType)

        table.pack(fill="both")

    def showFormateursInfo(top):
        lblFormInfo = tk.Label(top,text="Formateurs information: ", font="-family {Segoe UI} -size 16 -weight bold")
        lblFormInfo.pack()
        clsShowEmpInfo.setUpTable(top,"f")

    def showAgentsInfo(top):
        lblFormInfo = tk.Label(top,text="Agents information: ", font="-family {Segoe UI} -size 16 -weight bold")
        lblFormInfo.pack()
        clsShowEmpInfo.setUpTable(top,"a")
    
    
    
    def showEmployeesInfo() :
        top = tk.Toplevel()
        clsShowEmpInfo.showFormateursInfo(top)
        clsShowEmpInfo.showAgentsInfo(top)