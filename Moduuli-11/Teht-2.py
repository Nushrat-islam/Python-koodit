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


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


if __name__ == "__main__":
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    bensa_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(120)
    bensa_auto.kiihdyta(100)

    sahkoauto.kulje(3)
    bensa_auto.kulje(3)

    print(f"Sähköauto {sahkoauto.rekisteritunnus}: {sahkoauto.kuljettu_matka} km ajettu.")
    print(f"Polttomoottoriauto {bensa_auto.rekisteritunnus}: {bensa_auto.kuljettu_matka} km ajettu.")
