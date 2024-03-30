import tkinter as tk
from tkinter import messagebox
import sqlite3

# This file prompts the user to enter in their email and create a password to be attached with the email
# The information is stored in the database "users.db"
# Practice login email and password: nick@email.com, password

def signup():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validation
    if not email or not password or not confirm_password:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    if "@" not in email:
        messagebox.showerror("Error", "Invalid email format")
        return
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Save to database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Sign-up successful")

# Create the sign-up window
signup_window = tk.Tk()
signup_window.title("Sign Up")

# Create and place widgets
email_label = tk.Label(signup_window, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(signup_window)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(signup_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(signup_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

confirm_password_label = tk.Label(signup_window, text="Confirm Password:")
confirm_password_label.grid(row=2, column=0, padx=10, pady=5)
confirm_password_entry = tk.Entry(signup_window, show="*")
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(signup_window, text="Sign Up", command=signup)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

signup_window.mainloop()
