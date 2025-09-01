import random

arvottu_luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku (1–10): "))
    
    if arvaus > arvottu_luku:
        print("Liian suuri arvaus")
    elif arvaus < arvottu_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein!")
        break
