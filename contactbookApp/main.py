import tkinter as tk
from modules import imgLoad
from modules import add_contact

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
        if text == "Add Contact":
            btn.config(command=add_contact.open_add_contact_window)
        btn.pack(fill="x", pady=2)

def rightSideBar(rt, rtc_ico):
    #top cards
    cards = tk.Frame(rt, bg="#FFFFFF")
    cards.pack(fill="x", padx=25, pady=10)

    stats = [
        ("Total Contacts", "25"),
        ("Today Added", "3"),
        ("This Month", "18"),
        ("Favorites", "7")
    ]

    for text, value in stats:
        card = tk.Frame(cards, bg="#FFFFFF", width=130, height=100, pady=5, bd=0, relief="solid")
        card.pack(side="left", padx=10)
        card.pack_propagate(False)
        culr="black"
        match text:
            case "Total Contacts": culr="#1b7dfa"
            case "Today Added": culr="#a20cc3"
            case "This Month": culr="#1b7dfa"
            case "Favorites": culr="#a69e1a"
        tk.Label(card,text=text,font=("poppins",9, "bold"),bg="#FFFFFF", fg=culr).pack(pady=2)
        img = rtc_ico[text]
        tk.Label(card, image= img, compound="center",bg="#FFFFFF").pack()

        tk.Label(card,text=value,font=("poppins", 8, "bold"),bg="#FFFFFF").pack()

def homeWindow(rt, icons,rtc_icons, app_icon):
    label = tk.Label(rt, text=" Contact Book", image=app_icon, bg="white",
                     compound="left", font=("poppins", 17))
    label.pack(side="top", pady=5)
    leftSideBar(rt, icons)
    rightSideBar(rt, rtc_icons)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("850x550")
    root.configure(bg="white")
    app_icon = tk.PhotoImage(file="./images/contact1.png")
    root.iconphoto(False, app_icon)
    root.resizable(False, False)
    left_icons = {
        "dashboard": imgLoad.load_png("./images/home.png", (24, 24), master=root),
        "add_contact": imgLoad.load_png("./images/add-user.png", (24, 24), master=root),
        "view": imgLoad.load_png("./images/list.png", (24, 24), master=root),
        "search": imgLoad.load_png("./images/search.png", (24, 24), master=root),
        "update": imgLoad.load_png("./images/update.png", (24, 24), master=root),
        "delete": imgLoad.load_png("./images/bin.png", (24, 24), master=root),
        "exit": imgLoad.load_png("./images/exit.png", (24, 24), master=root),
    }

    right_top_cards_icons = {
        "Total Contacts": imgLoad.load_png("./images/group.png", (32, 32), master=root),
        "Today Added": imgLoad.load_png("./images/calendar_115107.png", (32, 32), master=root),
        "This Month": imgLoad.load_png("./images/icon-icons.png", (32, 32), master=root),
        "Favorites": imgLoad.load_png("./images/star.png", (32, 32), master=root),
    }
    homeWindow(root, left_icons, right_top_cards_icons, app_icon)
    root.mainloop()
