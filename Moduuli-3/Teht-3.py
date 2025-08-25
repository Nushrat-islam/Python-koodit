sukupuoli = input('Oletko nainen vai mies?')
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo: "))

if sukupuoli == 'nainen':
    if hemoglobiiniarvo <=117:
        print("Alhainen hemoglobiiniarvo!")
    
    if 117 <= hemoglobiiniarvo <=175:
        print("Normaali hemoglobiiniarvo!")
    
    if hemoglobiiniarvo >=175:
        print ("Korkea hemoglobiiniarvo!")

elif sukupuoli == 'mies':
    if hemoglobiiniarvo <=134:
        print("Alhainen hemoglobiiniarvo!")
    
    if 134 <= hemoglobiiniarvo <=195:
        print("Normaali hemoglobiiniarvo!")

    if hemoglobiiniarvo >=195:
        print("Korkea hemoglobiiniarvo!")
