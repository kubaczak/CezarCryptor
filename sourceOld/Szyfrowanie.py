import klasy
import szyfr

print("CezarCryptor 1.0 by kubaczak (23.12.2019)")

ls1 = szyfr.sprawdzza()
ls2 = szyfr.sprawdzod()
tab = szyfr.szyfr()

sr = input("Tajny kod: ")
while True:
    try:
        sr = int(sr)
        if 10 <= sr <= 99:
            sr = str(sr)
            break
        sr = input("Tajny kod: ")
    except:
        sr = input("Tajny kod: ")


tryb = input("Szyfrowanie wiadomośći (1), odszyfrowywanie wiadomości (2), szyfrowanie .txt (3), odszyfrowywanie .txt (4): ")
while True:
    try:
        tryb = int(tryb)
        if tryb == 1 or tryb == 2 or tryb == 3 or tryb == 4:
            break
        tryb = input("Szyfrowanie wiadomośći (1), odszyfrowywanie wiadomości (2), szyfrowanie .txt (3), odszyfrowywanie .txt (4): ")
    except:
        tryb = input("Szyfrowanie wiadomośći (1), odszyfrowywanie wiadomości (2), szyfrowanie .txt (3), odszyfrowywanie .txt (4): ")

if tryb == 1:
    inp = input("Wprowadź tekst do zaszyfrowania: ")
    while inp == "":
        inp = input("Wprowadź tekst do zaszyfrowania: ")
    out = klasy.szyfrowanie(inp, sr, tab)
    print("Twoje zaszyfrowane słowo: ", out, sep="")
elif tryb == 2:
    inp = input("Wprowadź tekst do odszyfrowania: ")
    while inp == "":
        inp = input("Wprowadź tekst do odszyfrowania: ")
    out = klasy.odszyfrowanie(inp, sr, tab)
    print("Twoje odszyfrowane słowo: ", out, sep="")
elif tryb == 3:
    print("Dostępne pliki: ", end="")
    for i in range(len(ls2)):
        print(ls2[i], end=", ")
    print("\n")
    txt = input("Wprowadź nazwę pliku, który chcesz zaszyfrować: ")
    while True:
        try:
            plik = open("odszyfrowane/"+txt+".txt", encoding="utf-8")
            break
        except:
            txt = input("Wprowadź nazwę pliku, który chcesz zaszyfrować: ")
    inp = ""
    for linia in plik:
        inp = inp+linia
    out = klasy.szyfrowanie(inp, sr, tab)
    plik = open("zaszyfrowane/"+txt+".txt", "w", encoding="UTF-8")
    plik.write(out)
    print("Gotowe!")
elif tryb == 4:
    print("Dostępne pliki: ", end="")
    for i in range(len(ls1)):
        print(ls1[i], end=", ")
    print("\n")
    txt = input("Wprowadź nazwę pliku, który chcesz odszyfrować: ")
    while True:
        try:
            plik = open("zaszyfrowane/"+txt+".txt", encoding="UTF-8")
            break
        except:
            txt = input("Wprowadź nazwę pliku, który chcesz odszyfrować: ")
    inp = ""
    for linia in plik:
        inp = inp+linia
    out = klasy.odszyfrowanie(inp, sr, tab)
    plik = open("odszyfrowane/"+txt+".txt", "w", encoding="UTF-8")
    plik.write(out)
    print("Gotowe!")


pause = input("")