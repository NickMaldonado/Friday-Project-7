import tkinter as tk
from tkinter import messagebox
import sqlite3

# This file promtps the user to sign in using their email and password that's stored in users.db

def signin():
    email = email_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Check if email/password combination exists
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()

    if user:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Email or password incorrect")

    # Close the connection
    conn.close()

# Create the sign-in window
signin_window = tk.Tk()
signin_window.title("Sign In")

# Create and place widgets
email_label = tk.Label(signin_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(signin_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(signin_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(signin_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

signin_button = tk.Button(signin_window, text="Sign In", command=signin)
signin_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

signin_window.mainloop()
