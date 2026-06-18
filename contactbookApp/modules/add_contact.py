import sqlite3
import tkinter as tk
import re

def open_add_contact_window():
    form = tk.Toplevel()
    form.title("Add Contact")
    form.geometry("400x300")
    form.configure(bg="white")
    form.resizable(False, False)

    def add_row(parent, label_text, width=30):
        row = tk.Frame(parent, bg="white")
        row.pack(fill="x", padx=10, pady=5)
        tk.Label(row, text=label_text, bg="white", anchor="w", width=12).pack(side="left")
        entry = tk.Entry(row, width=width)
        entry.pack(side="left", fill="x", expand=True)
        return entry

    name_entry = add_row(form, "Name: *", width=30)
    contact_entry = add_row(form, "Contact: *", width=30)
    gmail_entry = add_row(form, "Gmail:", width=30)
    address_entry = add_row(form, "Address:", width=40)

    message_label = tk.Label(form, text="", bg="white")
    message_label.pack(pady=5)

    btn_row = tk.Frame(form, bg="white")
    btn_row.pack(fill="x", pady=15)
    save_btn = tk.Button(btn_row, text="Save", bg="white", fg="black", width=12)
    save_btn.pack(side="left", padx=10)

    def save_contact():
        name = name_entry.get().strip()
        contact = contact_entry.get().strip()
        gmail = gmail_entry.get().strip() or None
        address = address_entry.get().strip()
        if not name:
            message_label.config(text="Name is required!", fg="red")
            return
        if not re.match(r"^[A-Za-z\s]+$", name):
            message_label.config(text="Name must contain only alphabets!", fg="red")
            return
        if not contact:
            message_label.config(text="Contact number is required!", fg="red")
            return
        if not re.match(r"^\d{10}$", contact):
            message_label.config(text="Contact must be only 10 DIGITS!", fg="red")
            return
        if gmail and not re.match(r"^[\w\.-]+@gmail\.com$", gmail):
            message_label.config(text="Enter a valid Gmail address!", fg="red")
            return
        conn = sqlite3.connect("contacts_data.db")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL UNIQUE,
                gmail TEXT UNIQUE,
                address TEXT
            );
        """)
        try:
            cur.execute("INSERT INTO contacts (name, contact, gmail, address) VALUES (?, ?, ?, ?)",
                        (name, contact, gmail, address))
            conn.commit()
            message_label.config(text="Contact saved successfully!", fg="green")
        except sqlite3.IntegrityError:
            message_label.config(text="Duplicate contact or Gmail already exists!", fg="red")
        finally:
            conn.close()
    save_btn.config(command=save_contact)