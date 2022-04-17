import tkinter as tk
import query as q

id = 1
window = tk.Tk()
window.geometry("240x320")
window.title("Password Manager")

name = tk.StringVar()
login = tk.StringVar()
password = tk.StringVar()

name = tk.Entry()
name.insert(0, "Name")
name.place(relx=.5, rely=.1, anchor="c")

login = tk.Entry()
login.insert(0, "Login")
login.place(relx=.5, rely=.2, anchor="c")

password = tk.Entry(show='*')
password.place(relx=.5, rely=.3, anchor="c")

submit_button = tk.Button(text="Submit", 
    command=lambda: q.insert(f"""INSERT INTO logpw (id, name, login, password) VALUES ('{id}', '{name.get()}', '{login.get()}', '{password.get()}');"""))
submit_button.place(relx=.5, rely=.5, anchor="c")

window.mainloop()