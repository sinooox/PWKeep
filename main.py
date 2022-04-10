import tkinter as tk
import query as q

id = 1
window = tk.Tk()
window.geometry("480x640")
window.title("Password Manager")

login = tk.StringVar()
password = tk.StringVar()

login = tk.Entry()
login.place(relx=.5, rely=.1, anchor="c")

password = tk.Entry(show='*')
password.place(relx=.5, rely=.2, anchor="c")

submit_button = tk.Button(text="Submit", 
    command=lambda: q.insert(f"""INSERT INTO logpw (id, login, password) VALUES ('{id}', '{login.get()}', '{password.get()}');"""))
submit_button.place(relx=.5, rely=.5, anchor="c")

window.mainloop()