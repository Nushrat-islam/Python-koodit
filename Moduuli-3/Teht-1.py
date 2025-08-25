pituus = float(input('Anna kuhan pituus: '))

alamitta = 37

if pituus<alamitta:
    lasku = alamitta - pituus
    print(f"Kuha on alamittainen! Laske kuhan takaisin järveen! {lasku:.1f} cm puuttuu vielä!")

else: 
    print(f"Vautsi mikä kala! Saat ottaa kalan kotiin.")