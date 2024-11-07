from Maze import *
"""
# TEST Exemples d'utilisation :

laby = Maze(4, 4)
print(laby.info())

print(laby)


laby.neighbors = {
    (0, 0): {(1, 0)},
    (0, 1): {(0, 2), (1, 1)},
    (0, 2): {(0, 1), (0, 3)},
    (0, 3): {(0, 2), (1, 3)},
    (1, 0): {(2, 0), (0, 0)},
    (1, 1): {(0, 1), (1, 2)},
    (1, 2): {(1, 1), (2, 2)},
    (1, 3): {(2, 3), (0, 3)},
    (2, 0): {(1, 0), (2, 1), (3, 0)},
    (2, 1): {(2, 0), (2, 2)},
    (2, 2): {(1, 2), (2, 1)},
    (2, 3): {(3, 3), (1, 3)},
    (3, 0): {(3, 1), (2, 0)},
    (3, 1): {(3, 2), (3, 0)},
    (3, 2): {(3, 1)},
    (3, 3): {(2, 3)}
}

print(laby)


# Exemple ajout de mur
laby.neighbors[(1,3)].remove((2,3))
laby.neighbors[(2,3)].remove((1,3))
print(laby)

# Exemple suppression de mur
laby.neighbors[(1, 3)].add((2, 3))
laby.neighbors[(2, 3)].add((1, 3))
print(laby)

# Testons maintenant s’il y a un mur entre deux cellules :
c1 = (1, 3)
c2 = (2, 3)
if c1 in laby.neighbors[c2] and c2 in laby.neighbors[c1]:
    print(f"Il n'y a pas de mur entre {c1} et {c2} car elles sont mutuellement voisines")
elif c1 not in laby.neighbors[c2] and c2 not in laby.neighbors[c1]:
    print(f"Il y a un mur entre {c1} et {c2} car {c1} n'est pas dans le voisinage de {c2} et {c2} n'est pas dans le voisinage de {c1}")
else:
    print(f"Il y a une incohérence de réciprocité des voisinages de {c1} et {c2}")


# Verifie si on peux accéder à une cellule depuis une autre
c1 = (1, 3)
c2 = (2, 3)
if c1 in laby.neighbors[c2] and c2 in laby.neighbors[c1]:
    print(f"{c1} est accessible depuis {c2} et vice-versa")
elif c1 not in laby.neighbors[c2] and c2 not in laby.neighbors[c1]:
    print(f"{c1} n'est pas accessible depuis {c2} et vice-versa")
else:
    print(f"Il y a une incohérence de réciprocité des voisinages de {c1} et {c2}")


# Parcourons La grille en listant les cellules :
L = []
for i in range(laby.height):
    for j in range(laby.width):
        L.append((i,j))
print(f"Liste des cellules : \n{L}")


laby = Maze(5, 5)
print(laby)
"""
laby = Maze(5, 5)

laby.empty()
print("Test Empty: ")
print( laby)

laby.fill()
print("Test Fill: ")
print(laby)

laby.remove_wall((0, 0), (0, 1))
print("Test Remove_wall: ")
print(laby)

laby.empty()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))
print("Test add_wall: ")
print(laby)

print("Test get_walls", laby.get_walls())

print("Test get_contiguous_cells", laby.get_contiguous_cells((0,1)))

print("Test get_reachable_cells",laby.get_reachable_cells((0,1)))


laby2 = Maze.gen_btree(4, 4)
print("Test Arbre binaire")
print(laby2)
print()

laby3 = Maze.gen_sidewinder(4, 4)
print("Test gen_sidewinder: ")
print(laby3)


laby4 = Maze.gen_fusion(15,15)
print("Fusion de chemin")
print(laby4)

laby5 = Maze.gen_exploration(12,12)
print("Gen exploration")
print(laby5)

laby6 = Maze.gen_wilson(11, 10)
print("Test Wilson")
print(laby6)

laby10 = Maze(4,4)
laby10.empty()
print(laby10.overlay({
    (0, 0):'c',
    (0, 1):'o',
    (1, 1):'u',
    (2, 1):'c',
    (2, 2):'o',
    (3, 2):'u',
    (3, 3):'!'}))

laby11 = Maze(4,4)
laby11.empty()
path = {(0, 0): '@',
        (1, 0): '*',
        (1, 1): '*',
        (2, 1): '*',
        (2, 2): '*',
        (3, 2): '*',
        (3, 3): '§'}
print(laby11.overlay(path))


print("Test solution laby gen fusion")
laby = Maze.gen_fusion(15, 15)
solution = laby.solve_dfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

print("Test solution laby gen exploration")
laby = Maze.gen_exploration(15, 15)
solution = laby.solve_bfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

laby11 = Maze.gen_wilson(11, 10)
solution = laby11.solve_bfs((0, 0), (10, 9))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(10, 9)] = 'A'
print ("Test Solution laby gen Wilson")
print(laby11.overlay(str_solution))


laby40 = Maze.gen_wilson(15,15)
solution = laby40.solve_rhr((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print ("Test Solution laby main droite")
print(laby40.overlay(str_solution))

chemincourt = laby40.distance_geo((0,0), (14,14))
print(chemincourt)

chemincourt2 = laby40.distance_man((0,0),(14,14))
print(chemincourt2)
print("ok")