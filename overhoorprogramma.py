DELETE = 'd'
EXTENSIE = '.wrd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 20
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NE'
STOPPEN = 'q'
TOEVOEGEN = 't'

woordenlijsten = []
inhoudLijsten = {}
woorden = {}

listActive = False

# Bestand inlezen
with open(f"lijsten{EXTENSIE}") as f:
    contentList = {}
    for line in f.readlines():
        if listActive:
            if line == "]\n":
                listActive = False
                contentList = {}
            else:
                if len(line.split(SCHEIDER)) == 2:
                    contentList[line.split(SCHEIDER)[0]] = line.split(SCHEIDER)[1].replace("\n", "")
                    inhoudLijsten[lijst.replace("\n", "")] = contentList
                    woorden[lijst.replace("\n", "")].append(line.split(SCHEIDER)[0])
        if line != "woordenlijsten:\n":
            if "[" in line:
                lijst = ""
                listActive = True
                for letter in line:
                    if letter != "[":
                        lijst = f"{lijst}{letter}"
                    else:
                        woordenlijsten.append(lijst)
                        woorden[lijst] = []


print(inhoudLijsten)

def print_leeg():
    print("\n"*10)

print_leeg()

def print_header():
    print("="*SCHERMBREEDTE)
    print("|"+" "*(SCHERMBREEDTE-2)+"|")

def print_footer():
    print("|" + " " * (SCHERMBREEDTE - 2) + "|")
    print("=" * SCHERMBREEDTE)

def print_regel(inhoud=''):
    print("| {:}".format(inhoud)+(" "*(SCHERMBREEDTE-MAX_WOORDLENGTE-len(inhoud)+16))+" |")



def lees_woordenlijst(bestandsnaam):
    woordenlijst = {}
    with open(bestandsnaam, "r") as f:
        for lijn in f.readlines():
            woordenlijst[lijn.split(SCHEIDER)[0]] = lijn.split(SCHEIDER)[1].replace("\n", "")
    return woordenlijst

def print_menu(text):
    print_header()
    print_regel(text)
    print_regel("")
    print_regel("1. Nieuwe woordenlijst maken")
    print_regel("2. Sla nieuwe woordenlijsten op")
    print_regel("3. Verander van woordenlijst")
    print_regel("4. Woorden toevoegen aan een woordenlijst")
    print_regel("5. Woordenlijst overhoren")
    print_regel("6. Stoppen met het programma")
    print_footer()


def nieuwe_lijst_naam():
    print_header()
    print_regel("Typ de naam van de lijst.")
    print_footer()
    typen = True
    while typen:
        lijstNaam = input()
        if lijstNaam in woordenlijsten:
            print_header()
            print_regel("Deze lijst bestaat al! Typ een andere.")
            print_footer()
        else:
            typen = False
    print_header()
    print_regel("Lijst gemaakt! Klik op enter om door te gaan.")
    print_footer()
    input()
    return lijstNaam

def overhoren(woordenlijst):
    aan_het_overhoren = True
    woordX = 0
    if len(inhoudLijsten[woordenlijst] ) > 1:
        while aan_het_overhoren:
            woord = woorden[woordenlijst][woordX]
            vertaling = inhoudLijsten[woordenlijst][woord]
            if woord != "IGNORE":
                print_header()
                print_regel("Wat is de vertaling van {:}?".format(woord))
                print_footer()
                geraden_vertaling = input().replace("\n", "")
                print_leeg()
                if geraden_vertaling.lower() == vertaling:
                    print_header()
                    print_regel("Heel goed! Klik op enter om door te gaan!")
                    print_footer()
                    input()
                elif geraden_vertaling.lower() == STOPPEN:
                    aan_het_overhoren = False
                elif geraden_vertaling.lower() != vertaling:
                    print_header()
                    print_regel("Helaas! De goede vertaling was {:}!".format(vertaling))
                    print_regel("Klik op enter om door te gaan!")
                    print_footer()
                    r = input()
                    if r.lower() == STOPPEN:
                        aan_het_overhoren = False
                woordX += 1
                print_leeg()
                if woordX == len(woorden[woordenlijst]):
                    aan_het_overhoren = False
    else:
        print_header()
        print_regel("Er zitten geen woorden in die woordenlijst!")
        print_regel("Klik op enter om door te gaan naar het menu!")
        print_footer()
        input()
def print_afscheid():
    print_header()
    print_regel("Tot ziens!")
    print_footer()

def schrijf_woordenlijst(bestandsnaam, woordenlijst):
    nieuweLijst = f"\n{woordenlijst}[\n"
    for item in inhoudLijsten[woordenlijst]:
        vertaling = inhoudLijsten[woordenlijst][item]
        nieuweLijst = f"{nieuweLijst}{item}{SCHEIDER}{vertaling}\n"
    nieuweLijst = f"{nieuweLijst}]"
    with open(bestandsnaam, "a") as f:
        f.write(nieuweLijst)
    print_header()
    print_regel("Opgeslagen!")
    print_footer()
    print_leeg()


