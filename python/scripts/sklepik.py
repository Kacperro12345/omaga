products = []
money = 100.0

while True:
    print("\n=== SKLEPIK KAPCOSIA ===")
    print("1. Dodaj produkt do sklepu")
    print("2. Pokaż wszystkie produkty")
    print("3. Kup produkt")
    print("4. Pokaż ile masz kasy")
    print("5. Zapisz i wyjdź")

    choice = input("Wybierz opcję (1-5): ")
    
    if choice == "1":
        name = input("Dodaj produkt do sklepu: ")

        try:
            cena = float(input("Podaj cenę produktu: "))
        except ValueError:
            print("Weź wpisz liczbę, a nie jakieś gówno")
            continue

        produkt = {"name": name, "cena": cena}
        products.append(produkt)
        print(f"Dodałeś produkt: {name} za {cena:.2f} zł \n")

    elif choice == "2":
        if not products:
            print("Sklepik pusty jak portfel pod koniec miesiąca\n")
        else:
            print("Produkty w sklepie:")
            for i, produkt in enumerate(products, 1):
                print(f"{i}. {produkt['name']} - {produkt['cena']:.2f} zł")


    if choice == "3":
        if not products:
            print("Nie ma nic do kupienia pustki jak w twojej głowie")
            continue

        bought = input("Co chcesz kupić?")
        for i, produkt in enumerate(products, 1):
            print(f"{i}. {produkt['name']} {produkt['cena']}zł" )
