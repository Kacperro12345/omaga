import random
import time

print('\n<==== Kasyno w domu ====>\n')

# klasa
class Player:
    def __init__(self, bal):
        self.bal = bal

player = Player(100)

games = ['Sloty🎰', 'Ruletka🎯', 'Sprawdź balans📈📉', 'Wyjście🚪 (nie preferowane)']
bettypes = ['Liczba🦄', 'Kolor✅', 'Parzystość✌️']
def slots():

    def roll(): 
        symbols = ['🍒', '🍋', '💎', '💰', '🍊', '🍉', '⭐']

        while True:
            bet = int(input('\nile stawiasz? (0 = odpuść (nie odpuszczaj)'))
            print(f'\nMasz {player.bal} jak coś')

            if bet == 0:
                print("\nDobra decyzja (dla ciebie)")
                return
            
            if bet > player.bal:
                print(f"\nOH HELL NAH MAN masz TYLKO: {player.bal}")

            elif bet < 0:
                print("\nZakłady powyżej zera bolo") 

            else:
                break   

        bell1 = random.choice(symbols)
        bell2 = random.choice(symbols)
        bell3 = random.choice(symbols)
        print("\nLosuje się...")
        time.sleep(2)

        if bell1 == '💰' and bell2 == '💰' and bell3 == '💰':
            jackpot = bet * 50
            player.bal += jackpot
            print("\n<==== 777 JACKPOT 777 ====>")
            time.sleep(1.5)
            print(f"\nTwój status konta wynosi: {player.bal}")  
            
        elif bell1 == bell2 == bell3:
            wygrana = bet * 10
            player.bal += wygrana
            print("\nNo prawie jackpot")
            time.sleep(1)
            print(f"\nWylosowalo się: {bell1}{bell2}{bell3}, twoj status wynosi: {player.bal}")
            
        else:
            player.bal -= bet
            print(f"\nNo i dupa przegrałeś... wylosowalo się: {bell1}{bell2}{bell3} a twój status wynosi: {player.bal} nooo albo bezdomny")

    # glowna petla slotow
    while True:
        print("\nKręcisz czy odchodzisz od slotsow? (k/o)")
        choice = input()

        if choice.lower() == 'k':
            roll()
        elif choice.lower() == 'o':
            print("\nNo i gicior")
            break
        else:
            print("\nA mogłbyś doczytać ślepoto?")

def ruletka():
    def color_number(liczba):
        if liczba == 0:
            return 'g'
        
        elif liczba % 2 == 0:
            return 'b'
        
        else:
            return 'r'
        
    randomnum = random.randint(0, 36)

    for k, nazwa in enumerate(bettypes, start=1):
        print(f"\n{k}. {nazwa}")

    try:
        bet_type = int(input('\nJak chcesz obstawic?'))

        if bet_type == 1:
            bet_num = int(input('\nNa co stawiasz? (Podaj liczbę od 0-36): '))

            if bet_num > 36 or bet_num < 0:
                print("\nA weź doczytaj")
                return           
            
            stawka = int(input('\nIle stawiasz?'))
            print(f'\nMasz {player.bal} jak coś')
            if stawka > player.bal:
                print(f"\nNie masz tyle kast ziutek! Masz TYLKO {player.bal}")
                return

            if bet_num == randomnum:
                win = stawka * 35
                player.bal += win
                print("\n<==== JACKPOT ====>")
                print(f"\nTwoj stan wynosi: {player.bal}")

            else:
                player.bal -= stawka
                print("\nPróbuj dalej i się nie poddawaj (ez)")
                print(f"Wypadło: {randomnum}")
                print(f'\nA tak wogóle to masz {player.bal} kasy (jeszcze)')

        elif bet_type == 2:
            bet_color = str(input('\nJaki kolor wariacie? (r-red, b-black, g-green):'))

            stawka = int(input('\nIle stawiasz bratku?'))
            print(f'\nMasz {player.bal} jak coś')
            if stawka > player.bal:
                print(f'\nNie masz tyle hajsu ziutek, masz tylko: {player.bal}')
                return
            
            wynik_color = color_number(randomnum)

            print(f"\nWypadło: {randomnum} ({wynik_color})")

            if wynik_color == bet_color:
                player.bal += stawka
                print("\nTrafiłeś!🎉")

            else:
                player.bal -= stawka
                print("\nNo trudno, próbuj dalej (ez)")

            print(f"Twoj stan konta: {player.bal}")

        elif bet_type == 3:
            wynik_kolor = color_number(randomnum)
            choice = str(input("\nLiczba parzysta czy nieparzysta? (p/n)"))
            time.sleep(1)
            bet = int(input('\nIle stawiasz wariacie?'))
            print(f'\nMasz {player.bal} jak coś')

            if choice == 'p' and wynik_kolor == 'b':
                wygrana = bet
                player.bal += wygrana
                print("\nTrafiłeś!🎉")
                print(f'\nTwoj stan konta wynosi: {player.bal}')
                
            elif choice == 'n' and (wynik_kolor == 'r' or wynik_kolor == 'g'):
                wygrana = bet
                player.bal += wygrana
                print("\nTrafiłeś!🎉")
                print(f'\nTwoj stan konta wynosi: {player.bal}') 

            else:
                player.bal -= bet
                print("\nPrzegrałeś, ale się nie poddawaj (ez🤑)")    
                print(f"\nA tak przy okazji masz: {player.bal}")               

    except ValueError:
        print("\nWpisz cyfre a nie jakies dziwne coś")

while True:

    print("\nNa co idziesz?")
    for i, name in enumerate(games, start=1):
        print(f"\n{i}. {name}")

    choice = int(input('\nWybierz 1-4: '))

    if choice == 1:
        slots()

    elif choice == 2:
        ruletka()

    elif choice == 3:
        if player.bal > 100:
            print(f"Zarobiłeś (na farcie): {player.bal}📈")

        elif player.bal < 100:
            print(f"No trudno próbuj dalej (ez): {player.bal}")

        else:
            print(f"No zaryzykowałbyś troche bolo: {player.bal}")        

    elif choice == 4:
        print("\nNo nie radze ale jak uważasz...")
        time.sleep(1.5)
        print(f'A tak wogóle to masz: {player.bal} pieniędzy')
    
    else:
        print("\nNo nie ma takiego wyboru")  
