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
    def __init__(self, anrede, vorname, name, tel, alter):
        self.anrede = anrede
        self.vorname = vorname
        self.name = name
        self.tel = tel
        self.alter = alter

#mariadb verbinden
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

    return cur, conn

#db abfrage
def sql(cur, eingabe):

    cur.execute("""SELECT 
  anrede.Anrede, 
  kunden.Vorname, 
  kunden.Name, 
  kunden.Telefon,
  TIMESTAMPDIFF(YEAR, kunden.Geburtsdatum, CURDATE()) AS 'Alter'
FROM kunden
JOIN anrede ON kunden.Anrede = `anrede`.`ID_Anrede`
WHERE TIMESTAMPDIFF(YEAR, kunden.Geburtsdatum, CURDATE()) < ?
""", (eingabe,))
    
    ergebnis = cur.fetchall()

    kunden_liste = []

    for e in ergebnis:
        kunde = User(*e)
        kunden_liste.append(kunde)

    return kunden_liste
