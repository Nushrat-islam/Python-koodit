oikea_tunnus = "Meow"
oikea_salasana = "salasana"
yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print(f"Väärä käyttäjätunnus tai salasana. Yrityksiä jäljellä: {max_yritykset - yritykset}")

if yritykset == max_yritykset:
    print("Pääsy evätty")
