import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<10} {'Huippu':<10} {'Nopeus':<10} {'Matka':<10}")
        print("-" * 45)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<10} {auto.nopeus:<10} {auto.kuljettu_matka:<10.1f}")

    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka >= self.pituus_km for auto in self.autot)

if __name__ == "__main__":
    autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        tunti += 1
        kilpailu.tunti_kuluu()
        if tunti % 10 == 0:
            print(f"\n--- Tunti {tunti} ---")
            kilpailu.tulosta_tilanne()

    print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!")
    kilpailu.tulosta_tilanne()
