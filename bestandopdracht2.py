def schrijf_woordenlijst(bestandsnaam, woordenLijst):
    SCHEIDER = '='
    with open(bestandsnaam, "w") as bestand:
        for x in woordenLijst:
            print(woordenLijst[x])
            bestand.write(f"{x}{SCHEIDER}{woordenLijst[x]}\n")

woordenlijst = {"koe": "cow", "schaap": "sheep", "varken": "pig"}
schrijf_woordenlijst("nl-en.wrd", woordenlijst)
