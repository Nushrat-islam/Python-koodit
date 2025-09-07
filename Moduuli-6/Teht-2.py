import random

def heita_noppa_tahkoilla(tahkot):
    return random.randint(1, tahkot)

while True:
    try:
        max_silmaluku = int(input("Anna nopan maksimisilmäluku (vähintään 1): "))
        if max_silmaluku >= 1:
            break
        else:
            print("Syötä luku joka on vähintään 1.")
    except ValueError:
        print("Syötä kokonaisluku!")

print(f"Heitetään {max_silmaluku}-tahkoista noppaa kunnes tulee {max_silmaluku}:")

while True:
    silmaluku = heita_noppa_tahkoilla(max_silmaluku)
    print(silmaluku)
    if silmaluku == max_silmaluku:
        break
