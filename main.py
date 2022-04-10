import tkinter as tk

window = tk.Tk()
window.geometry("480x640")
window.title("Password Manager")

login = tk.Entry()
login.place(relx=.5, rely=.1, anchor="c")


window.mainloop()