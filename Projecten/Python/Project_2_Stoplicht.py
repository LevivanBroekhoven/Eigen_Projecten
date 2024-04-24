from time import sleep
from termcolor import colored

count = 1

while True:
    while count <= 20:
        print(colored("Rood","red"))
        count += 1
        sleep(1)
    print()

    while count <= 50:
        print(colored("Groen","green"))
        count += 1
        sleep(1)
    print()

    while count <= 60:
        print(colored("Geel","yellow"))#In Geel want termcolor heeft geen oranje
        count += 1
        sleep(1)
    print()
    count = 1