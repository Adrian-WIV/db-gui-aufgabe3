from db import mariadbconnect, sql
from gui import gui_layout

def malguckenwaswird(eingabe, listbox):
    alter = int(eingabe)


    cur, conn = mariadbconnect()

    kunden_liste = sql(cur, alter)

    listbox.delete(0, "end")

    for kunden in kunden_liste:
        listbox.insert("end", f"{kunden.anrede} {kunden.vorname} {kunden.name} {kunden.tel} ({kunden.alter})")



    conn.close()


gui_layout(malguckenwaswird)