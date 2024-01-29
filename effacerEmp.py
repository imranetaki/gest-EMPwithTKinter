import tkinter as tk
import tkinter.ttk as ttk
from employeeClasses import Formature
from employeeClasses import Agent
from tkinter import messagebox

class clsDeletEmpWindow(tk.Toplevel):
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''

        top.geometry("600x450+396+202")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("delete employee ")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")


        self.top = top
        self.empType = tk.StringVar()
        self.empType.set("agent")  # Set a default value

        self.btnDeleteEmployer = tk.Button(self.top)
        self.btnDeleteEmployer.place(relx=0.367, rely=0.770, height=36, width=150)
        self.btnDeleteEmployer.configure(takefocus="")
        self.btnDeleteEmployer.configure(text='''DELETE EMP''')
        self.btnDeleteEmployer.configure(compound='left')
        self.btnDeleteEmployer.configure(command=self.deleteEmployee)

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
        self.TLabel1.place(relx=0.1, rely=0.35, height=30, width=350)
        self.TLabel1.configure(font="-family {Segoe UI} -size 14 ")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''enter employee "matricule" to DELETE :''')
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
        self.TLabel6.configure(text='''DELETING EMPLOER WINDOW''')
        self.TLabel6.configure(compound='left')
          
    def deleteEmployee(self):
        id = self.enMatricule.get()
        if self.empType.get() == "agent":
            
            agentToDelete = Agent("","","","",0,0)
            agentToDelete = agentToDelete.findAgentInJSON(id)
            if agentToDelete != None:
                self.deleteAgent()
                messagebox.showinfo("delete message", "agent deleted successfully!")

            else:
                messagebox.showinfo("delete message", "agent not exist!")

        elif self.empType.get() == "formateur":
           
            FormToDelete = Formature("","","","",0,0)
            FormToDelete = FormToDelete.findFormateurInJSON(id)
            if FormToDelete != None:
                self.deleteFormateur(id)
                messagebox.showinfo("delete message", "formateur deleted successfully!")

            else:
                messagebox.showinfo("delete message", "formateur not exist!")
    
    def deleteFormateur(self,id):
        empyForm = Formature("","","","",0,0)
        empyForm.deleteForamteurFromJSON(id)
    
    def deleteAgent(self,id):
        empyForm = Agent("","","","",0,0)
        empyForm.deleteAgentFromJSON(id)