luku = int(input("Syötä kokonaisluku: "))

if luku < 2:
    print(f"{luku} ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")
