import tkinter as tk

def welcomeWindow(rt):
    label = tk.Label(rt, text="Welcome in Contact Book",image=icon,
    compound="left", font=("poppins", 15) )
    label.pack( side="top")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Book")
    icon = tk.PhotoImage(file="./images/contact1.png")
    root.geometry("650x500")  #window size
    root.iconphoto(False,icon)
    welcomeWindow(root)
    root.mainloop()