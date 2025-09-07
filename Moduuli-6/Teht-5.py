def karsi_parittomat(luku_lista):
    return [luku for luku in luku_lista if luku % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8]
karsittu_lista = karsi_parittomat(lista)
print("Alkuperäinen lista:", lista)
print("Karsittu lista:", karsittu_lista)
