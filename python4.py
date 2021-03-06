import random
import os
import sys
import time
import turtle
woorden = {}
SCHERMBREEDTE = 80
MAX_WOORD_LENGTE = 40
MAX_WOORD_LENGTE2 = 80
dic_woordenlijst_toevoegen_opslaan = {}


menu = '''
_____________________________________________________________________________
| typ b om een woordenlijst te bekijken.                                    |
| typ f om een nieuwe woorden lijst te maken.                               |
| typ t om woorden toe te voegen aan een dictionary.                        |
| typ q om het overhoor programma te stoppen.                               |
| typ o om te worden overhoord.                                             |
| typ s om de toegevoegde woorden op te slaan.                              |
| typ k om de nog niet opgeslagen dictionary te bekijken.                   |
| typ x om een woord uit een nog niet opgeslagen dictionary te verwijderen. |
| typ 5 om vijf woorden met vertaling toe tevoegen aan de dictionary        |
|___________________________________________________________________________|
'''

def print_regel(regel):
    print(("| {:" + str(SCHERMBREEDTE - 4)+ "} |").format(regel))

def overhoren(woorden):
    gekozen_woord = random.choice(list(woorden.keys()))

    betekenis = input("wat is de vertaling van het woord " + gekozen_woord + " ")
    if betekenis == woorden[gekozen_woord]:
        print("goed zo")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        overhoren(woorden)
    elif betekenis == "q":
        print("doei")
    else:
        print("): Dat is fout")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        overhoren(woorden)

def vijf_woorden_toevoegen(dic_woordenlijst_toevoegen_opslaan):
    for i in range(5):
        input_woord_toevoegen1 = input("Welk woord wil je toevoegen ")
        input_vertaling_toevoegen1 = input("Wat is de vertaling van dit woord ")
        dic_woordenlijst_toevoegen1 = {input_woord_toevoegen1: input_vertaling_toevoegen1}
        dic_woordenlijst_toevoegen_opslaan.update(dic_woordenlijst_toevoegen1)
        #f1 = open(lijst, "a")
        #f1.write( input_woord_toevoegen + "=" + input_woord_toevoegen2 + "\n")
        #f1.close()

    #print(dic__toevoegen1)
    #weet_je_zeker3 = input("Weet je zeker dat je deze vijf woorden wil toevoegen aan de dictionary ")
    #if weet_je_zeker3 == "ja":
        #dic_woordenlijst_toevoegen_opslaan.update(dic_woordenlijst_toevoegen1)
    #else:
        #print("Oke")

def woorden_toevoegen(dic_woordenlijst_toevoegen_opslaan):
    input_woord_toevoegen = input("Welk woord wil je toevoegen druk q om te stoppen ")
    if input_woord_toevoegen == "q":
        print("Oke")
    else:
        input_woord_toevoegen2 = input("Wat is de vertaling van dit woord ")
        print_regel(("Woord: {:^" + str(MAX_WOORD_LENGTE) + "} Vertaling: {:^" + str(MAX_WOORD_LENGTE) + "}").format(input_woord_toevoegen, input_woord_toevoegen2))
        print_regel(("{:^" + str(MAX_WOORD_LENGTE2) + "}").format("Weet je zeker dat je het bovenstaande wil toevoegen: ja of nee "))
        weet_je_zeker = input("Weet je zeker dat je het bovenstaande wil toevoegen: ja of nee ")
        if weet_je_zeker == "nee":
            print("oke")
            woorden_toevoegen(dic_woordenlijst_toevoegen)
        else:
            dic_woordenlijst_toevoegen = {input_woord_toevoegen: input_woord_toevoegen2}
            dic_woordenlijst_toevoegen_opslaan.update(dic_woordenlijst_toevoegen)
            #f1 = open(lijst, "a")
            #f1.write( input_woord_toevoegen + "=" + input_woord_toevoegen2 + "\n")
            #f1.close()
            woorden_toevoegen(dic_woordenlijst_toevoegen_opslaan)

