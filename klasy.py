import os
import random

import szyfr

# Klasa generująca losowy klucz
def generujKlucz():

    # Tworzymy plik
    plik = open("./key.txt", "w")

    # Tworzymy 10 losowych linijek
    for i in range(10):
        alfa = szyfr.szyfr
        random.shuffle(alfa)
        for n in range(len(szyfr.szyfr)):
            plik.write(szyfr.szyfr[n] + ";")
        plik.write("\n")

    plik.close()

# Klasa do odczytywania szyfru
def getKey(numer = None):

    # Sprawdzam, czy istnieje plik z kluczem
    try:
        plik = open("./key.txt")

    # Jeśli nie, to tworzymy nowy
    except:
        generujKlucz()
        plik = open("./key.txt")

    # Tworzymy tabelkę z kluczem
    klucz = [["-" for i in range(len(szyfr.szyfr))] for i in range(10)]

    # Odczytujemy klucz zpliku
    a = 0
    for linia in plik:
        znaki = linia.split(sep=";")
        for i in range(len(znaki) - 1):
            klucz[a][i] = znaki[i]
        a = a + 1

    # Jeśli jest podane, który konkretnie klucz chcemy użyć, zwracamy go, jeśli nie, zwracamy cały klucz
    if numer is not None:
        numer = numer % 10
        return klucz[numer]
    else:
        return klucz

# Funkcja od szyfrowania plików
def szyfruj():

    # Pobieranie klucza od użytkownika
    klucz = input("Podaj numer klucza (liczba całkowita): ")
    klucz = getKey(int(klucz))
    alfa = szyfr.szyfr

    # Pobieranie nazwy pliku
    plik = input("Podaj nazwę pliku, który chcesz zaszyrować: ")

    # Sprawdzenie, czy plik istnieje
    try:
        zaszyfrowany = open("./zaszyfrowany_%s" % plik, "a", encoding="UTF-8")
        plik = open("./%s" % plik, "r", encoding="UTF-8")
    except:
        print("Taki plik nie itsnieje.")
        return

    # Szyfrowanie pliku
    for linia in plik:
        zaszyfrowanaLinia = ""
        # Dla każdego znaku danej linii
        for n in linia:
            # Sprawdzamy, czy istnieje znak w standardowym ciągu znaków
            try:
                index = alfa.index(n)
            except:
                index = -1

            # Jeśli tak, to przypisujemy odpowiedni znak z szyfry, jeśli nie, to pozostawiamy ten znak
            if index != -1:
                zaszyfrowanaLinia += klucz[index]
            else:
                zaszyfrowanaLinia += n
        zaszyfrowany.write(zaszyfrowanaLinia)

    zaszyfrowany.close()
    print("Pomyślnie zaszyfrowano plik!")


def odszyfruj():
    # Pobieranie klucza od użytkownika
    klucz = input("Podaj numer klucza (liczba całkowita): ")
    klucz = getKey(int(klucz))
    alfa = szyfr.szyfr

    # Pobieranie nazwy zafrowanego pliku
    plik = input("Podaj nazwę pliku, który chcesz odszyrować: ")

    # Sprawdzenie, czy plik istnieje
    try:
        odszyfrowany = open("./odszyfrowany_%s" % plik, "a", encoding="UTF-8")
        plik = open("./%s" % plik, "r", encoding="UTF-8")
    except:
        print("Taki plik nie itsnieje.")
        return

    # Szyfrowanie pliku
    for linia in plik:
        odszyfrowanaLinia = ""
        # Dla każdego znaku danej linii
        for n in linia:
            # Sprawdzamy, czy istnieje znak w standardowym ciągu znaków
            try:
                index = klucz.index(n)
            except:
                index = -1

            # Jeśli tak, to przypisujemy odpowiedni znak z szyfry, jeśli nie, to pozostawiamy ten znak
            if index != -1:
                odszyfrowanaLinia += alfa[index]
            else:
                odszyfrowanaLinia += n
        odszyfrowany.write(odszyfrowanaLinia)

    odszyfrowany.close()
    print("Pomyślnie odszyfrowano plik!")