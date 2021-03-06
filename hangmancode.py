import json
import csv
import random
import pandas as pd
from art import *
from termcolor import colored

kategoria = 0
jezyk = 0
zycia = 0
ruchy = 1
liczba_podpowiedzi = 0
zgadywane_litery = []
odgadniete_litery = []
def pokaz_wisielca(zycia):
    wisielec = ["""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     //
                   |----|______
                   |          |
                   |__________|
                   """,
              """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     /
                |----|______
                |          |
                |__________|
                """,
                """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |
                |----|______
                |          |
                |__________|
                """,
                """
                --------
                |      |
                |      O
                |     \|
                |      |
                |
                |----|______
                |          |
                |__________|
                """,
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                |----|______
                |          |
                |__________|
                """,
                """
                --------
                |      |
                |      O
                |
                |
                |
                |----|______
                |          |
                |__________|
                """,
                ]
    return wisielec[zycia]


def ruchy_gracza():
    '''zapis ruch??w gracza'''

    d = {}
    litery = input_gracza
    ruchy_gracza = str(ruchy)
    d[ruchy_gracza] = litery
    with open('ruchy_gracza.json', 'a') as f:
        json.dump(d, f, indent=2)


def podpowiedz():
    print("Je??li chcesz zobaczy?? pierwsz?? liter??, wci??nj p, a je??li ostatni??, wci??nij o.\n"
          "Mo??esz te?? podejrze?? litery, kt??rych ju?? pr??bowa??e??, wciskaj??c r.")
    wybor_podp = input().lower()
    if wybor_podp == "p":
        print("Pierwsza litera to: " + slowo[0])
        print(zakodowane_slowo)
    elif wybor_podp == "o":
        print("Ostatnia litera to: " + slowo[-1])
        print(zakodowane_slowo)
    elif wybor_podp == "r":
        print("Tych liter ju?? pr??bowa??e?? :" + str(zgadywane_litery))
    else:
        print("B????dna warto????.\n"
              "Rezygnujesz z podpowiedzi? (tak/nie)")
        podp_odp = input()
        if podp_odp == "nie":
            podpowiedz()
        elif podp_odp == "tak":
            pass
        else:
            print("Zn??w b????dna warto????. Wracamy do gry.")

def zapisz_wynik():
    f = open('Ranking.csv', 'a')
    writer = csv.writer(f)
    for w in range (1):
        writer.writerow([infoimie[w], infowynik[w]])
    f.close()


def pokaz_ranking():
    df = pd.read_csv("Ranking.csv", delimiter =',')
    sorted_df = df.sort_values(by=["Wynik"], ascending=False)
    print(sorted_df)

def zakodowane_slowo():
    '''kodowanie s??owa'''

    zakodowane_slowo = []
    for i in range(len(slowo)):
        zakodowane_slowo.append('_')
    return ''.join(zakodowane_slowo)


# g????wna cz?????? programu (main part)
# pocz??tek gry


tprint('''Szubienica''', font="cybermedium")
print("Witaj w grze Szubienica!\n"
      "Aby wygra??, musisz odgadn???? zakodowane s??owo. Mo??esz zgadywa?? pojedy??cze litery lub ca??y wyraz.\n"
      "Pami??taj jednak, ??e odgadywanie ca??ego s??owa jest bardziej ryzykowne. Podczas gry mo??esz skorzysta?? z jednej podpowiedzi.\n"
      "Podaj swoje imi?? :)")
imie = input("Moje imi?? to ")

# wyb??r kategorii
while True:
    print(imie + ", wybierz kategori?? s????w: \n"
                 "1 - Zwierz??ta\n"
                 "2 - Kolory\n"
                 "3 - Kraje")
    kategoria = input("\nWpisz sw??j wyb??r: ")

    if kategoria == '1':
        print("Wybra??e?? kategori?? Zwierz??ta")
        break
    elif kategoria == '2':
        print("Wybra??e?? kategori?? Kolory")
        break
    elif kategoria == '3':
        print("Wybra??e?? kategori?? Kraje")
        break
    else:
        print("Wybra??e?? niepoprawn?? warto????. Prosz?? poda?? poprawn?? liczb??.")

# wyb??r j??zyka
while True:
    print(imie + ", wybierz j??zyk: \n"
                 "1 - Polski\n"
                 "2 - Angielski\n"
                 "3 - Japo??ski")
    jezyk = input("\nWpisz sw??j wyb??r: ")

    if jezyk == '1':
        print("Wybra??e?? j??zyk polski.")
        break
    elif jezyk == '2':
        print("Wybra??e?? j??zyk angielski.")
        break
    elif jezyk == '3':
        print("Wybra??e?? j??zyk japo??ski.")
        break
    else:
        print("Wybra??e?? niepoprawn?? warto????. Prosz?? poda?? poprawn?? liczb??.")

# ??adowanie listy s????w z pliku
if jezyk == '1' and kategoria == '1':
    word_file = open('animalpl.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '1' and kategoria == '2':
    word_file = open('colorpl.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '1' and kategoria == '3':
    word_file = open('krajpl.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '2' and kategoria == '1':
    word_file = open('animaleng.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '2' and kategoria == '2':
    word_file = open('coloreng.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '2' and kategoria == '3':
    word_file = open('krajeng.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '3' and kategoria == '1':
    word_file = open('animaljap.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '3' and kategoria == '2':
    word_file = open('colorjap.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

if jezyk == '3' and kategoria == '3':
    word_file = open('krajjap.txt', 'r+')
    slowo = random.choice(word_file.read().split())
    word_file.close()

while True:
    print(imie + " wybierz poziom trudno??ci\n"
                 "1 - ??atwy\n"
                 "2 - trudny")
    poziom = int(input("\nWpisz sw??j wyb??r: "))

    if poziom == 1 or poziom == 2:
        break
    else:
        print("Prosz?? wybra?? poprawn?? warto????")

if poziom == 1:
    zycia = 6
elif poziom == 2:
    zycia = 4

zakodowane_slowo = zakodowane_slowo()
lista_liter = ['a', '??', 'b', 'c', '??', 'd', 'e', '??', 'f', 'g', 'h', 'i', 'j', 'k', 'l', '??', 'm', 'n', '??', 'o', '??',
               'p', 'q', 'r', 's', '??', 't', 'u', 'v', 'w', 'x', 'y', 'z', '??', '??',
               'A', '??', 'B', 'C', '??', 'D', 'E', '??', 'F', 'G', 'H', 'I', 'J', 'K', 'L', '??', 'M', 'N', '??', 'O', '??',
               'P', 'Q', 'R', 'S', '??', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '??', '??', '#']
print(zakodowane_slowo)
print("Pami??taj, je??li chcesz otrzyma?? podpowied??, wpisz #")

zagadka = list(zakodowane_slowo)

while zycia > 0:
    if ''.join(zagadka) == slowo:
        print(colored("Gratulacje, uda??o ci si??!", 'green'))
        if poziom == 1:
            wynik = (zycia) * 2
        elif poziom == 2:
            wynik = (zycia) * 5
        print("Zdobywasz " + str(wynik) + " punkt??w")
        tprint("brawo", font="cybermedium")
        break

    print('Masz jeszcze ' + str(zycia) + ' szans. ')
    input_gracza = input()
    ruchy_gracza()

    if len(input_gracza) == len(slowo):
        if input_gracza.lower() == slowo:
            print("Gratulacje, odgad??e?? ca??e s??owo!!")
            if poziom == 1:
                wynik = (zycia) * 2 + 10
            elif poziom == 2:
                wynik = (zycia) * 5 + 15
            print("Zdobywasz " + str(wynik) + " punkt??w")
            tprint("brawo",font="cybermedium")
            break
        else:
            print("Niestety, nie trafi??e?? :(")
            zycia -= 2
            print(pokaz_wisielca(zycia))
            continue

    elif len(input_gracza) > 1 and len(input_gracza) != len(slowo):
        if input_gracza.isalpha():
            print("Mo??esz wpisa?? tylko jedn?? liter??!")
            ruchy += 1
        else:
            print("Wpisujesz niedozwolone znaki!")
        continue

    if input_gracza == "":
        print("Musisz wpisa?? jak???? liter??!")
        ruchy += 1
        continue

    if input_gracza not in lista_liter and len(input_gracza) != len(slowo):
        print("To nie litera!")
        ruchy += 1
        continue

    if input_gracza.lower() in slowo:
        if input_gracza.lower() not in odgadniete_litery:
            print(colored("Dobrze!", 'green'))
            ruchy += 1
            for i in range(len(slowo)):
                if list(slowo)[i] == input_gracza.lower():
                    zagadka[i] = input_gracza.lower()
            print(''.join(zagadka))
            odgadniete_litery.append(input_gracza.lower())
        else:
            print("Ju?? odgad??e?? t?? liter??!")

    elif input_gracza == "#":
        if liczba_podpowiedzi == 0:
            podpowiedz()
            liczba_podpowiedzi += 1
        else:
            print("Ju?? skorzysta??e?? z podpowiedzi ;)")

    elif input_gracza.lower() not in slowo and len(input_gracza) == 1:
        if input_gracza.lower() not in zgadywane_litery:
            print(colored('??le!', 'red'))
            zgadywane_litery.append(input_gracza.lower())
            ruchy += 1
            zycia -= 1
            print(pokaz_wisielca(zycia))
        else:
            print("Ju?? pr??bowa??e?? tej litery!")

if zycia == 0:
    print(colored('Nie masz ju?? szans :( Koniec gry.', 'red'))
    tprint("RIP", font="cybermedium")
    quit()

infoimie = [imie]
infowynik = [wynik]
zapisz_wynik()
while True:
    print("Czy chcesz zobaczy?? ranking? (tak/nie)")
    odp = input()
    if odp.lower() == "tak":
        pokaz_ranking()
        quit()
    elif odp.lower() == "nie":
        quit()
    else:
        print('Prosz?? o podanie odpowiedzi "tak" lub "nie" ')



