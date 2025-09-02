luvut = []

while True:
    syote = input("Syötä luku (tai paina Enter lopettaaksesi): ")
    if syote == "":
        break
    try:
        luku = float(syote) 
        luvut.append(luku)
    except ValueError:
        print("Syötä kelvollinen numero!")

luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:")
for luku in luvut[:5]:
    print(luku)
