import tkinter as tk
from addEmpWindow import clsAddEmployeeWindow
from showAllEmpInfo import clsShowEmpInfo
from updateEmp import clsUpdatEmp
from findEmp import clsFindEmpWindow
from deleteEmp import clsDeletEmpWindow

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'

class mainWindow:
    def __init__(self, top=None):
        
        top.geometry("600x437+359+137")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Employers App")
        top.configure(background="#79bcff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.btnShowEmp = tk.Button(self.top)
        self.btnShowEmp.place(relx=0.183, rely=0.297, height=46, width=417)
        self.btnShowEmp.configure(activebackground="#d9d9d9")
        self.btnShowEmp.configure(activeforeground="black")
        self.btnShowEmp.configure(background="#0053a6")
        self.btnShowEmp.configure(disabledforeground="#a3a3a3")
        self.btnShowEmp.configure(font="-family {Segoe UI} -size 14")
        self.btnShowEmp.configure(foreground="#ffff80")
        self.btnShowEmp.configure(highlightbackground="#d9d9d9")
        self.btnShowEmp.configure(highlightcolor="#000000")
        self.btnShowEmp.configure(text='''Show all Employees info''')
        self.btnShowEmp.configure(command=self.showAllEmployees)

        self.btnDeleteEmployee = tk.Button(self.top)
        self.btnDeleteEmployee.place(relx=0.183, rely=0.503, height=46, width=187)
        self.btnDeleteEmployee.configure(activebackground="#d9d9d9")
        self.btnDeleteEmployee.configure(activeforeground="black")
        self.btnDeleteEmployee.configure(background="#0053a6")
        self.btnDeleteEmployee.configure(disabledforeground="#a3a3a3")
        self.btnDeleteEmployee.configure(font="-family {Segoe UI} -size 14")
        self.btnDeleteEmployee.configure(foreground="#ffff80")
        self.btnDeleteEmployee.configure(highlightbackground="#d9d9d9")
        self.btnDeleteEmployee.configure(highlightcolor="#000000")
        self.btnDeleteEmployee.configure(text='''Delete Employee''')
        self.btnDeleteEmployee.configure(command=self.deleteEmployee)
     
        self.btnFindEmployee = tk.Button(self.top)
        self.btnFindEmployee.place(relx=0.183, rely=0.709, height=46, width=167)
        self.btnFindEmployee.configure(activebackground="#d9d9d9")
        self.btnFindEmployee.configure(activeforeground="black")
        self.btnFindEmployee.configure(background="#0053a6")
        self.btnFindEmployee.configure(disabledforeground="#a3a3a3")
        self.btnFindEmployee.configure(font="-family {Segoe UI} -size 14")
        self.btnFindEmployee.configure(foreground="#ffff80")
        self.btnFindEmployee.configure(highlightbackground="#d9d9d9")
        self.btnFindEmployee.configure(highlightcolor="#000000")
        self.btnFindEmployee.configure(text='''Find Employee''')
        self.btnFindEmployee.configure(command=self.findEmployee)
    
        self.btnUpdateEmployee = tk.Button(self.top)
        self.btnUpdateEmployee.place(relx=0.483, rely=0.709, height=46, width=237)
        self.btnUpdateEmployee.configure(activebackground="#d9d9d9")
        self.btnUpdateEmployee.configure(activeforeground="black")
        self.btnUpdateEmployee.configure(background="#0053a6")
        self.btnUpdateEmployee.configure(disabledforeground="#a3a3a3")
        self.btnUpdateEmployee.configure(font="-family {Segoe UI} -size 14")
        self.btnUpdateEmployee.configure(foreground="#ffff80")
        self.btnUpdateEmployee.configure(highlightbackground="#d9d9d9")
        self.btnUpdateEmployee.configure(highlightcolor="#000000")
        self.btnUpdateEmployee.configure(text='''Update Employee info''')
        self.btnUpdateEmployee.configure(command=self.updateEmployee)

        # self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        # top.configure(menu = self.menubar)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.1, rely=0.114, height=61, width=324)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#79bcff")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Chose a proccess to execut :''')
   
        self.btnAddEmployee = tk.Button(self.top)
        self.btnAddEmployee.place(relx=0.567, rely=0.503, height=46, width=187)
        self.btnAddEmployee.configure(activebackground="#d9d9d9")
        self.btnAddEmployee.configure(activeforeground="black")
        self.btnAddEmployee.configure(background="#0053a6")
        self.btnAddEmployee.configure(disabledforeground="#a3a3a3")
        self.btnAddEmployee.configure(font="-family {Segoe UI} -size 14")
        self.btnAddEmployee.configure(foreground="#ffff80")
        self.btnAddEmployee.configure(highlightbackground="#d9d9d9")
        self.btnAddEmployee.configure(highlightcolor="#000000")
        self.btnAddEmployee.configure(text='''Add Employee''')
        self.btnAddEmployee.configure(command=self.addEmployee)
    
    def addEmployee(self):
        addWin = tk.Toplevel(self.top)
        win = clsAddEmployeeWindow(addWin)

    def updateEmployee(self):     
        updateWin = tk.Toplevel(self.top)
        win = clsUpdatEmp(updateWin)
        
    def showAllEmployees(self):
        clsShowEmpInfo.showEmployeesInfo()
        
    def deleteEmployee(self):
        deleteWin = tk.Toplevel(self.top)
        win = clsDeletEmpWindow(deleteWin)

        

    def findEmployee(self):
        findWin = tk.Toplevel(self.top)
        win = clsFindEmpWindow(findWin)

 
  


root = tk.Tk()

root.geometry("800x600")
app = mainWindow(root)

root.mainloop()