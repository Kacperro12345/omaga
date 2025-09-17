import random
import time

ma_questa = False
przypinka = False

szynka = True
bron = True
zbroja = True
wiedza = False



postacie = ["Szlifierka kątowa Bosch", "Nelania", "Jula", "Kapcos"]

print("=== Mini erpegie kapcosia :3 ===")
print("Wybierz se postać:")

for i, postac in enumerate(postacie, start=1):
    print(f"{i}. {postac}")
character = input().lower()

if character == "szlifierka" or character == "1":
    hp = 120
    attack = 30
    defense = 50
    zabsy = 30
    champ = "szlifierka"
elif character == "nelania" or character == "2" or character == "nela":
    hp = 100
    attack = 60
    defense = 40
    zabsy = 40
    champ = "nelania"
elif character == "jula" or character == "3":
    hp = 50
    attack = 100
    defense = 50
    zabsy = 20
    champ = "jula"
elif character == "kapcos" or character == "sigma" or character == "4":
    hp = 60
    attack = 60
    defense = 60
    zabsy = 50
    champ = "kapcos"
else:
    print("Nie ma takiej postaci, grasz kapcosiem :3")
    hp = 60
    attack = 60
    defense = 60
    zabsy = 50
    champ = "kapcos"

print(f"Twoja postać to: {champ.capitalize()}, masz {hp} zdrowia, {attack} ataku i {defense} obrony")

if hp <= 0:
    print("No i przegrałeś [*]")
    exit()

etap = "walka_zul"

def walka_z_zulem(hp, attack, defense, zabsy):
    enemy_hp = random.randint(50, 150)
    enemy_attack = random.randint(20, 80)
    enemy_defense = random.randint(10, 60)
    print(f"\nSpotkałeś Żula spod biedry proszącego o kase ma on {enemy_hp} zdrowia, {enemy_attack} ataku i {enemy_defense} obrony")

    while hp > 0 and enemy_hp > 0:
        print("\nCo robisz? (1. Atak, 2. Ucieczka, 3. Rozmowa)")
        move = input().lower()

        if move == "1":
            dmg = attack - enemy_defense // 2
            dmg = max(dmg, 10)

            roll = random.randint(1, 7)
            if roll == 7:
                dmg *= 2
                print("\nTrafiłeś Żula w błyszczącą łysinę, x2 obrażenia!")
            elif roll == 3:
                dmg //= 2
                print("\nPotknąłeś się o sznurówkę, zadajesz połowę obrażeń! A mama mówiła wiąż sznurówki")
            elif roll == 1:
                dmg += 10
                print("\nŻula cię obraźił a ty się wkurzyłeś, +10 obrażeń!")

            enemy_hp -= dmg
            print(f"\nZadałeś {dmg} obrażeń, Żulowi pozostało {enemy_hp} zdrowia")

            if enemy_hp <= 0:
                zabsy += 10
                print("Wygrałeś z Żulem, miał przy sobie 10 żabsów, +10 żabsów!")
                return hp, zabsy, "wybor_lokacji"

            time.sleep(1)
            enemy_dmg = enemy_attack - defense // 2
            enemy_dmg = max(min(enemy_dmg, 80), 0)
            hp -= enemy_dmg
            print(f"\nŻul walnął cię szklaną butelką za: {enemy_dmg} obrażeń, twoje zdrowie wynosi {hp}")

            if hp <= 0:
                print("\nŻul cię pokonał, a przy okazji ukradł ci punkty z karty Moja Biedronka i żapsy")
                print("NO I PRZEGRAŁEŚ")
                exit()

        elif move == "2":
            hp -= 20
            print("\nGdy uciekałeś Żula obrzucał cię kamieniami - 20hp")
            return hp, zabsy, "wybor_lokacji"

        elif move == "3":
            print("\nŻul powiedział: Jak mi oddasz żabsy to cie zostawię (Tak/Nie)")
            if input().lower() == "tak":
                zabsy -= 20
                print("\nŻul zabrał ci 20 żabsów")
                return hp, zabsy, "wybor_lokacji"
            else:
                print("\nŻul nie jest usatysfakcjonowany twoją odpowiedzią, będzie z tobą walczył")
                time.sleep(1.5)
                dmg = attack - enemy_defense // 2
                dmg = max(dmg, 10)

                roll = random.randint(1, 10)
                if roll == 7:
                    dmg *= 2
                    print("\nTrafiłeś Żula w błyszczącą łysinę, x2 obrażenia!")
                elif roll == 3:
                    dmg //= 2
                    print("\nPotknąłeś się o sznurówkę, zadajesz połowę obrażeń! A mama mówiła wiąż sznurówki")
                elif roll == 1:
                    dmg += 10
                    print("\nŻula cię obraźił a ty się wkurzyłeś, +10 obrażeń!")

                enemy_hp -= dmg
                print(f"\nZadałeś {dmg} obrażeń, Żula pozostało {enemy_hp} zdrowia")

                if enemy_hp <= 0:
                    print("Wygrałeś z Żulem! Miał przy sobie 10 żabsów, +10 żabsów!")  
                    zabsy += 10  
                    return hp, zabsy, "wybor_lokacji"

                time.sleep(1)
                enemy_dmg = enemy_attack - defense // 2
                enemy_dmg = max(min(enemy_dmg, 80), 0)
                hp -= enemy_dmg
                print(f"\nŻul walnął cię szklaną butelką za: {enemy_dmg} obrażeń, twoje zdrowie wynosi {hp}")

                if hp <= 0:
                    print("\nŻul cię pokonał, a przy okazji ukradł ci punkty z karty Moja Biedronka i żapsy")
                    return hp, zabsy, "wybor_lokacji"
                
