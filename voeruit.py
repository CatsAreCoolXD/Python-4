kleuren_auto = {"rood": 6, "blauw": 4}
kleuren_auto2 = kleuren_auto
kleuren_auto["rood"] = 3
print("{}: {}".format("rood", kleuren_auto["rood"]))
print("{}: {}".format("rood", kleuren_auto2["rood"]))