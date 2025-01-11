import os
import random
import klasy

def sprawdzza():
    if not os.path.exists("zaszyfrowane"):
        os.mkdir("zaszyfrowane")
    ls1 = []
    for i in os.listdir("zaszyfrowane"):
        z = i.split(sep=".")
        if z[1] == "txt":
            ls1.append(z[0])
    return ls1

def sprawdzod():
    if not os.path.exists("odszyfrowane"):
        os.mkdir("odszyfrowane")
    ls2 = []
    for i in os.listdir("odszyfrowane"):
        z = i.split(sep=".")
        if z[1] == "txt":
            ls2.append(z[0])
    return ls2

def szyfr():
    try:
        plik = open("szyfr.txt")
        plik.close()
    except:
        plik = open("szyfr.txt", "w")
        for i in range(9):
            random.shuffle(klasy.szyfr)
            for n in range(len(klasy.szyfr)):
                plik.write(klasy.szyfr[n]+";")
            plik.write("\n")
        plik.close()
    while True:
        try:
            tab = [["-" for i in range(len(klasy.szyfr))] for i in range(9)]
            a = 0
            plik = open("szyfr.txt")
            for linia in plik:
                z = linia.split(sep=";")
                for i in range(len(z)-1):
                    tab[a][i] = z[i]
                a = a + 1
            return tab
        except:
            plik = open("szyfr.txt", "w")
            for i in range(9):
                random.shuffle(klasy.szyfr)
                for n in range(len(klasy.szyfr)):
                    plik.write(klasy.szyfr[n] + ";")
                plik.write("\n")
            plik.close()