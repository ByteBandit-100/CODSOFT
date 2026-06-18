import sqlite3
import tkinter as tk
import re

def open_update_contact_window():
    form = tk.Toplevel()
    form.title("Update Contact")
    form.geometry("420x350")
    form.configure(bg="white")
    form.resizable(False, False)

    # dropdown menu to seled id
    tk.Label(form, text="Select Contact ID:", bg="white").pack(pady=5)
    id_var = tk.StringVar(form)
    id_var.set("Select...")
    id_dropdown = tk.OptionMenu(form, id_var, "Select...")
    id_dropdown.pack(pady=5)

    tk.Label(form, text="Name:", bg="white").pack()
    name_entry = tk.Entry(form, width=35); name_entry.pack(pady=5)
    tk.Label(form, text="Contact:", bg="white").pack()
    contact_entry = tk.Entry(form, width=35); contact_entry.pack(pady=5)
    tk.Label(form, text="Gmail:", bg="white").pack()
    gmail_entry = tk.Entry(form, width=35); gmail_entry.pack(pady=5)
    tk.Label(form, text="Address:", bg="white").pack()
    address_entry = tk.Entry(form, width=35); address_entry.pack(pady=5)

    message_label = tk.Label(form, text="", bg="white")
    message_label.pack(pady=5)

    conn = sqlite3.connect("contacts_data.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM contacts ORDER BY id ASC")
    ids = [str(row[0]) for row in cur.fetchall()]
    conn.close()

    menu = id_dropdown["menu"]
    menu.delete(0, "end")
    menu.add_command(label="Select...", command=lambda: id_var.set("Select..."))
    for cid in ids:
        menu.add_command(label=cid, command=lambda value=cid: id_var.set(value))

    # load contacts
    def load_contact(*args):
        if id_var.get() == "Select ID ": return
        conn = sqlite3.connect("contacts_data.db")
        cur = conn.cursor()
        cur.execute("SELECT name, contact, gmail, address FROM contacts WHERE id=?", (id_var.get(),))
        record = cur.fetchone()
        conn.close()
        if record:
            name_entry.delete(0, "end"); name_entry.insert(0, record[0])
            contact_entry.delete(0, "end"); contact_entry.insert(0, record[1])
            gmail_entry.delete(0, "end");
            if record[2]: gmail_entry.insert(0, record[2])
            address_entry.delete(0, "end");
            if record[3]: address_entry.insert(0, record[3])

    id_var.trace_add("write", load_contact)
    def update_contact():
        if id_var.get() == "Select...":
            message_label.config(text="Please select a contact ID!", fg="red")
            return

        name = name_entry.get().strip()
        contact = contact_entry.get().strip()
        gmail = gmail_entry.get().strip() or None
        address = address_entry.get().strip()

        # validation
        if not name or not re.match(r"^[A-Za-z\s]+$", name):
            message_label.config(text="Invalid name!", fg="red"); return
        if not contact or not re.match(r"^\d{10}$", contact):
            message_label.config(text="Invalid contact!", fg="red"); return
        if gmail and not re.match(r"^[\w\.-]+@gmail\.com$", gmail):
            message_label.config(text="Invalid Gmail!", fg="red"); return

        try:
            conn = sqlite3.connect("contacts_data.db")
            cur = conn.cursor()
            cur.execute("UPDATE contacts SET name=?, contact=?, gmail=?, address=? WHERE id=?",
                        (name, contact, gmail, address, id_var.get()))
            conn.commit()
            message_label.config(text="Contact updated successfully!", fg="green")
        except sqlite3.IntegrityError:
            message_label.config(text="Duplicate contact/Gmail!", fg="red")
        finally:
            conn.close()

    tk.Button(form, text="Update", command=update_contact).pack(pady=10)
