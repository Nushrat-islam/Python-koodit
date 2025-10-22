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

if __name__ == "__main__":
    autot = []
    for i in range(1, 11):
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(f"ABC-{i}", huippunopeus))

    kilpailu_kaynnissa = True
    tunti = 0

    while kilpailu_kaynnissa:
        tunti += 1
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False

    print(f"\nKilpailu päättyi {tunti} tunnin jälkeen.\n")
    print(f"{'Rekisteri':<10} {'Huippu':<10} {'Nopeus':<10} {'Matka':<10}")
    print("-" * 45)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<10} {auto.nopeus:<10} {auto.kuljettu_matka:<10.1f}")
