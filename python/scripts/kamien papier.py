import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors wins\n")

while True:
    print('Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n')
    choice = int(input('Enter your choice (1-3): '))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺: '))

    if choice == 1:
        choice_name = 'Rock'

    elif choice == 2:
        choice_name = 'Paper'

    else:
        choice_name = 'Scissors'
    
    print("You chose: ", choice_name)
    print("\nNow its Computer's turn...")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'

    elif comp_choice == 2:
        comp_choice_name = 'Paper'

    else:
        comp_choice_name = 'Scissors'

    print("Computer chose: ", comp_choice_name)

    print(f"\n{comp_choice_name} VS {choice_name}!")   

    if choice == comp_choice:
        result = 'Draw'

    elif choice == 1 and comp_choice == 2:
        result = 'Computer'

    elif choice == 2 and comp_choice == 1:
        result = 'Player'

    elif choice == 1 and comp_choice == 3:
        result = 'Player'

    elif choice == 3 and comp_choice == 1:
        result = 'Computer'

    elif choice == 2 and comp_choice == 3:
        result = 'Computer'

    elif choice == 3 and comp_choice == 2:
        result = 'Player'
        
    if result == 'Draw':
        print("<== It's a tie! ==>")

    elif result == 'Player':
        print("<== You win!")
        
    else:
        print("<== Computer wins! ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")    

