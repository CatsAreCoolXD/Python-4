def voeg_woorden_toe(woordenlijst):
    while True:
        woord = input("Welk woord moet toegevoegd worden?\n")
        woordenlijst.append(woord)
        doorgaan = input("Toegevoegd! Wil je verder gaan?(y/n)\n").lower()
        if doorgaan == "n":
            print(woordenlijst)
            break

voeg_woorden_toe([])