import tkinter as tk
from tkinter import ttk
import query as q

window = tk.Tk()
window.geometry("400x500")
window.title("PWKeep")

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
reg = ttk.Frame(tabControl)
auth = ttk.Frame(tabControl)

scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side='right', fill='y')

ttk.Label(tab1, text="Enter Name").grid(row=0, column=0, sticky='W', pady=35)
ttk.Label(tab1, text="Enter Login").grid(row=1, column=0, sticky='W', pady=0)
ttk.Label(tab1, text="Enter Password").grid(row=2, column=0, sticky='W', pady=25)

ttk.Label(reg, text="Enter Login").grid(row=0, column=0, sticky='W', pady=35)
ttk.Label(reg, text="Enter Password").grid(row=1, column=0, sticky='W', pady=0)

ttk.Label(auth, text="Enter Login").grid(row=0, column=0, sticky='W', pady=35)
ttk.Label(auth, text="Enter Password").grid(row=1, column=0, sticky='W', pady=0)

tabControl.add(auth, text='Auth')
tabControl.add(reg, text='Register')
tabControl.add(tab1, text='Enter')
tabControl.add(tab2, text='Saved')
tabControl.pack(expand=1, fill="both")

auth_login = tk.StringVar()
auth_password = tk.StringVar()

auth_login = ttk.Entry(auth)
auth_login.place(relx=.5, rely=.1, anchor="c")

auth_password = ttk.Entry(auth, show='*')
auth_password.place(relx=.5, rely=.2, anchor="c")

reg_login = tk.StringVar()
reg_password = tk.StringVar()

reg_login = ttk.Entry(reg)
reg_login.place(relx=.5, rely=.1, anchor="c")

reg_password = ttk.Entry(reg, show='*')
reg_password.place(relx=.5, rely=.2, anchor="c")

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
    prev_id = [q.out("""SELECT * from logpw""")][-1][-1]
    new_id = int(prev_id[0]) + 1
    return new_id


def reg_id():
    prev_id = [q.reg_out()][-1][-1]
    new_id = int(prev_id[0]) + 1
    return new_id


def clean(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    text = ttk.Label(frame, text='Name - Login - Password')
    text.pack(anchor='w')


def auth1(login, passw, mspass):
    is_authorized = False
    if is_authorized:
        return None
    else:
        if q.auth(login, passw, mspass):
            is_authorized = True
            listbox = tk.Listbox(tab2, yscrollcommand=scrollbar.set)
            lst = q.out(f"""SELECT name, login, password FROM logpw WHERE added_by='{login}'""")
            print(lst)
            for i in lst:
                listbox.insert("end", i)
            listbox.pack(expand=True, fill="both")
            scrollbar.config(command=listbox.yview)
        else:
            print('Неверный логин, пароль или мастер-пароль')


def refresh(login):
    clean(tab2)
    listbox = tk.Listbox(tab2, yscrollcommand=scrollbar.set)
    lst = q.out(f"""SELECT name, login, password FROM logpw WHERE added_by='{login}'""")
    print(lst)
    for i in lst:
        listbox.insert("end", i)
    listbox.pack(expand=True, fill="both")
    scrollbar.config(command=listbox.yview)


submit_button = ttk.Button(tab1, text="Submit",
                           command=lambda: [q.insert(f"""INSERT INTO logpw (id, name, login, password, added_by) VALUES ('{id()}', '{name.get()}', '{login.get()}', '{password.get()}', '{auth_login.get()}');"""),
                                            refresh(auth_login.get())])
submit_button.place(relx=.5, rely=.5, anchor="c")

reg_submit_button = ttk.Button(reg, text="Submit",
                               command=lambda: q.check(reg_login.get(), f"""INSERT INTO registred (id, login, password) VALUES ('{reg_id()}', '{reg_login.get()}', '{reg_password.get()}');"""))
reg_submit_button.place(relx=.5, rely=.5, anchor="c")

auth_submit_button = ttk.Button(auth, text="Submit", command=lambda: [clean(tab2), auth1(auth_login.get(), auth_password.get())])
auth_submit_button.place(relx=.5, rely=.5, anchor="c")

window.mainloop()
