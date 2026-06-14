import tkinter as tk
from modules import imgLoad

def add_hover_effect(widget, hover_bg="lightblue", hover_fg="black", normal_bg="white", normal_fg="black"):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg, fg=hover_fg))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg, fg=normal_fg))

def leftSideBar(rt, icons):
    sidebar = tk.Frame(rt, width=200, relief="solid", bg="white")
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
        btn = tk.Button(sidebar,text=text,image=value, compound="left",font=("poppins", 10),relief="flat",bg="white",fg="black",anchor="w",padx=20,pady=8)
        add_hover_effect(btn, hover_bg="#42adf0", hover_fg="white")
        btn.pack(fill="x", pady=2)

def rightSideBar(rt):
    return None

def homeWindow(rt, icons, app_icon):
    label = tk.Label(rt, text=" Contact Book", image=app_icon, bg="white",
                     compound="left", font=("poppins", 17))
    label.pack(side="top")
    leftSideBar(rt, icons)
    rightSideBar(rt)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("650x500")
    root.configure(bg="white")
    app_icon = tk.PhotoImage(file="./images/contact1.png")
    root.iconphoto(False, app_icon)

    icons = {
        "dashboard": imgLoad.load_png("./images/home.png", (24, 24), master=root),
        "add_contact": imgLoad.load_png("./images/add-user.png", (24, 24), master=root),
        "view": imgLoad.load_png("./images/list.png", (24, 24), master=root),
        "search": imgLoad.load_png("./images/search.png", (24, 24), master=root),
        "update": imgLoad.load_png("./images/update.png", (24, 24), master=root),
        "delete": imgLoad.load_png("./images/bin.png", (24, 24), master=root),
        "exit": imgLoad.load_png("./images/exit.png", (24, 24), master=root),
    }

    homeWindow(root, icons, app_icon)
    root.mainloop()
