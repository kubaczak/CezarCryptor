from klasy import *

def main():
    # Informacje o wersji
    print("Cezar Cryptor 1.1")

    # Flaga, oznaczająca koniec programu
    end = False

    while not end:
        print("Wybierz, co chcesz zrobić: ")
        print(" 1 - Szyfruj plik")
        print(" 2 - odszyfruj plik")
        print(" 3 - generuj nowy klucz")
        print(" 4 - Zakończ")
        wybor = input("Twój wybór: ")

        match wybor:
            case "1":
                szyfruj()
            case "2":
                odszyfruj()
            case "3":
                generujKlucz()
            # Zakończ program, gdy użytkownik wybierze inną opcję
            case "4":
                end = True

    print("Dziękuję za skorzystanie z programu!")

if __name__ == '__main__':
    main()