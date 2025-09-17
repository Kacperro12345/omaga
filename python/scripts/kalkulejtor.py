import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")    

while True:

    clear_console()

    a = float(input("Wpisz pierwszą liczbę: "))
    b = float(input("Wpisz drugą liczbę: "))

    choice = input("Chcesz dodać (d), odjąć (m), pomnożyć (x) czy podzielić (/)")


    if choice == "d":
        print("Wynik dodawania to:", a + b)

    elif choice == "m":
        print("Wynik odejmowania:", a - b)

    elif choice == "x":
        print("Wynik mnożenia:", a * b)

    elif choice == "/":
        print("Wynik dzielenia:", a / b)        

    else:
        print("Nie ma takiej opcji")

    again = input("Chcesz jeszcze raz? (t/n): ")
    if again != "t":
        print("bajo jajo")
        break    