kaupungit = []

for i in range(5):
    nimi = input(f"Syötä kaupungin {i+1} nimi: ")
    kaupungit.append(nimi)

print("\nSyötetyt kaupungit ovat:")
for kaupunki in kaupungit:
    print(kaupunki)
