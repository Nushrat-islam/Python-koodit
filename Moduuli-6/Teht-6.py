import math

def pizza_yksikkohinta(halkaisija_cm, hinta_euroa):
    sade_m = halkaisija_cm / 2 / 100
    ala = math.pi * sade_m ** 2
    return hinta_euroa / ala

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (EUR): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (EUR): "))

yks_hinta1 = pizza_yksikkohinta(halkaisija1, hinta1)
yks_hinta2 = pizza_yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yks_hinta1:.2f} EUR/m²")
print(f"Toisen pizzan yksikköhinta: {yks_hinta2:.2f} EUR/m²")

if yks_hinta1 < yks_hinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle.")
