PawnFirstMove = True

movelist = [(0,-75)]

if PawnFirstMove:
    movelist.append(tuple(map(lambda x : x*2 ,movelist)))

print(movelist)
if abs(movelist[1]) > 75:
    movelist.pop()
    print("First Move allwoed")

print(movelist)
