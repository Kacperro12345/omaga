import random

row = 0
attempt = 0

while row < 11:
    x = random.randint(2)
    if x == 2:
        row += 1
        attempt += 1
    
    if x != 2:
        row = 0
        attempt += 1

    if row == 10:
        print(f"udalo sie w {attempt} probach")