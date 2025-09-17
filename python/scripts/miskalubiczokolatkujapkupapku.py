import time

chance = 3

print("=========Mega super sigma quiz kapcosia=========")

while True:
    if chance == 0:
        print("No i przegrałeś, taki z ciebie kolega...")
        break

    print("Chcesz super mega quiz o kapcosiu? (Tak/Nie)")
    choice = input().lower()
    if choice == "tak":

        print("Pytanie pierwsze: Czy mega super kapcos lubi japuszka?")
        answer1 = input().lower()
        if answer1 == "tak":
            print("Oczywiście ze kapcos lubi japuszka!")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue

        print("Drugie pytanie: Jaką range ma super mega kapcos w lolu?")
        answer2 = input().lower()
        if answer2 == "iron":
            print("Masz racje ale nie miło żę tak pomyślałeś :(")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue

        print("Trzecie pytanie: Czy super mega kapcos ma piesia?")
        answer3 = input().lower()
        if answer3 == "tak" or answer3 == "nelanie":
            print("Tak super mega kapcos ma piesia, Nelanie!")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue

        print("Czwarte pytanie: Czy super mega kapcos siedzi po nocach i gra w lola?")
        answer4 = input().lower()
        if answer4 == "tak" or answer4 == "niestety":
            print("Tak, niestety siedzi po nocach i niszczy se życie")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue

        print("Udało ci się, bardzo dobrze znasz mega super kapcosia! Zostały ci", chance, "szanse.")
        break

    else:
        print("A to bajo jajo klocku")
        break
