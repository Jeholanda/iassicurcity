# -*- coding: UTF-8 -*-

from flask import Flask
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

app = Flask(__name__)


@app.route("/")
def home():
    application_window = tk.Tk()
    nome = simpledialog.askstring("IAssicurCity", "Come ti chiami?", parent=application_window)
    # preparo variabili
    oggi = datetime.today()
    giorni = ('Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica')
    mese = switch_demo(oggi.month)
    # chiude popup dopo l'ok
    application_window.destroy()
    application_window.mainloop()
    return f'<h1 style="font-family:calibri;background-color:DodgerBlue;color:white;">IAssicurCity</h1>' \
           f'<h2 style="font-family:calibri;color:DodgerBlue;"><br>Benvenuto a IAssicurCity, {nome}!</h2>' \
           f'<br>Oggi è {giorni[oggi.weekday()]}, {oggi.day} {mese} {oggi.year}.'


def switch_demo(mese):
    switcher = {
        1: "Gennaio",
        2: "Febbraio",
        3: "Maggio",
        4: "Aprile",
        5: "Maggio",
        6: "Giugno",
        7: "Luglio",
        8: "Agosto",
        9: "Settembre",
        10: "Ottobre",
        11: "Novembre",
        12: "Dicembre"
    }
    return switcher.get(mese, "Mese non valido")


if __name__ == "__main__":
    app.run(debug=True)
