import tkinter as tk

def welcomeWindow(rt):
    # tk.Label(text="Welcome to ContactBook App", justify="center").grid(row=0, column=0)

    label = tk.Label(rt, text="Contact Book", height=10, width=100)
    label.pack()
    label.pack(expand=True, side="top")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("600x400")  #window size
    welcomeWindow(root)
    root.mainloop()