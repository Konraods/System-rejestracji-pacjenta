import tkinter as tk
from tkinter import *



def po_logowaniu_pacjent():
    visit = tk.Toplevel(root)  # Okno wizyt (dla pacjenta)
    login.destroy()

    visit.title("Obsluga wizyt pacjenta")

    Button(master=visit, text="Umow wizyte").grid(row=0)
    Button(master=visit, text="Odwolaj wizyte").grid(row=1)
    Button(master=visit, text="Przeloz wizyte").grid(row=2)
    Button(master=visit, text="Przegladaj historie wizyt").grid(row=3)


def po_logowaniu_lekarz():
    timetable = tk.Toplevel(root) #Okno grafiku (dla lekarza)
    login.destroy()

    timetable.title("Przeglad grafiku")

    Button(master=timetable, text="Zobacz grafik").grid(row=0)
    Button(master=timetable, text="Przegladaj historie pacjenta").grid(row=1)


def po_rejestracji_pacjent():
    register_pat.destroy()
    root.iconify()
    root.deiconify()


def po_rejestracji_lekarz():
    register_doc.destroy()
    root.iconify()
    root.deiconify()


def logowanie_pacjent():
    login = tk.Toplevel(root)  # Okno logowania
    root.withdraw() #Chowa glowne okno

    login.title("Logowanie dla pacjenta")
    login.rowconfigure([0, 1], minsize=50)
    login.columnconfigure(0, minsize=100)

    Label(master=login, text="PESEL").grid(row=0)
    Label(master=login, text="Haslo").grid(row=1)
    Button(master=login, text="Login", command=po_logowaniu_pacjent).grid(row=3)

    e1 = Entry(master=login)
    e2 = Entry(master=login, show="*")
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


def logowanie_lekarz():
    login = tk.Toplevel(root)  # Okno logowania
    root.withdraw()  # Chowa glowne okno

    login.title("Logowanie dla lekarza")
    login.rowconfigure([0, 1], minsize=50)
    login.columnconfigure(0, minsize=100)

    Label(master=login, text="PESEL").grid(row=0)
    Label(master=login, text="Haslo").grid(row=1)
    Button(master=login, text="Login", command=po_logowaniu_lekarz).grid(row=3)


    e1 = Entry(master=login)
    e2 = Entry(master=login, show="*")
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


def rejestracja_pacjent():
    register_pat = tk.Toplevel(root)  # Okno rejestacji pacjenta
    root.withdraw()  # Chowa glowne okno


    register_pat.title("Rejestracja dla pacjenta")

    Label(master=register_pat, text="PESEL").grid(row=0)
    Label(master=register_pat, text="Haslo").grid(row=1)
    Label(master=register_pat, text="Imie").grid(row=2)
    Label(master=register_pat, text="Nazwisko").grid(row=3)
    Label(master=register_pat, text="Email").grid(row=4)
    Label(master=register_pat, text="Data urodzenia").grid(row=5)
    Label(master=register_pat, text="Telefon").grid(row=6)
    Button(master=register_pat, text="Rejestracja", command=po_rejestracji_pacjent).grid(row=7)

    e1 = Entry(master=register_pat)
    e2 = Entry(master=register_pat, show="*")
    e3 = Entry(master=register_pat)
    e4 = Entry(master=register_pat)
    e5 = Entry(master=register_pat)
    e6 = Entry(master=register_pat)
    e7 = Entry(master=register_pat)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)


def rejestracja_lekarz():
    register_doc = tk.Toplevel(root)  # Okno rejestracji lekarza
    root.withdraw()  # Chowa glowne okno


    register_doc.title("Rejestracja dla lekarza")

    Label(master=register_doc, text="PESEL").grid(row=0)
    Label(master=register_doc, text="Haslo").grid(row=1)
    Label(master=register_doc, text="Imie").grid(row=2)
    Label(master=register_doc, text="Nazwisko").grid(row=3)
    Label(master=register_doc, text="Email").grid(row=4)
    Label(master=register_doc, text="Data urodzenia").grid(row=5)
    Label(master=register_doc, text="Telefon").grid(row=6)
    Label(master=register_doc, text="PWZ").grid(row=7)
    Label(master=register_doc, text="Telefon").grid(row=8)
    Label(master=register_doc, text="Specjalizacja").grid(row=9)
    lb = Listbox(master=register_doc)
    Button(master=register_doc, text="Rejestracja", command=po_rejestracji_lekarz).grid(row=10)

    lb.insert(1, "Epidemiologia")
    lb.insert(2, "Hematologia")
    lb.insert(3, "Kardiologia")
    lb.insert(4, "Okulistyka")
    lb.insert(5, "Pediatria")
    lb.insert(6, "Psychiatria")

    e1 = Entry(master=register_doc)
    e2 = Entry(master=register_doc, show="*")
    e3 = Entry(master=register_doc)
    e4 = Entry(master=register_doc)
    e5 = Entry(master=register_doc)
    e6 = Entry(master=register_doc)
    e7 = Entry(master=register_doc)
    e8 = Entry(master=register_doc)
    e9 = Entry(master=register_doc)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    e9.grid(row=8, column=1)
    lb.grid(row=9, column=1)



root = tk.Tk() #Glowne okno apki

root.title("Aplikacja")
l1 = tk.Label(master=root, text="System rejestracji na wizyte", width=25, height=3)
b1 = tk.Button(master=root, text="Rejestracja - pacjent", command=rejestracja_pacjent, width=15, height=5)
b2 = tk.Button(master=root, text="Logowanie - pacjent", command=logowanie_pacjent, width=15, height=5)
b3 = tk.Button(master=root, text="Rejestracja - lekarz", command=rejestracja_lekarz, width=15, height=5)
b4 = tk.Button(master=root, text="Logowanie - lekarz", command=logowanie_lekarz, width=15, height=5)

l1.grid(row=0, column=1)
b1.grid(row=1, column=0, sticky="nsew")
b2.grid(row=2, column=0, sticky="nsew")
b3.grid(row=1, column=2, sticky="nsew")
b4.grid(row=2, column=2, sticky="nsew")

login = tk.Toplevel(root) #Okno logowania
register_doc = tk.Toplevel(root) #Okno rejestracji lekarza
register_pat = tk.Toplevel(root) #Okno rejestacji pacjenta

login.withdraw()
register_pat.withdraw()
register_doc.withdraw()

root.mainloop()


