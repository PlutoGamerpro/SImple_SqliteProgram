import tkinter as tk


def login():
    username = entry_user.get()
    password = entry_pass.get()
    print(username, password)


window = tk.Tk()
window.title("Login")

tk.Label(window, text="Username").pack()
entry_user = tk.Entry(window)
entry_user.pack()

tk.Label(window, text="Password").pack()
entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

tk.Button(window, text="Login", command=login).pack()

window.mainloop()
