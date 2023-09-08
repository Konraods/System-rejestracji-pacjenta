path = 'bd.txt'
czlowiek = []
with open(path, 'r+') as f:
    lines = f.readlines()
    for x in lines:
        czlowiek.append(x.split())


def rejestracja():
    email = str(input("Podaj maila: "))
    haslo = str(input("Podaj haslo: "))

    if email == "":
        print("Wypelnij pole email")
    if haslo == "":
        print("Wypelnij pole haslo")
    if email != "" and haslo != "":
        file = open("bd.txt", "a")
        temp = [email, " ", haslo, "\n"]
        for i in range(len(temp)):
            file.write(temp[i])
        file.close()
        print("Zarejestrowano")


def logowanie():
    email = str(input("Podaj maila: "))
    haslo = str(input("Podaj haslo: "))
    temp = 0

    if email == "":
        print("Wypelnij pole email")
    if haslo == "":
        print("Wypelnij pole haslo")
    if email != "" and haslo != "":
        for x in range(len(czlowiek)):
            if email == czlowiek[x][0] and haslo == czlowiek[x][1]:
                temp = 1
                print("Zalogowano")
    if temp != 1:
        print("Niezalogowano")

class Osoba:
    def __init__(self, imie, nazwisko, email, data_urodzenia, telefon, pesel, haslo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.data_urodzenia = data_urodzenia
        self.telefon = telefon
        self.pesel = pesel
        self.haslo = haslo

class Pacjent(Osoba):
    def __init__(self, imie, nazwisko, email, data_urodzenia, telefon, pesel, haslo, historiaWizyt):
        super().__init__(imie, nazwisko, email, data_urodzenia, telefon, pesel, haslo)
        self.historiaWizyt = historiaWizyt


class Lekarz(Osoba):
    def __init__(self, imie, nazwisko, email, data_urodzenia, telefon, pesel, haslo, PWZ, tytul, specjalizacja,
                 dostepnosc):
        super().__init__(imie, nazwisko, email, data_urodzenia, telefon, pesel, haslo)
        self.PWZ = PWZ
        self.tytul = tytul
        self.specjalizacja = specjalizacja
        self.dostepnosc = dostepnosc


print("\nRejestracja")
# rejestracja()
print("\nLogowanie")
#logowanie()

o1 = Pacjent("Jan", "Kolawksi", "2093@gmail.com", "1900-22-12", 930205233, 9090903456, "tajne", None)

print(o1.imie, o1.email)