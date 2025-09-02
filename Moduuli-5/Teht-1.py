import random

n = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

for i in range(n):
    heitto = random.randint(1, 6) 
    summa += heitto

print("Arpakuutioiden silmälukujen summa on:", summa)
