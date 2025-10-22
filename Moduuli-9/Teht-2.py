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

if __name__ == "__main__":
    auto = Auto("ABC-123", 142)

    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(f"Nopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

    auto.kiihdyta(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")
