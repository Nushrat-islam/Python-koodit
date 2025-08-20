import math
leviskät = int(input("Anna leviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))

naulaa_per_leviskä = 20
luotia_per_naula = 32
grammaa_per_luoti = 13.3

kokonaisluodit = (leviskät*naulaa_per_leviskä*luotia_per_naula)+(naulat*luotia_per_naula)+luodit
kokonaisgrammat = kokonaisluodit * grammaa_per_luoti
kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 1000


print(f"Massa nykymittojen mukaan: {kilogrammat} kg ja {grammat:.1f}g")
