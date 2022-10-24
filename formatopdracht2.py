SCHERMBREEDTE = 30
HULP_V = 18
woord = "dylàn k"

print("+" + SCHERMBREEDTE*"-" + "+")
print("| Je gekozen woord: " + " "*(SCHERMBREEDTE - HULP_V - len(woord) - 3) + " {:} |".format(woord))
print("+" + SCHERMBREEDTE*"-" + "+")
