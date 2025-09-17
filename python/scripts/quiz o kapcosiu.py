import time




print("=========Mega super sigma quiz kapcosia=========")

while True:
    score = 0
    chance = None
    
    if chance == 0:
        print("No i przegrałeś, taki z ciebie kolega...")
        break

    print("Chcesz super mega quiz o kapcosiu? (Tak/Nie)")
    choice = input().lower()
    if choice == "tak":
        print("Wybierz poziom trudności:")
        for i, lvl in enumerate(["Easy", "Hard", "Sigma"], start=1):
            print(f"{i}. {lvl}")
        difficulty = input().lower()
        if difficulty == "1" or difficulty == "easy":
            chance = 3
        elif difficulty == "2" or difficulty == "hard":
            chance = 2
        elif difficulty == "3" or difficulty == "sigma":
            chance = 1
        print("Pomyślnie wybrano poziom trudności:", difficulty)            

        print("Pytanie pierwsze: Czy mega super kapcos lubi japłuszka?")
        answer1 = input().lower()
        if answer1 == "tak":
            score += 1
            print("Oczywiście ze kapcos lubi japłuszka!")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue

        print("Drugie pytanie: Jaką range ma super mega kapcos w lolu?")
        answer2 = input().lower()
        if answer2 == "bronz" or answer2 == "bronze":
            score += 1
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
            score += 1
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
            score += 1
            print("Tak, niestety siedzi po nocach i niszczy se życie")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue

        print("Pytanie piąte: Ile lat ma super mega kapcos?") 
        answer5 = input()
        if answer5 == "13" or answer5 == "12":
            score += 1
            print("Zgadłeś, kapcos ma 13/12 lat!")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue
        print("Pytanie szóste: Czy super mega kapcos jest mężczyzną?")
        answer6 = input().lower()
        if answer6 == "tak" or answer6 == "sigma":
            score += 1
            print("On jest sigmą! (albo mężczyzną)")
        else:
            chance -= 1
            print("To jest mężczyzną i sigma na raz, a nie baba")
            time.sleep(1)
            if chance == 0:
                continue


        print("Czy kapcos chodzi do szkoły?")
        answer7 = input().lower()
        if answer7 == "nie":
            score +=1
            print("Nie chodzi bo ma hore nuszki")
        else:
            chance -= 1
            print("Nie prawda, taki jesteś kolega i nic o nim nie wiesz :(")
            time.sleep(1)
            if chance == 0:
                continue    
        
        print("Udało ci się, bardzo dobrze znasz mega super kapcosia! Zostały ci", chance, "szanse i zdobyłeś", score,"punktów!")
        break

    else:
        print("A to bajo jajo klocku")
        break
