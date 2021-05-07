import os

def wielkosc_plikow(sciezka_glowna):
    wielkosc_wszystkich_plikow = os.path.getsize(sciezka_glowna)

    for kazdy_folder in os.listdir(sciezka_glowna):
        sciezka_konkretnego_pliku = os.path.join(sciezka_glowna, kazdy_folder)
        
        if os.path.isfile(sciezka_konkretnego_pliku):
            wielkosc_wszystkich_plikow = wielkosc_wszystkich_plikow + os.path.getsize(sciezka_konkretnego_pliku)

        elif os.path.isdir(sciezka_konkretnego_pliku):
            print('Lokalizacja:',sciezka_konkretnego_pliku,'Liczba plików:', len(os.listdir(sciezka_konkretnego_pliku)))
            wielkosc_wszystkich_plikow = wielkosc_wszystkich_plikow + wielkosc_plikow(sciezka_konkretnego_pliku)

    return wielkosc_wszystkich_plikow

if __name__ == '__main__':
    okresl_folder_lokalizacji_plikow = "C:\SGH_Programowanie\M_Python_programming\Liczby_pierwsze"
    print()
    print("SZCZEGOLOWE DANE O LICZBIE PLIKOW")
    print("Miejsce okupowane przez wszystkie pliki wynosi", wielkosc_plikow(okresl_folder_lokalizacji_plikow), "bajtow")
    print()
    print('Lokalizacja glowna:', okresl_folder_lokalizacji_plikow, 'Liczba plików:', len(os.listdir(okresl_folder_lokalizacji_plikow)))