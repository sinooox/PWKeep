import tkinter as tk
from tkinter import ttk
import query as q

window = tk.Tk()
window.geometry("400x500")
window.title("PWKeep")

tabControl = ttk.Notebook(window)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

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

refresh_button = ttk.Button(tab2, text="Refresh", command=tab2.update())
refresh_button.pack(anchor='s')

tabControl.add(tab1, text='Enter')
tabControl.add(tab2, text='Saved')
tabControl.pack(expand=1, fill="both")

name = tk.StringVar()
login = tk.StringVar()
password = tk.StringVar()

name = ttk.Entry(tab1)
name.insert(0, "Name")
name.place(relx=.5, rely=.1, anchor="c")

login = ttk.Entry(tab1)
login.insert(0, "Login")
login.place(relx=.5, rely=.2, anchor="c")

password = ttk.Entry(tab1, show='*')
password.place(relx=.5, rely=.3, anchor="c")

def id():
    prev_id = [q.out()][-1][-1]
    new_id = int(prev_id[0]) + 1
    return new_id

submit_button = ttk.Button(tab1, text="Submit", 
    command=lambda:q.insert(f"""INSERT INTO logpw (id, name, login, password) VALUES ('{id()}', '{name.get()}', '{login.get()}', '{password.get()}');"""))
submit_button.place(relx=.5, rely=.5, anchor="c")

window.mainloop()