while True:
    if etap == "walka_zul":
        hp, zabsy, etap = walka_z_zulem(hp, attack, defense, zabsy)

    elif etap == "wybor_lokacji":
        print("\nGdzie idziesz?")
        print("1. Do biedry na zakupy")
        print("2. Do kościoła pomodlić się za Żula")
        print("3. Do centrum")
        print("4. Sprawdź swoje statystyki")
        choice = input("Wybierz 1/2/3: ")

        if choice == "1":
            while True:
                print("\nGdy wchodzisz do biedry, widzisz przecenę na leczącą szynkę, kwiatka wyglądającego jak broń, zbroje z arbuza i ziutka od questow")
                print("\n1. Kup szynkę (-10 żabsów, +20hp)")
                print("\n2. Kup broń (-25 żabsów, +15 ataku)")
                print("\n3. Kup zbroję (-25 żabsów, +20 obrony)")
                print("\n4. Idź po zadanie")
                print("\n5. Zwróć przypinkę")
                print("\n6. Wyjdź z Biedronki")
                wybor = input("Wybierz 1/2/3/4/5/6: ")

                if wybor == "1":
                    if zabsy >= 10 and szynka == True:
                        zabsy -= 10
                        hp += 20
                        szynka = False
                        print("\nKupiłeś szynkę, -10 żabsów")
                        print(f"Twoje zdrowie wynosi {hp}, masz {zabsy} żabsów")
                    elif szynka == True:
                        print("Masz za mało żabsów")
                    elif szynka == False:
                        print("Szynka się skończyła")    
                    break

                elif wybor == "2":
                    if zabsy >= 25 and bron == True:
                        zabsy -= 25
                        attack += 15
                        bron = False
                        print("\nKupiłeś broń, +15 ataku, - 25 żabsów")
                        print(f"\nMasz teraz {attack} ataku i {zabsy} żabsów")
                    elif bron == True:
                        print("Masz za mało żabsów")
                    elif bron == False:
                        print("Babcie wykupiły kwiatki... znaczy broń")    
                    break

                elif wybor == "3":
                    if zabsy >= 25 and zbroja == True:
                        zabsy -= 25
                        defense += 20
                        zbroja = False
                        print("\nKupiłeś zbroję, +20 obrony, - 25 żabsów")
                        print(f"\nMasz teraz {attack} ataku, {defense} obrony i {zabsy} żabsów")

                elif wybor == "4":
                    print("\nNieznajomy powiedział, że jak przyniesiesz mu Żulowską przypinkę to ci zapłaci, powiedział też że każdy Żul ją ma")
                    ma_questa = True
                    break

                elif wybor == "5":
                    if przypinka and ma_questa:
                        przypinka = False
                        ma_questa = False
                        zabsy += 30
                        print("\nDzięki za przypinkę ziomek, masz 30 żabsów")
                        print(f"Masz {zabsy} żabsów")
                    else:
                        print("Nie masz przypinki i zadania")
                    break

                elif wybor == "6":
                    print("\nWyszedłeś z Biedronki")
                    print(f"\nPo udanych zakupach masz {hp} zdrowia, {attack} ataku i {zabsy} żabsów")
                    break

                else:
                    print("Nie ma takiej opcji")

        elif choice == "2":
            print("\nW kościele na mszy po modlitwie w imieniu Żula on przylatuje jako nawrócony duch i daje ci jego przypinkę i mówi że się nawrócił i przeprasza")
            hp += 10
            przypinka = True
        
        elif choice == "3":
            print("\nW centrum warszawy widzisz: Sprzedawce japuszek, fontanne w której możesz się umyć i ")
            wybierz = input("Co robisz? (Japuszko, Fontanna) ")
            if wybierz().lower() == "japuszko":
                print("\nKupiłeś japuszko od miłego sprzedawcy, +20 hp, -15 żabsów, powiedźiał też że fontanna jest bardzo brudna i trująca")
                hp += 20
                zabsy -= 15
                wiedza = True 

            elif wybierz().lower() == "fontanna":
                print("\nWykąpałeś się w brudnej fontannie zatrułeś się i zgubiłeś 5 żabsów, -10 hp, -5 żabsów")
                print("\nJestem zbyt mało kreatywny i nic wiecęj nie wymyśle do gry :3 (no chyba że dasz jakis pomysł to dodam), ale i tak spoko wyszło")
                print("=======KONIEC==========")
                hp -= 10
                zabsy -= 5
            elif wybierz().lower() == "fontanna" and wiedza == True:
                print("\nJesteś pewien że chcesz się wykąpać w trującej fontannie? (Tak nie)")
                lampa = input().lower()
                if lampa == "tak":
                    print("\nWykąpałeś się w brudnej fontannie zatrułeś się i zgubiłeś 5 żabsów, -10 hp, -5 żabsów")
                    hp -= 10
                    zabsy -= 5
                    print("\nJestem zbyt mało kreatywny i nic wiecęj nie wymyśle do gry :3 (no chyba że dasz jakis pomysł to dodam), ale i tak spoko wyszło")
                    print("=======KONIEC==========")                    

                elif lampa == "nie":
                    print("\nNie wykąpałeś się w brudnej fontannie")
                    time.sleep(2)
                    print("\nJestem zbyt mało kreatywny i nic więcej nie wymyśle do gry :3 (no chyba że dasz jakis pomysł to dodam), ale i tak spoko wyszło")
                    print("=======KONIEC==========")        

        elif choice == "4":
            print(f"\nTwoje statystiki:")
            print(f"Zdrowie: {hp}")
            print(f"Atak: {attack}")
            print(f"Obrona: {defense}")
            print(f"Żabsy: {zabsy}")        
        
    

    
