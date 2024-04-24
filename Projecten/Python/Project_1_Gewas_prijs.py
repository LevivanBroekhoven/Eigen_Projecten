from termcolor import colored
from time import sleep

def Gewas_berekening(hoeveelheid, gewas_waarde):
    totale_waarde = (hoeveelheid * gewas_waarde)
    return totale_waarde

gewassen = {"aardappel": 80, "meloen": 250, "pompoen": 320, "aardbei": 120}

gewas_input = input("Wat is je gewas? ").lower()
hoeveelheid = int(input("Hoeveel gewassen heb je? "))

while True:
    if gewas_input not in gewassen:
        print(colored(f"Gewas niet gevonden, je zei: {gewas_input}", "red"))

    if gewas_input in gewassen:
        print(colored("Goed", "green"))
        sleep(1)
        resultaat = Gewas_berekening(hoeveelheid, gewassen[gewas_input])
        print(colored(f"{resultaat} Goud", "yellow"))
    break

        