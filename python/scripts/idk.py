import time
import random

chars = [
    # Symbole
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '|', '\\',
    
    # Małe litery
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    
    # Duże litery
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    
    # Cyfry
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

target = input("Wpisz halso do zgadniecia")

attempt = ''
tries = 0
guessed = []

while True:
    attempt = ''.join(random.choice(chars) for _ in range(len(target)))
    
    while attempt in guessed:
            attempt = ''.join(random.choice(chars) for _ in range(len(target)))
    
    guessed.append(attempt)
    tries += 1
    print(f"proba {tries}: {attempt}")

    if attempt == target:
          print(f"haslo {target} zgadniete po {tries}")
          break