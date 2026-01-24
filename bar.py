nome_barman = "pasquale"
costo_drink = 3.5
drink_speciale = "coca cola"

print("benvenuto nel mio bar, per oggi abbiamo solo il nostro drink speciale: la "+drink_speciale)
print("vuoi procedere con l'acquisto?")
risposta1 = input("si o no? ")
risposta1
if risposta1 == "si":
    print("bene! il costo è di "+str(costo_drink)+"€")
else:
    print("sarà per la prossima volta!")