def verwijder_woord(woord, woordenlijst):
    print_header()
    print_regel(f"Weet je zeker dat je het woord {woord} wil verwijderen uit {woordenlijst}?(j/n)")
    print_footer()
    vragen = True
    while vragen:
        zeker = input()
        print_leeg()
        if zeker.lower() == "j":
            inhoudLijsten[woordenlijst].pop(woord)
            print_header()
            print_regel("Ik heb het woord {:} verwijdert!".format(woord))
            print_footer()
            with open(f"lijsten{EXTENSIE}", "r+") as f:
                old = f.read()
                lines = old.split("\n")
                ln = 0
                foundWord = False
                goodLijst = False
                for line in lines:
                    ln += 1
                    if woordenlijst in line:
                        goodLijst = True
                    if not foundWord:
                        if woord in line and goodLijst:
                            foundWord = True
                            lines.pop(ln-1)
                ln = 0
                nieuw = ""
                print(lines)
                for regel in lines:
                    nieuw = f"{nieuw}{lines[ln]}\n"
                    ln += 1
                f.seek(0)
                f.truncate(1)
                f.write(nieuw)
            vragen = False
        elif zeker.lower() == "n":
            vragen = False
            print_header()
            print_regel("Is goed! Klik op enter om door te gaan!")
            print_footer()
            input()
        else:
            print_header()
            print_regel("Hmm. Ik heb niet helemaal verstaan wat je wou zeggen. Probeer opnieuw!")
            print_footer()

def voeg_woorden_toe(woordenlijst):
    toevoegen = True
    while toevoegen:
        print_header()
        print_regel("Welk woord wil je toevoegen?")
        print_regel(f"Geselecteerde lijst: {woordenlijst}")
        print_footer()
        woord = input()
        if woord == STOPPEN:
            toevoegen = False
        print_header()
        print_regel("En wat is de vertaling?")
        print_regel(f"Geselecteerde lijst: {woordenlijst}")
        print_footer()
        vertaling = input()
        if vertaling == STOPPEN:
            toevoegen = False
        with open(f"lijsten{EXTENSIE}", "r+") as f:
            inhoudLijsten[woordenlijst][woord] = vertaling
            oud = f.read()
            lines = oud.split("\n")
            nlines = lines
            activeWoordenlijst = False
            ln = 0
            for regel in lines:
                if woordenlijst in regel:
                    activeWoordenlijst = True
                if activeWoordenlijst:
                    nlines.insert(ln+1, f"{woord}={vertaling}")
                    activeWoordenlijst = False
                ln += 1
            ln = 0
            nieuw = ""
            for _ in nlines:
                nieuw = f"{nieuw}{nlines[ln]}\n"
                ln += 1
            f.seek(0)
            f.truncate(0)
            f.write(nieuw)
        haha = True
        while haha:
            print_header()
            print_regel("Wil je nog een woord toevoegen?(j/n)")
            print_footer()
            verder = input()
            if verder == "n":
                toevoegen = False
                haha = False
            elif verder == "j":
                haha = False
            else:
                print_header()
                print_regel("Hmm. Ik heb niet helemaal verstaan wat je wou zeggen. Probeer opnieuw!")
                print_footer()


def reformat_file():
    with open(f"lijsten{EXTENSIE}", "r") as file:
        lijnen = file.readlines()
    with open(f"lijsten{EXTENSIE}", "w") as file:
        for lijn in lijnen:
            if lijn.strip("\n") != "":
                file.write(lijn)


def main():
    r = True
    gekozen_lijst = ""
    no_menu_text = False
    while r:
        if not no_menu_text:
            print_menu("Welkom bij het overhoorprogramma! Selecteer astublieft een optie!")
        no_menu_text = False
        keuze = input()
        if gekozen_lijst != "" or keuze == "3" or keuze == "6":
            if keuze == "1":
                inhoudLijsten[nieuwe_lijst_naam()] = {}
            elif keuze == "2":
                print_header()
                print_regel("Welke woordenlijst wil je opslaan?")
                print_footer()
                keuzelijst = input()
                print_leeg()
                if keuzelijst != STOPPEN:
                    schrijf_woordenlijst(f"lijsten{EXTENSIE}", keuzelijst)
            elif keuze == "3":
                selecteren = True
                print_header()
                print_regel("Welke woordenlijst wil je selecteren? Dit zijn de opties:")
                text = ""
                i = 0
                for woordenlijst in woordenlijsten:
                    text = f"{text}{woordenlijst}"
                    i += 1
                    if len(woordenlijsten)-i > 0:
                        if len(text) > (SCHERMBREEDTE-MAX_WOORDLENGTE+16):
                            text = f"{text} |\n"
                        text = f"{text} - "
                print_regel(text)
                print_footer()
                while selecteren:
                    keuzelijst = input()
                    if keuzelijst != STOPPEN:
                        if keuzelijst in inhoudLijsten:
                            gekozen_lijst = keuzelijst
                            print_header()
                            print_regel("Geselecteerd! Klik op enter om door te gaan.")
                            print_footer()
                            input()
                            selecteren = False
                        else:
                            print_header()
                            print_regel("Deze lijst bestaat niet! Typ een andere.")
                            print_footer()
            elif keuze == "4":
                print_leeg()
                voeg_woorden_toe(gekozen_lijst)
                print_leeg()
            elif keuze == "5":
                overhoren(gekozen_lijst)
            elif keuze == "6":
                reformat_file()
                print_afscheid()
                r = False
            else:
                print_menu("Die optie bestaat niet! Probeer een andere optie!")
                no_menu_text = True
        else:
            print_menu("Je hebt nog geen lijst geselecteerd! Kies optie 3 om er een te selecteren.")
            no_menu_text = True


# Laat een keuzemenu zien
#
# Op zijn minst zijn de volgende keuzes mogelijk:
#  - nieuwe woordenlijst maken
#  - veranderen van woordenlijst
#  - woorden toevoegen aan een woordenlijst
#  - woordenlijsten overhoren
#  - stoppen met het programma
#
# De gebruiker kan vervolgens steeds nieuwe keuzes blijven maken.
#
# Gebruikt: STANDAARD_LIJST, KIES_LIJST, OVERHOREN, TOEVOEGEN, EXTENSIE, STOPPEN
# Parameters: Geen
# Returnwaarde: Geen

main()
