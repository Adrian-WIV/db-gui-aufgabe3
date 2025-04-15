import tkinter as tk
from tkinter import ttk, messagebox

def gui_layout(suche_callback):
    root = tk.Tk()
    root.title("Aufgabe3")
    root.geometry("500x500")

    entry = tk.Entry(
        root,
        width = 50,
    )


    listbox = tk.Listbox(
        root,
        width = 50,
        height = 20,

    )


    def execute():
        
        eingabe = entry.get().strip()

        if eingabe =="":
            messagebox.showerror("Fehler", "Eingabe darf nicht leer sein")
            return
        
        entry.delete(0, tk.END)
        suche_callback(eingabe, listbox)

    suche = ttk.Button(
            root,
            text = "Suche",
            command = execute
        )
    

    entry.pack()
    suche.pack()
    listbox.pack()
    

    root.mainloop()

