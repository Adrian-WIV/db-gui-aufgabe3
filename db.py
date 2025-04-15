# Aufgabe 3:

# Schreiben Sie ein Programm, welches ein Alter vom Benutzer abfragt, und dann alle Kunden ausgibt, 
# welche jünger als dieses Alter sind. Die Liste soll Anrede, Vorname, Name und Telefonnummer enthalten.
# Verwalten Sie die Abfrage in einer Liste, die Objekte enthält. Gestalten Sie eine grafische Oberfläche.

#imports

import mariadb
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


#klasse

class User:
    def __init__(self, anrede, vorname, name, tel):
        self.anrede = anrede
        self.vorname = vorname
        self.name = name
        self.tel = tel

def mariadbconnect():
    try: 
        conn = mariadb.connect(
            user = "Adrian",
            password = "Passwort",
            host = "localhost",
            port = 3306,
            database = "schlumpfshop3"
        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")

    cur = conn.cursor()
