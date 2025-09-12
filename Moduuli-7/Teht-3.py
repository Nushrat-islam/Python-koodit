def main():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1 = Syötä uusi lentoasema")
        print("2 = Hae lentoaseman tiedot")
        print("3 = Lopeta")
        valinta = input("Anna valintasi (1-3): ")

        if valinta == "1":
            icao = input("Anna lentoaseman ICAO-koodi: ").upper()
            nimi = input("Anna lentoaseman nimi: ")
            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} tallennettu koodilla {icao}.")

        elif valinta == "2":
            icao = input("Anna haettava ICAO-koodi: ").upper()
            if icao in lentoasemat:
                print(f"Lentoaseman nimi: {lentoasemat[icao]}")
            else:
                print("Lentoasemaa ei löydy.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()
