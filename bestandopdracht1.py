def lees_woordenlijst(bestandsnaam):
  SCHEIDER = '='
  woordenlijst = {}

  bestand = open(bestandsnaam)
  for lijn in bestand:
      woordenlijst[lijn.split(SCHEIDER)[0]] = lijn.split(SCHEIDER)[1].replace("\n", "")
  bestand.close()

  return woordenlijst

print(lees_woordenlijst("bestand"))