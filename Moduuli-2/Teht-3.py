import math
kanta = float(input("Anna kannan pituus: "))
korkeus = float(input("Anna korkeus: "))

piiri = kanta + kanta + korkeus + korkeus
A = kanta * korkeus

print(f"Suorakulmion piiri on {piiri:.2f}")
print(f"Suorakulmion pinta-ala on {A:.2f}")