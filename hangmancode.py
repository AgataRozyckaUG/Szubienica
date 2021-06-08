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
    '''zapis ruchów gracza'''

    d = {}
    litery = input_gracza
    ruchy_gracza = str(ruchy)
    d[ruchy_gracza] = litery
    with open('ruchy_gracza.json', 'a') as f:
        json.dump(d, f, indent=2)


def podpowiedz():
    print("Jeśli chcesz zobaczyć pierwszą literę, wciśnj p, a jeśli ostatnią, wciśnij o.\n"
          "Możesz też podejrzeć litery, których już próbowałeś, wciskając r.")
    wybor_podp = input().lower()
    if wybor_podp == "p":
        print("Pierwsza litera to: " + slowo[0])
        print(zakodowane_slowo)
    elif wybor_podp == "o":
        print("Ostatnia litera to: " + slowo[-1])
        print(zakodowane_slowo)
    elif wybor_podp == "r":
        print("Tych liter już próbowałeś :" + str(zgadywane_litery))
    else:
        print("Błędna wartość.\n"
              "Rezygnujesz z podpowiedzi? (tak/nie)")
        podp_odp = input()
        if podp_odp == "nie":
            podpowiedz()
        elif podp_odp == "tak":
            pass
        else:
            print("Znów błędna wartość. Wracamy do gry.")

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
    '''kodowanie słowa'''

    zakodowane_slowo = []
    for i in range(len(slowo)):
        zakodowane_slowo.append('_')
    return ''.join(zakodowane_slowo)


# główna część programu (main part)
# początek gry


tprint('''Szubienica''', font="cybermedium")
print("Witaj w grze Szubienica!\n"
      "Aby wygrać, musisz odgadnąć zakodowane słowo. Możesz zgadywać pojedyńcze litery lub cały wyraz.\n"
      "Pamiętaj jednak, że odgadywanie całego słowa jest bardziej ryzykowne. Podczas gry możesz skorzystać z jednej podpowiedzi.\n"
      "Podaj swoje imię :)")
imie = input("Moje imię to ")

# wybór kategorii
while True:
    print(imie + ", wybierz kategorię słów: \n"
                 "1 - Zwierzęta\n"
                 "2 - Kolory\n"
                 "3 - Kraje")
    kategoria = input("\nWpisz swój wybór: ")

    if kategoria == '1':
        print("Wybrałeś kategorię Zwierzęta")
        break
    elif kategoria == '2':
        print("Wybrałeś kategorię Kolory")
        break
    elif kategoria == '3':
        print("Wybrałeś kategorię Kraje")
        break
    else:
        print("Wybrałeś niepoprawną wartość. Proszę podać poprawną liczbę.")

# wybór języka
while True:
    print(imie + ", wybierz język: \n"
                 "1 - Polski\n"
                 "2 - Angielski\n"
                 "3 - Japoński")
    jezyk = input("\nWpisz swój wybór: ")

    if jezyk == '1':
        print("Wybrałeś język polski.")
        break
    elif jezyk == '2':
        print("Wybrałeś język angielski.")
        break
    elif jezyk == '3':
        print("Wybrałeś język japoński.")
        break
    else:
        print("Wybrałeś niepoprawną wartość. Proszę podać poprawną liczbę.")

# ładowanie listy słów z pliku
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
    print(imie + " wybierz poziom trudności\n"
                 "1 - łatwy\n"
                 "2 - trudny")
    poziom = int(input("\nWpisz swój wybór: "))

    if poziom == 1 or poziom == 2:
        break
    else:
        print("Proszę wybrać poprawną wartość")

if poziom == 1:
    zycia = 6
elif poziom == 2:
    zycia = 4

zakodowane_slowo = zakodowane_slowo()
lista_liter = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
               'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ż', 'ź',
               'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó',
               'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ż', 'Ź', '#']
print(zakodowane_slowo)
print("Pamiętaj, jeśli chcesz otrzymać podpowiedź, wpisz #")

zagadka = list(zakodowane_slowo)

while zycia > 0:
    if ''.join(zagadka) == slowo:
        print(colored("Gratulacje, udało ci się!", 'green'))
        if poziom == 1:
            wynik = (zycia) * 2
        elif poziom == 2:
            wynik = (zycia) * 5
        print("Zdobywasz " + str(wynik) + " punktów")
        tprint("brawo", font="cybermedium")
        break

    print('Masz jeszcze ' + str(zycia) + ' szans. ')
    input_gracza = input()
    ruchy_gracza()

    if len(input_gracza) == len(slowo):
        if input_gracza.lower() == slowo:
            print("Gratulacje, odgadłeś całe słowo!!")
            if poziom == 1:
                wynik = (zycia) * 2 + 10
            elif poziom == 2:
                wynik = (zycia) * 5 + 15
            print("Zdobywasz " + str(wynik) + " punktów")
            tprint("brawo",font="cybermedium")
            break
        else:
            print("Niestety, nie trafiłeś :(")
            zycia -= 2
            print(pokaz_wisielca(zycia))
            continue

    elif len(input_gracza) > 1 and len(input_gracza) != len(slowo):
        if input_gracza.isalpha():
            print("Możesz wpisać tylko jedną literę!")
            ruchy += 1
        else:
            print("Wpisujesz niedozwolone znaki!")
        continue

    if input_gracza == "":
        print("Musisz wpisać jakąś literę!")
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
            print("Już odgadłeś tę literę!")

    elif input_gracza == "#":
        if liczba_podpowiedzi == 0:
            podpowiedz()
            liczba_podpowiedzi += 1
        else:
            print("Już skorzystałeś z podpowiedzi ;)")

    elif input_gracza.lower() not in slowo and len(input_gracza) == 1:
        if input_gracza.lower() not in zgadywane_litery:
            print(colored('Źle!', 'red'))
            zgadywane_litery.append(input_gracza.lower())
            ruchy += 1
            zycia -= 1
            print(pokaz_wisielca(zycia))
        else:
            print("Już próbowałeś tej litery!")

if zycia == 0:
    print(colored('Nie masz już szans :( Koniec gry.', 'red'))
    tprint("RIP", font="cybermedium")
    quit()

infoimie = [imie]
infowynik = [wynik]
zapisz_wynik()
while True:
    print("Czy chcesz zobaczyć ranking? (tak/nie)")
    odp = input()
    if odp.lower() == "tak":
        pokaz_ranking()
        quit()
    elif odp.lower() == "nie":
        quit()
    else:
        print('Proszę o podanie odpowiedzi "tak" lub "nie" ')



