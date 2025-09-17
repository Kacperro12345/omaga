import random

liczba = random.randint(1,100)
user_input = None

while user_input != liczba:
    user_input = int(input("Zgadnij liczbę od 1 do 100: "))

    if user_input < liczba: print("wieksza liczba")

    elif user_input > liczba: print("mniejsza liczba")

    else: print("zgadles")