def woorden_toevoegen_opslaan(dic_woordenlijst_toevoegen_opslaan, lijst):
    f_opslaan = open(lijst, "a")
    print(dic_woordenlijst_toevoegen_opslaan)
    input_gebruiker_1 = input("Weet je zekere dat je dit wil toevoegen ja of nee ")
    if input_gebruiker_1 == "ja":
        for key, value in dic_woordenlijst_toevoegen_opslaan.items():
            print(key, value)
            f_opslaan.write(key + "=" + value + "\n")
            dic_woordenlijst_toevoegen_opslaan.clear
    else:
        print("oke")

    f_opslaan.close()

def woorden_verwijderen_dic(dic_woordenlijst_toevoegen_opslaan):
    print(dic_woordenlijst_toevoegen_opslaan)
    welk_woord_verwijderen = input("Welk woord wil je uit de dictionary verwijderen ")
    if welk_woord_verwijderen in dic_woordenlijst_toevoegen_opslaan:
        print(welk_woord_verwijderen)
        weet_je_zeker = input("Weet je zeker dat je dit contact wilt verwijderen ")
        if weet_je_zeker == "ja":
            del dic_woordenlijst_toevoegen_opslaan[welk_woord_verwijderen]
            woorden_verwijderen_dic(dic_woordenlijst_toevoegen_opslaan)
        else:
            woorden_verwijderen_dic(dic_woordenlijst_toevoegen_opslaan)
    else:
        wil_je_ander_verwijderen = input("Dit woord bestaat niet wil je een ander woord verwijderen ja of nee ")
        if wil_je_ander_verwijderen == "nee":
            print("Doei")
        else:
            woorden_verwijderen_dic(dic_woordenlijst_toevoegen_opslaan)

def turtle_tekening():
    turtle.shape("turtle")
    turtle.clearscreen()
    turtle.forward(20)
    turtle.right(90)

def lijst_aanmaken():
    welke_lijst = input("Hoe wil je de nieuwe lijst noemen ")
    weet_je_zeker_aanmaken = input("Weet je zeker dat je de woordenlijst " + welke_lijst + " wilt toe voegen ja of nee ")
    if weet_je_zeker == "ja":
        fr = open(welke_lijst, "x")
    else:
        print("Oke")
def kies_lijst():
    print("NED-EN.wrd")
    lijst_keuze = input("Welke woorden lijst wil je kiezen ")
    return lijst_keuze

def lijst_bekijken(lijst):
    f3 = open(lijst, "r")
    print(f3.read())

def lijst_openen(lijst):
    f = open(lijst)
    woorden = {}
    for line in f:
        woord1, woord2 = line.strip('\n').split('=')
        woorden[woord1] = woord2
    return woorden
    f.close

def runner_code():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu)
    menu_keuze = input("maak een keuze uit het menu hierboven ")
    if menu_keuze == "o":
        lijst = kies_lijst()
        os.system('cls' if os.name == 'nt' else 'clear')
        woorden = lijst_openen(lijst)
        overhoren(woorden)
    elif menu_keuze == "t":
        os.system('cls' if os.name == 'nt' else 'clear')
        woorden_toevoegen(dic_woordenlijst_toevoegen_opslaan)
    elif menu_keuze == "b":
        lijst = kies_lijst()
        os.system('cls' if os.name == 'nt' else 'clear')
        lijst_bekijken(lijst)
    elif menu_keuze == "s":
        lijst = kies_lijst()
        os.system('cls' if os.name == 'nt' else 'clear')
        woorden_toevoegen_opslaan(dic_woordenlijst_toevoegen_opslaan, lijst)
    elif menu_keuze == "q":
        print("Deze optie bestaat nog niet")
    elif menu_keuze == "f":
        lijst_aanmaken()
    elif menu_keuze == "k":
        print(dic_woordenlijst_toevoegen_opslaan)
    elif menu_keuze == "x":
        woorden_verwijderen_dic(dic_woordenlijst_toevoegen_opslaan)
    elif menu_keuze == "e":
        turtle_tekening()
    elif menu_keuze == "5":
        vijf_woorden_toevoegen(dic_woordenlijst_toevoegen_opslaan)
    else:
        print("Dat is geen mogelijke optie ")

    wil_je_doorgaan = input("Druk q om te stoppen of druk y om doortegaan ")
    if wil_je_doorgaan == "q":
        print("doei")
    else:
        print("Nog een keer ")
        runner_code()

runner_code()
