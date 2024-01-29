
import tkinter as tk
import tkinter.ttk as ttk
from employeeClasses import Formature
from employeeClasses import Agent
from tkinter import messagebox

class clsAddEmployeeWindow(tk.Toplevel):
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

          self.btnAddEmployer = tk.Button(self.top)
          self.btnAddEmployer.place(relx=0.367, rely=0.889, height=36, width=150)
          self.btnAddEmployer.configure(takefocus="")
          self.btnAddEmployer.configure(text='''ADD EMP''')
          self.btnAddEmployer.configure(compound='left')
          self.btnAddEmployer.configure(command=self.addEmployee)

          self.enHeureSup = tk.Entry(self.top,state="disabled")
          self.enHeureSup.place(relx=0.283, rely=0.8, relheight=0.064, relwidth=0.09)
          self.enHeureSup.configure(takefocus="")
          self.enHeureSup.configure(cursor="ibeam")

          self.TSeparator1 = ttk.Separator(self.top)
          self.TSeparator1.place(relx=0.4, rely=0.8,  relheight=0.067)
          self.TSeparator1.configure(orient="vertical")

          self.TLabel5 = tk.Label(self.top)
          self.TLabel5.place(relx=0.433, rely=0.8, height=27, width=83)
          self.TLabel5.configure(font="TkDefaultFont")
          self.TLabel5.configure(relief="flat")
          self.TLabel5.configure(anchor='w')
          self.TLabel5.configure(justify='left')
          self.TLabel5.configure(text='''prime respo :''')
          self.TLabel5.configure(compound='left')
          
          self.enPrimeRespo = tk.Entry(self.top,state="disabled")
          self.enPrimeRespo.place(relx=0.6, rely=0.8, relheight=0.064, relwidth=0.157)
          self.enPrimeRespo.configure(takefocus="")
          self.enPrimeRespo.configure(cursor="ibeam")
  


          self.rdbAgent = tk.Radiobutton(self.top,variable=self.empType,value="agent")
          self.rdbAgent.place(relx=0.3, rely=0.711, relheight=0.056, relwidth=0.13)
  
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
          self.rdbAgent.configure(command=self.EnableRightEntry)
  
          self.rdbFormateur = tk.Radiobutton(self.top,variable= self.empType ,value="formateur")
          self.rdbFormateur.place(relx=0.45, rely=0.711, relheight=0.056, relwidth=0.163)

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
          self.rdbFormateur.configure(command=self.EnableRightEntry)
  
          self.TLabel3 = tk.Label(self.top)
          self.TLabel3.place(relx=0.1, rely=0.622, height=27, width=113)
          self.TLabel3.configure(font="TkDefaultFont")
          self.TLabel3.configure(relief="flat")
          self.TLabel3.configure(anchor='w')
          self.TLabel3.configure(justify='left')
          self.TLabel3.configure(text='''salire base :''')
          self.TLabel3.configure(compound='left')
  
          self.TLabel4 = tk.Label(self.top)
          self.TLabel4.place(relx=0.1, rely=0.8, height=27, width=83)
          self.TLabel4.configure(font="TkDefaultFont")
          self.TLabel4.configure(relief="flat")
          self.TLabel4.configure(anchor='w')
          self.TLabel4.configure(justify='left')
          self.TLabel4.configure(text='''heure sup :''')
          self.TLabel4.configure(compound='left')
  
          self.Label1 = tk.Label(self.top)
          self.Label1.place(relx=0.1, rely=0.711, height=21, width=104)
          self.Label1.configure(activebackground="#d9d9d9")
          self.Label1.configure(activeforeground="black")
          self.Label1.configure(anchor='w')
          self.Label1.configure(background="#d9d9d9")
          self.Label1.configure(compound='left')
          self.Label1.configure(disabledforeground="#a3a3a3")
          self.Label1.configure(foreground="#000000")
          self.Label1.configure(highlightbackground="#d9d9d9")
          self.Label1.configure(highlightcolor="#000000")
          self.Label1.configure(text='''employer Type :''')
  
          self.enSalaireBase = tk.Entry(self.top)
          self.enSalaireBase.place(relx=0.3, rely=0.622, relheight=0.064, relwidth=0.207)
          self.enSalaireBase.configure(takefocus="")
          self.enSalaireBase.configure(cursor="ibeam")
  
          self.enDateEmbauche = tk.Entry(self.top)
          self.enDateEmbauche.place(relx=0.3, rely=0.533, relheight=0.064, relwidth=0.207)
          self.enDateEmbauche.configure(takefocus="")
          self.enDateEmbauche.configure(cursor="ibeam")
  
          self.TLabel1_1_1 = tk.Label(self.top)
          self.TLabel1_1_1.place(relx=0.1, rely=0.533, height=27, width=113)
          self.TLabel1_1_1.configure(font="-family {Segoe UI} -size 9")
          self.TLabel1_1_1.configure(relief="flat")
          self.TLabel1_1_1.configure(anchor='w')
          self.TLabel1_1_1.configure(justify='left')
          self.TLabel1_1_1.configure(text='''date eumbauche :''')
          self.TLabel1_1_1.configure(compound='left')
  
          self.TLabel2 = tk.Label(self.top)
          self.TLabel2.place(relx=0.1, rely=0.444, height=27, width=113)
          self.TLabel2.configure(font="TkDefaultFont")
          self.TLabel2.configure(relief="flat")
          self.TLabel2.configure(anchor='w')
          self.TLabel2.configure(justify='left')
          self.TLabel2.configure(text='''date naissance :''')
          self.TLabel2.configure(compound='left')
  
          self.enDateNaissance = tk.Entry(self.top)
          self.enDateNaissance.place(relx=0.3, rely=0.444, relheight=0.064
                  , relwidth=0.207)
          self.enDateNaissance.configure(takefocus="")
          self.enDateNaissance.configure(cursor="ibeam")
  
          self.enNom = tk.Entry(self.top)
          self.enNom.place(relx=0.3, rely=0.356, relheight=0.064, relwidth=0.423)
          self.enNom.configure(takefocus="")
          self.enNom.configure(cursor="ibeam")
  
          self.enMatricule = tk.Entry(self.top)
          self.enMatricule.place(relx=0.3, rely=0.267, relheight=0.064
                  , relwidth=0.207)
          self.enMatricule.configure(takefocus="")
          self.enMatricule.configure(cursor="ibeam")
  
          self.TLabel1 = tk.Label(self.top)
          self.TLabel1.place(relx=0.1, rely=0.267, height=27, width=83)
          self.TLabel1.configure(font="TkDefaultFont")
          self.TLabel1.configure(relief="flat")
          self.TLabel1.configure(anchor='w')
          self.TLabel1.configure(justify='left')
          self.TLabel1.configure(text='''matricule :''')
          self.TLabel1.configure(compound='left')
  
          self.TLabel1_1 = tk.Label(self.top)
          self.TLabel1_1.place(relx=0.1, rely=0.356, height=27, width=93)
          self.TLabel1_1.configure(font="-family {Segoe UI} -size 9")
          self.TLabel1_1.configure(relief="flat")
          self.TLabel1_1.configure(anchor='w')
          self.TLabel1_1.configure(justify='left')
          self.TLabel1_1.configure(text='''nom complete :''')
          self.TLabel1_1.configure(compound='left')
  
          self.TSeparator2 = ttk.Separator(self.top)
          self.TSeparator2.place(relx=0.1, rely=0.2,  relwidth=0.817)
  
          self.TLabel6 = tk.Label(self.top)
          self.TLabel6.place(relx=0.233, rely=0.067, height=47, width=353)
          self.TLabel6.configure(font="-family {Segoe UI} -size 16 -weight bold")
          self.TLabel6.configure(relief="flat")
          self.TLabel6.configure(anchor='w')
          self.TLabel6.configure(justify='center')
          self.TLabel6.configure(text='''ADDING NEW EMPLOER WINDOW''')
          self.TLabel6.configure(compound='left')
     
     def EnableRightEntry(self):     
          if self.empType.get() == "formateur":
               self.enHeureSup["state"] = "normal"
               self.enPrimeRespo["state"] = "disabled"
          elif self.empType.get() == "agent":
               self.enPrimeRespo["state"] = "normal"
               self.enHeureSup["state"] = "disabled"
               
     def addEmployee(self):
          try:   
               if self.empType.get() == "agent":
                    salaire = int(self.enSalaireBase.get())
                    primeRespo = int(self.enPrimeRespo.get())
                    newAgent = Agent(self.enMatricule.get(),self.enNom.get(),self.enDateNaissance.get(),self.enDateEmbauche.get(),salaire,primeRespo)
                    newAgent.addAgentToJSON()

               elif self.empType.get() == "formateur":
                    salaire = int(self.enSalaireBase.get())
                    heureSup = int(self.enHeureSup.get())
                    newFormateur = Formature(self.enMatricule.get(),self.enNom.get(),self.enDateNaissance.get(),self.enDateEmbauche.get(),salaire,heureSup)
                    newFormateur.addFormateurToJSON()
          
               self.top.destroy()
               messagebox.showinfo("add message", "employee added successfully!")
          except:
               messagebox.showinfo("add message", "employee add failed!! check your input!")
