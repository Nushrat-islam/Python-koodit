class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kohde):
        print(f"Siirrytään kerrokseen {kohde}...")
        while self.nykyinen_kerros < kohde:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohde:
            self.kerros_alas()

if __name__ == "__main__":
    h = Hissi(1, 10)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(1)
