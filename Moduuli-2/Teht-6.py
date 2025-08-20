import random
kolme_numeroa = [str(random.randint(0, 9)) for _ in range(3)]
kolmenumeroinen_koodi = ''.join(kolme_numeroa)

neljä_numeroa = [str(random.randint(1, 6)) for _ in range(4)]
neljänumeroinen_koodi = ''.join(neljä_numeroa)

print(f"Kolmenumeroinen koodi 0-9: {kolmenumeroinen_koodi}")
print (f"Neljänumeroinen koodi 1-6: {neljänumeroinen_koodi}")