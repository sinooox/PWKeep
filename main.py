import tkinter as tk
from tkinter import ttk
import query as q
import os

window = tk.Tk()
window.geometry("400x500")
window.title("PWKeep")

tabControl = ttk.Notebook(window)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
reg = ttk.Frame(tabControl)

def update():
    window.destroy()
    os.system('main.py')

l = ttk.Label(tab2, text='ID Name Login Password')
l.pack(anchor='w')

scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side='right', fill='y')

listbox = tk.Listbox(tab2, yscrollcommand=scrollbar.set)

lst = q.out()
for i in lst:
    listbox.insert("end", i)
listbox.pack(expand=True, fill="both")
scrollbar.config(command=listbox.yview)

refresh_button = ttk.Button(tab2, text="Refresh", command=lambda: update())
refresh_button.pack(anchor='s')

ttk.Label(tab1, text="Enter Name").grid(row=0, column=0, sticky='W', pady=35)
ttk.Label(tab1, text="Enter Login").grid(row=1, column=0, sticky='W', pady=0)
ttk.Label(tab1, text="Enter Password").grid(row=2, column=0, sticky='W', pady=25)

tabControl.add(reg, text='Register')
tabControl.add(tab1, text='Enter')
tabControl.add(tab2, text='Saved')
tabControl.pack(expand=1, fill="both")

reg_login = tk.StringVar()
reg_password = tk.StringVar()
master_password = tk.StringVar()

reg_login = ttk.Entry(reg)
reg_login.place(relx=.5, rely=.1, anchor="c")

reg_password = ttk.Entry(reg, show='*')
reg_password.place(relx=.5, rely=.2, anchor="c")

master_password = ttk.Entry(reg, show='*')
master_password.place(relx=.5, rely=.3, anchor="c")

name = tk.StringVar()
login = tk.StringVar()
password = tk.StringVar()

name = ttk.Entry(tab1)
name.place(relx=.5, rely=.1, anchor="c")

login = ttk.Entry(tab1)
login.place(relx=.5, rely=.2, anchor="c")

password = ttk.Entry(tab1, show='*')
password.place(relx=.5, rely=.3, anchor="c")

def id():
    prev_id = [q.out()][-1][-1]
    new_id = int(prev_id[0]) + 1
    return new_id

def reg_id():
    prev_id = [q.reg_out()][-1][-1]
    new_id = int(prev_id[0]) + 1
    return new_id

submit_button = ttk.Button(tab1, text="Submit", 
    command=lambda:q.insert(f"""INSERT INTO logpw (id, name, login, password) VALUES ('{id()}', '{name.get()}', '{login.get()}', '{password.get()}');"""))
submit_button.place(relx=.5, rely=.5, anchor="c")

reg_submit_button = ttk.Button(reg, text="Submit", command=lambda: q.check(reg_login.get(), f"""INSERT INTO registred (id, login, password, masterpassword) VALUES ('{reg_id()}', '{reg_login.get()}', '{reg_password.get()}', '{master_password.get()}');"""))
reg_submit_button.place(relx=.5, rely=.5, anchor="c")

window.mainloop()