import tkinter as tk
import tkinter.ttk as ttk
from employeeClasses import Formature
from employeeClasses import Agent
from tkinter import messagebox

class clsFindEmpWindow(tk.Toplevel):
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''

        top.geometry("600x450+396+202")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("add employee ")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")


        self.top = top
        self.empType = tk.StringVar()
        self.empType.set("agent")  # Set a default value

        self.btnFindEmployer = tk.Button(self.top)
        self.btnFindEmployer.place(relx=0.367, rely=0.770, height=36, width=150)
        self.btnFindEmployer.configure(takefocus="")
        self.btnFindEmployer.configure(text='''FIND EMP''')
        self.btnFindEmployer.configure(compound='left')
        self.btnFindEmployer.configure(command=self.findEmployee)

        self.rdbAgent = tk.Radiobutton(self.top,variable=self.empType,value="agent")
        self.rdbAgent.place(relx=0.6, rely=0.55, relheight=0.056, relwidth=0.13)
  
        self.rdbAgent.configure(activebackground="#d9d9d9")
        self.rdbAgent.configure(activeforeground="black")
        self.rdbAgent.configure(anchor='w')
        self.rdbAgent.configure(background="#d9d9d9")
        self.rdbAgent.configure(compound='left')
        self.rdbAgent.configure(disabledforeground="#a3a3a3")
        self.rdbAgent.configure(foreground="#000000")
        self.rdbAgent.configure(highlightbackground="#d9d9d9")
        self.rdbAgent.configure(highlightcolor="#000000")
        self.rdbAgent.configure(justify='left')
        self.rdbAgent.configure(text='''Agente''')
  
        self.rdbFormateur = tk.Radiobutton(self.top,variable= self.empType ,value="formateur")
        self.rdbFormateur.place(relx=0.760, rely=0.55, relheight=0.056, relwidth=0.163)



        self.rdbFormateur.configure(activebackground="#d9d9d9")
        self.rdbFormateur.configure(activeforeground="black")
        self.rdbFormateur.configure(anchor='w')
        self.rdbFormateur.configure(background="#d9d9d9")
        self.rdbFormateur.configure(compound='left')
        self.rdbFormateur.configure(disabledforeground="#a3a3a3")
        self.rdbFormateur.configure(foreground="#000000")
        self.rdbFormateur.configure(highlightbackground="#d9d9d9")
        self.rdbFormateur.configure(highlightcolor="#000000")
        self.rdbFormateur.configure(justify='left')
        self.rdbFormateur.configure(text='''formateur''')

        self.enMatricule = tk.Entry(self.top)
        self.enMatricule.place(relx=0.7, rely=0.35, relheight=0.064, relwidth=0.207)
        self.enMatricule.configure(takefocus="")
        self.enMatricule.configure(cursor="ibeam")

        self.TLabel1 = tk.Label(self.top)
        self.TLabel1.place(relx=0.1, rely=0.35, height=30, width=310)
        self.TLabel1.configure(font="-family {Segoe UI} -size 14 ")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''enter employee "matricule" to find :''')
        self.TLabel1.configure(compound='left')

        self.TLabel19 = tk.Label(self.top)
        self.TLabel19.place(relx=0.1, rely=0.55, height=30, width=250)
        self.TLabel19.configure(font="-family {Segoe UI} -size 14 ")
        self.TLabel19.configure(relief="flat")
        self.TLabel19.configure(anchor='w')
        self.TLabel19.configure(justify='left')
        self.TLabel19.configure(text='''choose employee type :''')
        self.TLabel19.configure(compound='left')


        self.TLabel6 = tk.Label(self.top)
        self.TLabel6.place(relx=0.233, rely=0.067, height=47, width=353)
        self.TLabel6.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='w')
        self.TLabel6.configure(justify='center')
        self.TLabel6.configure(text='''FINDING EMPLOER WINDOW''')
        self.TLabel6.configure(compound='left')
          
    def findEmployee(self):
        if self.empType.get() == "agent":
            agentMat = self.enMatricule.get()
            
            agentToFind = Agent(self.enMatricule.get(),"","","",0,0)
            self.agentToFind = agentToFind.findAgentInJSON(agentMat)
            if self.agentToFind != None:
                self.showAgentInfo()
            else:
                messagebox.showinfo("find message", "agent not exist!")

        elif self.empType.get() == "formateur":
           
            FormToFindMAT = self.enMatricule.get()
            
            FormToFind = Formature(self.enMatricule.get(),"","","",0,0)
            self.FormToFind = FormToFind.findFormateurInJSON(FormToFindMAT)
            if self.FormToFind != None:
                self.showFormateurInfo()
            else:
                messagebox.showinfo("find message", "formateur not exist!")


    def setHeading(self,table,empType):
        table.heading("mtle", text="matricule",anchor="center")
        table.heading("nom", text="nom")
        table.heading("dateNaissance", text="date Naissance")
        table.heading("dateEmbuche", text="date Embuche")
        table.heading("salaireBase", text="salaire Base",anchor="center")
        if empType == "f":
            table.heading("heurSup", text="heur Sup",anchor="center")
        else:
            table.heading("primeRespo", text="prime Respo",anchor="center")

    def setColumns(self,table,empType):
        table.column("mtle", anchor="center")
        table.column("nom", anchor="center")
        table.column("dateNaissance", anchor="center")
        table.column("dateEmbuche", anchor="center")
        table.column("salaireBase", anchor="center")

        if empType =="f":
            table.column("heurSup", anchor="center")
        else :
            table.column("primeRespo", anchor="center")

    def fillTable(self,table,empType): 
        if empType == "f":
            formateurData = self.FormToFind
            table.insert("", "end", 0, text="", values=(formateurData["matricule"],formateurData["nom"], formateurData["date naissance"], formateurData["date embuche"], formateurData["salaire base"], formateurData["heur sup"]))

        else:
            agentData = self.agentToFind
            table.insert("", "end", 0, text="", values=(agentData["matricule"],agentData["nom"], agentData["date naissance"], agentData["date embuche"], agentData["salaire base"], agentData["prime respo"]))

    def setUpTable(self,top,empType):
        if empType =="f":
            table = ttk.Treeview(top, columns=("mtle","nom", "dateNaissance", "dateEmbuche","salaireBase","heurSup"), show="headings")
        else :
            table = ttk.Treeview(top, columns=("mtle","nom", "dateNaissance", "dateEmbuche","salaireBase","primeRespo"), show="headings")

        self.setHeading(table,empType)
        self.setColumns(table,empType)
       
        self.fillTable(table,empType)

        table.pack(fill="both")

    def showFormateurInfo(self):
        top = tk.Toplevel()

        lblFormInfo = tk.Label(top,text="Formateur information: ", font="-family {Segoe UI} -size 16 -weight bold")
        lblFormInfo.pack()
        self.setUpTable(top,"f")

    def showAgentInfo(self):
        top = tk.Toplevel()
        lblAgentInfo = tk.Label(top,text="Agent information: ", font="-family {Segoe UI} -size 16 -weight bold")
        lblAgentInfo.pack()
        self.setUpTable(top,"a")