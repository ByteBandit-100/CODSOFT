import tkinter as tk
from tkinter import ttk
from modules import imgLoad
from modules import add_contact
from modules import update_contacts
from modules import delete_contact
import sqlite3

def load_contacts():
    conn = sqlite3.connect("contacts_data.db")
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact TEXT NOT NULL UNIQUE,
                    gmail TEXT UNIQUE,
                    address TEXT
                );
            """)
    cursor.execute("""
        SELECT id, name, contact, gmail, address
        FROM contacts
        ORDER BY id DESC
    """)
    records = cursor.fetchall()
    conn.close()
    return records

def refresh_table(tree):
    for row in tree.get_children():
        tree.delete(row)
    contact_data = load_contacts()
    for row in contact_data:
        tree.insert("", "end", values=row)

def add_hover_effect(widget, hover_bg="lightblue", hover_fg="black", normal_bg="white", normal_fg="black"):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg, fg=hover_fg))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg, fg=normal_fg))

def leftSideBar(rt, icons):
    sidebar = tk.Frame(rt, width=200, relief="solid", bg="white")
    sidebar.pack(side="left", anchor="center" )

    btn = tk.Button(sidebar, text="Add Contact", image=icons["add_contact"], compound="left", font=("poppins", 10), relief="flat", bg="white",command=add_contact.open_add_contact_window, fg="black", anchor="w", padx=20, pady=8)
    btn.pack(fill="x", pady=2)

    btn = tk.Button(sidebar, text="Update Contact", image=icons["update"], compound="left", font=("poppins", 10),relief="flat", bg="white", command=update_contacts.open_update_contact_window, fg="black", anchor="w", padx=20, pady=8)
    btn.pack(fill="x", pady=2)
    add_hover_effect(btn, hover_bg="#42adf0", hover_fg="white")

    btn = tk.Button(sidebar, text="Delete", image=icons["delete"], compound="left", font=("poppins", 10), relief="flat", bg="white", command=delete_contact.open_delete_contact_window, fg="black", anchor="w", padx=20, pady=8)
    btn.pack(fill="x", pady=2)
    add_hover_effect(btn, hover_bg="#42adf0", hover_fg="white")

def rightSideBar(rt):

    # table for displaying information of contact
    table_frame = tk.Frame(rt, bg="white", bd=1, relief="solid")
    table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # creating treeview
    columns = ("ID", "Name", "Phone", "Email", "Address")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    tree.column("ID", width=50)
    tree.column("Name", width=150)
    tree.column("Phone", width=100)
    tree.column("Email", width=150)
    tree.column("Address", width=200)

    for col in columns:
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True, padx=10, pady=10)
    header_frame = tk.Frame(table_frame, bg="white")
    header_frame.pack(fill="x", padx=10, pady=5)
    tk.Label(header_frame, text="Recent Contacts",font=("poppins", 12, "bold"), bg="white").pack(side="left")
    refresh_btn = tk.Button(header_frame, text="⟳",font=("poppins", 10, "bold"),bg="white", relief="flat",command=lambda: refresh_table(tree))
    refresh_btn.pack(side="right")

    # load data from datavase
    contact_data = load_contacts()
    for row in contact_data:
        tree.insert("", "end", values=row)

    rt.tree = tree
    return tree

def homeWindow(rt, icons, app_icon):
    label = tk.Label(rt, text=" Contact Book", image=app_icon, bg="white",compound="left", font=("poppins", 17))
    label.pack(side="top", pady=5)
    leftSideBar(rt, icons)
    rightSideBar(rt)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("850x550")
    root.configure(bg="white")
    app_icon = tk.PhotoImage(file="./images/contact1.png")
    root.iconphoto(False, app_icon)
    root.resizable(False, False)
    left_icons = {
        "add_contact": imgLoad.load_png("./images/add-user.png", (24, 24), master=root),
        "update": imgLoad.load_png("./images/update.png", (24, 24), master=root),
        "delete": imgLoad.load_png("./images/bin.png", (24, 24), master=root),
    }
    homeWindow(root, left_icons, app_icon)
    root.mainloop()