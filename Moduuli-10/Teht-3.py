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

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero + 1}:")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissin numero!")

    def palohalytys(self):
        print("\nPALOHÄLYTYS! Kaikki hissit siirtyvät pohjakerrokseen!")
        for i, hissi in enumerate(self.hissit, 1):
            print(f"\nHissi {i}:")
            hissi.siirry_kerrokseen(hissi.alin)

if __name__ == "__main__":
    talo = Talo(1, 10, 3)
    talo.aja_hissia(0, 7)
    talo.aja_hissia(1, 5)
    talo.palohalytys()
