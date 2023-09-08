import sqlite3
import tkinter as tk
from tkinter import *
import GUI as gui

database = 'db_file'
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pacjent
              (imie TEXT, nazwisko TEXT, email TEXT, data_urodzenia TEXT, telefon TEXT,
              pesel TEXT, haslo TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Lekarz
      (pesel TEXT, haslo TEXT, imie TEXT, nazwisko TEXT, email TEXT, data_urodzenia TEXT, telefon TEXT, PWZ TEXT, specjalizacjia TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Terminy
                (imie TEXT, nazwisko TEXT, dzien TEXT, godzina TEXT)''')
cursor.execute('''Create TABLE IF NOT EXISTS wizytyPacjenta
                (imieP TEXT, nazwiskoP TEXT, imieL TEXT, nazwiskoL TEXT, dzien TEXT, godzina TEXT)''')
conn.commit()

# dodanie kilku przykladowych pacjentow
cursor.execute('''INSERT INTO Pacjent VALUES('Andrzej', 'Konar', 'konar@gmail.com', '12-02-1987', '123456789', '12345678912', 'mocnehaslo')''')
cursor.execute('''INSERT INTO Pacjent VALUES('Jakub', 'Cymbalek', 'kubix@gmail.com', '12-02-1987', '123456789', '12367678912', 'sprtynybyk')''')
cursor.execute('''INSERT INTO Pacjent VALUES('Jakub', 'Nierobek', 'jakubek@gmail.com', '16-03-1999', '123456789', '12345645912', 'sprtynybyk')''')
cursor.execute('''INSERT INTO Pacjent VALUES('Jakub', 'Nierobek', 'jakubek@gmail.com', '16-03-1999', '123456789', '123', '123')''')
# dodanie kilku przykladowych lekarzy
cursor.execute('''INSERT INTO Lekarz VALUES('12345678912', 'haslo', 'Marek', 'Mostowiak', 'kartony@gmai.com', '12-12-1980', '123456789', '0918234', 'Psychiatria')''')
cursor.execute('''INSERT INTO Lekarz VALUES('12323678912', 'haslo2', 'Arek', 'Mostowiak', 'kartony1@gmai.com', '12-12-1980', '122456789', '1918234', 'Psychiatria')''')
cursor.execute('''INSERT INTO Lekarz VALUES('12128078912', 'haslo3', 'Witold', 'Mostowiak', 'kartony2@gmai.com', '12-12-1980', '123433789', '0318234', 'Psychiatria')''')
cursor.execute('''INSERT INTO Lekarz VALUES('234', '234', 'Anna', 'Baran', 'kartony16@gmai.com', '12-12-1980', '123433789', '2218234', 'Okulistyka')''')
#dodanie godzin terminow dla lekarzy
cursor.execute('''INSERT INTO Terminy VALUES('Marek', 'Mostowiak', '04-02-2022', '8:00')''')
cursor.execute('''INSERT INTO Terminy VALUES('Marek', 'Mostowiak', '04-02-2022', '9:00')''')
cursor.execute('''INSERT INTO Terminy VALUES('Marek', 'Mostowiak', '04-02-2022', '10:00')''')
cursor.execute('''INSERT INTO Terminy VALUES('Marek', 'Mostowiak', '04-02-2022', '11:00')''')
cursor.execute('''INSERT INTO Terminy VALUES('Anna', 'Baran', '06-02-2022', '11:00')''')
cursor.execute('''INSERT INTO Terminy VALUES('Anna', 'Baran', '10-02-2022', '11:00')''')
#dodanie wizyt pacjenta
cursor.execute('''INSERT INTO wizytyPacjenta VALUES('Jakub', 'Nierobek', 'Arek', 'mostowiak', '20-02-2022', '9:00')''')
cursor.execute('''INSERT INTO wizytyPacjenta VALUES('Jakub', 'Nierobek', 'Arek', 'mostowiak', '22-02-2022', '10:00')''')



def logowaniePacjent(p_logowanie, p_haslo):
    #logowanie
    global a
    y = cursor.execute('''SELECT pesel, haslo FROM Pacjent WHERE pesel = ? AND haslo = ?;''', [p_logowanie, p_haslo])
    row = cursor.fetchall()
    if row != []:
        print('Logowanie poprawne')
        z = cursor.execute('''SELECT imie, nazwisko FROM Pacjent WHERE pesel = ? AND haslo = ?;''', [p_logowanie, p_haslo])
        global dane_pacjenta
        dane_pacjenta = list(z)
        a = 1
    else:
        a = 0
        print('Dane logowanie niepoprawne')

def set_flag_logowanie():
    return a

def set_flag_logowanie_lekarz():
    return a

def rezerwacja(dane):
    #rezerwacja
    x = cursor.execute('''Select imie, nazwisko FROM Lekarz where specjalizacjia = ?''', [dane])
    global lista
    lista = list(x)
    for i in lista:
        gui.lekarz.insert(lista.index(i)+1, i)

def rezerwacja1(dane):
    y = cursor.execute('''SELECT dzien, godzina FROM Terminy where imie = ? and nazwisko = ? ''', [dane[0], dane[1]])
    global lista1, imie_lekarza, nazwisko_lekarza
    imie_lekarza = dane[0]
    nazwisko_lekarza = dane[1]
    lista1 = list(y)
    for i in lista1:
        gui.terminy.insert(lista1.index(i)+1, i)

def zapisanie_wizyty(dane):
    x = cursor.execute('''INSERT INTO wizytyPacjenta VALUES(?, ?, ?, ?, ?, ?)''', [dane_pacjenta[0][0], dane_pacjenta[0][1], imie_lekarza, nazwisko_lekarza, dane[0], dane[1]])
    cursor.execute('''DELETE FROM TERMINY WHERE imie = ? AND nazwisko = ? AND dzien = ? AND godzina = ?''', [imie_lekarza, nazwisko_lekarza, dane[0], dane[1]])
    conn.commit()

def anulowanieWizyty(dane):
    cursor.execute('''DELETE FROM wizytyPacjenta WHERE imieL = ? AND nazwiskoL = ? AND dzien = ? AND godzina = ?''', [dane[0], dane[1], dane[2], dane[3]])
    conn.commit()

def rejestracjaPacjent(z1, z2, z3, z4, z5, z6, z7):
    y = cursor.execute('''SELECT pesel FROM Pacjent WHERE pesel = ?;''', [z1])
    row = cursor.fetchall()
    if row == []:
        cursor.execute('''INSERT INTO Pacjent VALUES(?, ?, ?, ?, ?, ?, ?)''', (z3, z4, z5, z6, z7, z1, z2))
        print('Rejestracja zakonczona prawidlowo')
        conn.commit()
    else:
        print('niepoprawny pesel')

def rejestracjaLekarz(y1, y2, y3, y4, y5, y6, y7, y8, y9):
    y = cursor.execute('''SELECT pesel FROM Lekarz WHERE pesel = ?;''', [y1])
    row = cursor.fetchall()
    if row == []:
        cursor.execute('''INSERT INTO Lekarz VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', [y1, y2, y3, y4, y5, y6, y7, y8, y9])
        print('Rejestracja zakonczona prawidlowo')
        conn.commit()
    else:
        print('Niepoprawne dane')


def logowanieLekarz(login, haslo):
    global a
    y = cursor.execute('''SELECT pesel, haslo FROM Lekarz WHERE pesel = ? AND haslo = ?;''', [login, haslo])
    row = cursor.fetchall()
    if row != []:
        print('Logowanie poprawne')
        z = cursor.execute('''SELECT imie, nazwisko FROM Lekarz WHERE pesel = ? AND haslo = ?;''',[login, haslo])
        global dane_lekarza
        dane_lekarza = list(z)
        a = 1
    else:
        print('Dane logowanie niepoprawne')
        a = 0

def wizytyPacjenta():
    x = cursor.execute('''SELECT imieL, nazwiskoL, dzien, godzina FROM wizytyPacjenta WHERE imieP = ? and nazwiskoP = ?''', [dane_pacjenta[0][0], dane_pacjenta[0][1]])
    global listaWizyt
    listaWizyt = list(x)
    for i in range(len(listaWizyt)):
        gui.wizyty.insert(i, listaWizyt[i])

def grafikLekarza():
    x = cursor.execute(
        '''SELECT dzien, godzina FROM Terminy WHERE imie = ? and nazwisko = ?''', [dane_lekarza[0][0], dane_lekarza[0][1]])
    global grafikLekarz
    grafikLekarz = list(x)
    for i in range(len(grafikLekarz)):
        gui.grafik.insert(i, grafikLekarz[i])

def listaPacjentow():
    x = cursor.execute('''SELECT imie, nazwisko FROM Pacjent; ''')
    global pacjenci
    pacjenci = list(x)
    for i in range(len(pacjenci)):
        gui.pacjent.insert(i, pacjenci[i])

def wizytyWybranegoPacjenta(dane):
    x = cursor.execute('''SELECT * FROM wizytyPacjenta where imieP = ? and nazwiskoP = ?''', [dane[0], dane[1]])
    global wizytyWybranego
    wizytyWybranego = list(x)
    for i in wizytyWybranego:
        gui.historia.insert(wizytyWybranego.index(i)+1, i)

# cursor.execute('''SELECT dzien, godzina FROM Terminy WHERE imie = 'Anna' and nazwisko = 'Baran'; ''')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)