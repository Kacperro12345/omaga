zadania = []
while True:
    print("=== MENU ===")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Pokaż zadania")
    print("4. Wyjdź")
    wybor = input("Wybierz opcje 1-4: ")

    if wybor == "1":
        nowe = input("Wpisz se zadanko:")
        zadania.append(nowe)
        print("Dodałeś se zadanko!\n")

    elif wybor == "2":
        if not zadania:
            print("Najpierw wpisz zadanie nierobie\n")
            continue

        print("Wybierz numer zadania do usunięcia: ")
        for i, z in enumerate(zadania, 1):
            print(f"{i}. {z}")
        print()

        try:
            numer = int(input("Numer zadania: "))
            if 1 <= numer <= len(zadania):
                usuniete = zadania.pop(numer - 1)
                print(f"Usunąłeś zadanieL: {usuniete}\n")
            else:
                print("Nie ma takiego numeru idioto\n")
        except ValueError:
            print("Wpisz numer a nie jakies gówno ;-;\n")   


    elif wybor == "3":
        print("Twoje zadania: ")
        for z in zadania:
            print("-", z)
        print()    
    elif wybor == "4":
        print("Nara frajerze")
        break

    else:
        print("Nie ma takiej opcji głąbie")

