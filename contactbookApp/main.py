import tkinter as tk
from modules import imgLoad

def leftSideBar(rt, icons):
    sidebar = tk.Frame(rt, width=200, relief="solid")
    sidebar.pack(side="left", anchor="center" )

    menu_items = {
        "Dashboard": icons["dashboard"],
        "Add Contact": icons["add_contact"],
        "View Contacts": icons["view"],
        "Search Contact": icons["search"],
        "Update Contact": icons["update"],
        "Delete Contact": icons["delete"],
        "Exit": icons["exit"]
    }

    for text, value in menu_items.items():
        btn = tk.Button(
            sidebar,
            text=text,
            image=value,
            compound="left",
            font=("poppins", 10),

            fg="black",
            bd=0,
            anchor="w",
            padx=20,
            pady=10
        )
        btn.pack(fill="x", pady=2)

def rightSideBar(rt):
    return None

def homeWindow(rt, icons, app_icon):
    label = tk.Label(rt, text=" Contact Book", image=app_icon,
                     compound="left", font=("poppins", 17))
    label.pack(side="top")
    leftSideBar(rt, icons)
    rightSideBar(rt)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("650x500")

    app_icon = tk.PhotoImage(file="./images/contact1.png")
    root.iconphoto(False, app_icon)

    icons = {
        "dashboard": imgLoad.load_png("./images/home.png", (24, 24), master=root),
        "add_contact": imgLoad.load_png("./images/add_contact.png", (24, 24), master=root),
        "view": imgLoad.load_png("./images/list.png", (24, 24), master=root),
        "search": imgLoad.load_png("./images/search.png", (24, 24), master=root),
        "update": imgLoad.load_png("./images/update.png", (24, 24), master=root),
        "delete": imgLoad.load_png("./images/bin.png", (24, 24), master=root),
        "exit": imgLoad.load_png("./images/exit.png", (24, 24), master=root),
    }

    homeWindow(root, icons, app_icon)
    root.mainloop()
