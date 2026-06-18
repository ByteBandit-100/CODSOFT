import sqlite3
import tkinter as tk

def open_delete_contact_window():
    form = tk.Toplevel()
    form.title("Delete Contact")
    form.geometry("300x220")
    form.configure(bg="white")
    form.resizable(False, False)

    tk.Label(form, text="Select Contact ID:", bg="white").pack(pady=5)
    id_var = tk.StringVar(form)
    id_var.set("Select...")
    id_dropdown = tk.OptionMenu(form, id_var, "Select...")
    id_dropdown.pack(pady=5)

    message_label = tk.Label(form, text="", bg="white")
    message_label.pack(pady=10)

    # load IDs into dropdown
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

    # delete selected contact
    def delete_contact():
        if id_var.get() == "Select...":
            message_label.config(text="Please select an ID!", fg="red")
            return
        try:
            conn = sqlite3.connect("contacts_data.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM contacts WHERE id=?", (id_var.get(),))
            conn.commit()
            message_label.config(text=f"Contact ID {id_var.get()} deleted!", fg="green")
        except Exception as e:
            message_label.config(text=f"Error: {e}", fg="red")
        finally:
            conn.close()

    # drop all contacts
    def drop_all_contacts():
        try:
            conn = sqlite3.connect("contacts_data.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM contacts")
            cur.execute("DELETE FROM sqlite_sequence WHERE name='contacts'")
            conn.commit()
            message_label.config(text="All contacts deleted.", fg="green")
        except Exception as e:
            message_label.config(text=f"Error: {e}", fg="red")
        finally:
            conn.close()

    tk.Button(form, text="Delete Selected", command=delete_contact).pack(pady=5)
    tk.Button(form, text="Delete All Contacts", bg="red", fg="white", command=drop_all_contacts).pack(pady=5)
    tk.Button(form, text="Exit", command=form.destroy).pack(pady=5)
