import tkinter as tk
from tkinter import ttk, messagebox

def gui_layout():
    root = tk.Tk()
    root.title("Aufgabe3")
    root.geometry("500x500")

    entry = tk.Entry(
        root,
        width = 50,
    )

    suche = ttk.Button(
        root,
        text = "Suche",
        command = suche    
    )

    listbox = tk.Listbox(
        root,
        width = 50,
        height = 30,

    )

    entry.pack()
    suche.pack()
    listbox.pack()

def execute(entry):
    
    eingabe = entry.get().strip()

    if eingabe =="":
        messagebox.showerror("Fehler", "Eingabe darf nicht leer sein")
        return
    
    entry.delete(0, tk.END)

    return eingabe

