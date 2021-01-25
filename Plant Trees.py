"""Mubashir needs your help to plant some trees. He can give you three parameters of the land:

width of the land w
length of the land l
gap between the trees g
You have to create an algorithm to return the number of trees
which can be planted on the edges of the given land
in a symmetrical layout shown below ( unsymmetrical gap = x, tree = o, gap = -):
"""
def plant_trees(w, l, g) -> int:
    if w != l:
        return (0)
    perimiter = (w * 4) - 4
    print("Perimiter: %s" % perimiter)
    lengths = perimiter / (g + 1)
    print("Lengths for gap of %s: %s" % (g, lengths))
    if perimiter % lengths != 0:
        return (0)
    else:
        return lengths

print(plant_trees(3, 3, 3))


