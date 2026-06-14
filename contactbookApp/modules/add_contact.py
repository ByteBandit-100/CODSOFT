import sqlite3
import tkinter as tk
from logging import root


def open_add_contact_window():
    # New popup window
    form = tk.Toplevel()
    form.title("Add Contact")
    form.geometry("400x300")
    form.configure(bg="white")

    # Labels + Entry fields
    tk.Label(form, text="Name:", bg="white").pack(pady=5, side="left")
    name_entry = tk.Entry(form, width=50)
    name_entry.pack(pady=5)

    tk.Label(form, text="Contact:", bg="white").pack(pady=5, side="left")
    contact_entry = tk.Entry(form, width=50)
    contact_entry.pack(pady=5)

    tk.Label(form, text="Address (optional):", bg="white").pack(pady=5, side="left")
    address_entry = tk.Entry(form, width=50)
    address_entry.pack(pady=5)

    # Save button
    def save_contact():
        name = name_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()

        # Store in separate DB file
        conn = sqlite3.connect("contacts_data.db")   # different file
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL ,
                contact TEXT NOT NULL,
                address TEXT
            )
        """)
        cur.execute("INSERT INTO contacts (name, contact, address) VALUES (?, ?, ?)",
                    (name, contact, address))
        conn.commit()
        conn.close()

        tk.Label(form, text="Contact saved!", fg="green", bg="white").pack(pady=10)

    tk.Button(form, text="Save", command=save_contact, bg="#42adf0", fg="white").pack(pady=20)



