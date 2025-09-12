def main():
    nimet = set()

    while True:
        nimi = input("Anna nimi (tyhjä lopettaa): ")

        if nimi == "":
            break

        if nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)

    print("\nSyötetyt nimet:")
    for n in nimet:
        print(n)


if __name__ == "__main__":
    main()
