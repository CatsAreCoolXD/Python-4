SCHERMBREEDTE = 35
MAX_WOORD_LENGTE = 22
woord = "vlieger"
woord2 = "horror"
woord3 = "game"

def print_regel(regel):
    print(("> {:" + str(SCHERMBREEDTE-4) + "} <").format(regel))

print((SCHERMBREEDTE)*"-")
print_regel(("Je eerste woord: " + (SCHERMBREEDTE - MAX_WOORD_LENGTE - len(woord))*" "+woord).format(woord))
print_regel(("Je tweede woord: " + (SCHERMBREEDTE - MAX_WOORD_LENGTE - len(woord2))*" "+woord2).format(woord2))
print_regel(("Je derde woord: " + (SCHERMBREEDTE - MAX_WOORD_LENGTE - len(woord3))*" "+woord3).format(woord3))
print((SCHERMBREEDTE)*"-")