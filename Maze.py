import random
from random import randint


class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """

    def __init__(self, height, width):
        """
        Constructeur d'un labyrinthe de height cellules de haut
        et de width cellules de large
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height = height
        self.width = width
        self.neighbors = {(i, j): set() for i in range(height) for j in range(width)}

    def info(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = "**Informations sur le labyrinthe**\n"
        txt += f"- Dimensions de la grille : {self.height} x {self.width}\n"
        txt += "- Voisinages :\n"
        txt += str(self.neighbors) + "\n"
        valid = True
        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"
        return txt

    def __str__(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += "   ┃" if (0, j + 1) not in self.neighbors[(0, j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def add_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire

    def remove_wall(self, c1, c2):
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 not in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].add(c2)  # on le retire
        if c1 not in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].add(c1)  # on le retire

    def empty(self):
        """
        Supprime tous les murs du labyrinthe.
        """

        for c1 in self.neighbors:
            if c1[0] == 0:
                if isinstance(self.neighbors[c1], set):
                    self.neighbors[c1] = list(self.neighbors[c1])  # Convert set to list if needed
                self.neighbors[c1].append((c1[0], c1[1] + 1))
                self.neighbors[c1].append((c1[0] + 1, c1[1]))
            else:
                if c1[1] == self.width - 1:
                    if isinstance(self.neighbors[c1], set):
                        self.neighbors[c1] = list(self.neighbors[c1])  # Convert set to list if needed
                    self.neighbors[c1].append((c1[0] + 1, c1[1]))
                    self.neighbors[c1].append((c1[0] - 1, c1[1]))
                    self.neighbors[c1].append((c1[0], c1[1] - 1))
                else:
                    if isinstance(self.neighbors[c1], set):
                        self.neighbors[c1] = list(self.neighbors[c1])  # Convert set to list if needed
                    self.neighbors[c1].append((c1[0], c1[1] + 1))
                    self.neighbors[c1].append((c1[0] + 1, c1[1]))
                    self.neighbors[c1].append((c1[0] + 1, c1[1] + 1))
                    self.neighbors[c1].append((c1[0] - 1 + 1, c1[1] - 1))

    def fill(self):
        """
        ajoute tous les murs possibles dans le labyrinthe
        """
        self.neighbors = {(i, j): set() for i in range(self.height) for j in range(self.width)}

    def get_cells(self):
        """

        :return:  retourne la liste de toutes les cellules de la grille du labyrinthe
        """
        L = []  # Initialiser L à vide
        for i in range(self.height):
            for j in range(self.width):
                L.append((i, j))  # Ajouter (i, j) à L
        return L

    def get_walls(self):
        """

        :return: renvoie une liste de tuple contenant les cases entre lesquelles il y a un mur
        """
        L = []
        cells = self.get_cells()
        for cell in cells:
            row, col = cell
            if row + 1 < self.height and (row + 1, col) not in self.neighbors[cell]:
                L.append((cell, (row + 1, col)))
            if col + 1 < self.width and (row, col + 1) not in self.neighbors[cell]:
                L.append((cell, (row, col + 1)))
        return L

    # def get_contiguous_cells(self, c):
    #     """
    #
    #     :param c: cellules choisie
    #     :return: retourne la liste des cellules contigue
    #     """
    #     casse = self.get_cells()
    #     i = 0
    #     L = []
    #     while c != casse[i]:
    #         i += 1
    #     if c[0] == 0:
    #         L.append(casse[i + 1])
    #         L.append(casse[i - 1])
    #         L.append(casse[i + self.width])
    #
    #     else:
    #         if c[1] == self.width - 1:
    #             L.append(casse[i - self.width])
    #             L.append(casse[i - 1])
    #             L.append(casse[i + self.width])
    #         else:
    #             L.append(casse[i - self.width])
    #             L.append(casse[i - 1])
    #             L.append(casse[i + self.width])
    #             L.append(casse[i + 1])
    #     return L

    def get_contiguous_cells(self, c):
        """
        Retourne la liste des cellules contiguës à la cellule c.
        """
        rows, cols = self.height, self.width
        row, col = c

        neighbors = []

        if row > 0:
            neighbors.append((row - 1, col))  # Cellule au-dessus
        if row < rows - 1:
            neighbors.append((row + 1, col))  # Cellule en-dessous
        if col > 0:
            neighbors.append((row, col - 1))  # Cellule à gauche
        if col < cols - 1:
            neighbors.append((row, col + 1))  # Cellule à droite

        return neighbors

    def get_reachable_cells(self, c):
        """
        Retourne la liste des cellules accessibles depuis la cellule c
        :param c: cellule choisie
        :return: liste des cellules accessibles depuis c
        """
        reachable_cells = []
        for cell in self.get_contiguous_cells(c):
            if cell in self.neighbors[c]:
                reachable_cells.append(cell)
        return reachable_cells

    @classmethod
    def gen_btree(cls, h, w):
        maze = Maze(h, w)  # Création d'un objet labyrinthe
        for i in range(h - 1):
            for j in range(w - 1):
                # Supprimer aléatoirement le mur EST ou le mur SUD
                direction = random.choice(['E', 'S'])
                if direction == 'E':
                    maze.remove_wall((i, j), (i, j + 1))  # Supprimer le mur EST
                elif direction == 'S':
                    maze.remove_wall((i, j), (i + 1, j))  # Supprimer le mur SUD

        # Ajout des murs pour la dernière ligne (sauf la dernière cellule)
        for j in range(w - 1):
            maze.remove_wall((h - 1, j), (h - 1, j + 1))  # Supprimer le mur EST

        # Ajout des murs pour la dernière colonne (sauf la dernière cellule)
        for i in range(h - 1):
            maze.remove_wall((i, w - 1), (i + 1, w - 1))  # Supprimer le mur SUD

        return maze


    @classmethod
    def gen_sidewinder(cls, h, w):
        laby = Maze(h, w)
        laby.fill
        for i in range(h - 1):
            sequence = []
            for j in range(w - 1):
                sequence.append((i, j))
                pile_ou_face = randint(0, 1)
                if pile_ou_face == 0:
                    laby.remove_wall((i, j), (i, j + 1))
                else:
                    cell = random.choice(sequence)
                    laby.remove_wall(cell, (cell[0] + 1, cell[1]))
                    sequence = []
            sequence.append((i, j))
            cell = random.choice(sequence)
            laby.remove_wall(cell, (cell[0] + 1, cell[1]))
        for i in range(w - 1):
            laby.remove_wall((h - 1, i), (h - 1, i + 1))
        return laby

    @classmethod
    def gen_fusion(self, h, w) -> object:
        """
        Méthode d'instance qui génère un labyrinthe de `h` lignes et `w` colonnes parfait à l'aide de l’algorithme de fusion de chemins.

        Paramètres:
            `h` (int) : nombre de cases en hauteur du labyrinthe voulu.
            `w` (int) : nombre de cases en largeur du labyrinthe voulu.

        Retour:
            Retourne une instance de `Maze`.
        """
        new_maze = Maze(h, w)
        label = {}
        for i in range(h):
            for j in range(w):
                label[(i, j)] = None
        idx = 1
        for h in range(new_maze.height):
            for w in range(new_maze.width):
                # Ajout des label aux cellules
                label[(h, w)] = idx
                idx += 1
        list_wall = new_maze.get_walls()
        random.shuffle(list_wall)

        for wall in list_wall:
            if label[wall[0]] != label[wall[1]]:
                temp = label[wall[1]]
                for idx in label:
                    if label[idx] == temp:
                        label[idx] = label[wall[0]]
                new_maze.remove_wall(wall[0], wall[1])
        return new_maze

    @classmethod
    def gen_exploration(cls, h, w):
        stack = []
        visited = set()

        x_start = random.randint(0, h - 1)
        y_start = random.randint(0, w - 1)
        stack.append((x_start, y_start))
        visited.add((x_start, y_start))

        maze = cls(h, w)

        while stack:
            x_current, y_current = stack[-1]

            neighbors_unvisited = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x_neighbor, y_neighbor = x_current + dx, y_current + dy
                if 0 <= x_neighbor < h and 0 <= y_neighbor < w and (x_neighbor, y_neighbor) not in visited:
                    neighbors_unvisited.append((x_neighbor, y_neighbor))

            if neighbors_unvisited:
                random.shuffle(neighbors_unvisited)
                x_next, y_next = neighbors_unvisited[0]

                maze.remove_wall((x_current, y_current), (x_next, y_next))
                maze.remove_wall((x_next, y_next), (x_current, y_current))

                stack.append((x_next, y_next))
                visited.add((x_next, y_next))
            else:
                stack.pop()

        return maze

    @classmethod
    def gen_wilson(cls, h, w):
        laby = cls(h, w)
        marque = {i: False for i in laby.get_cells()}
        while not all(marque.values()):
            cellule = random.choice([cell for cell in marque if not marque[cell]])
            marque[cellule] = True
            cellulesMarquage = False
            while not cellulesMarquage:
                cellulesMarquage = True
                for i in marque:
                    if not marque[i]:
                        cellulesMarquage = False
                        break
                celluleNonMarquage = [cell for cell in marque if not marque[cell]]
                if celluleNonMarquage:
                    nextCellule = random.choice(celluleNonMarquage)
                    chemin = [nextCellule]
                    while not marque[nextCellule]:
                        nextCellule = random.choice(laby.get_contiguous_cells(nextCellule))
                        if nextCellule in chemin:
                            chemin = chemin[:chemin.index(nextCellule) + 1]
                        else:
                            chemin.append(nextCellule)
                    for i in chemin:
                        marque[i] = True
                    for j in range(len(chemin) - 1):
                        laby.remove_wall(chemin[j], chemin[j + 1])

        return laby

    def overlay(self, content=None):
        """
        Rendu en mode texte, sur la sortie standard, \
        d'un labyrinthe avec du contenu dans les cellules
        Argument:
            content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
        Retour:
            string
        """
        if content is None:
            content = {(i, j): ' ' for i in range(self.height) for j in range(self.width)}
        else:
            # Python >=3.9
            # content = content | {(i, j): ' ' for i in range(
            #    self.height) for j in range(self.width) if (i,j) not in content}
            # Python <3.9
            new_content = {(i, j): ' ' for i in range(self.height) for j in range(self.width) if (i, j) not in content}
            content = {**content, **new_content}
        txt = r""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += " " + content[(0, j)] + " ┃" if (0, j + 1) not in self.neighbors[(0, j)] else " " + content[
                (0, j)] + "  "
        txt += " " + content[(0, self.width - 1)] + " ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += " " + content[(i + 1, j)] + " ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else " " + content[(i + 1,j)] + "  "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"
        return txt


    def solve_dfs(self,start,stop):
        """
            Méthode d'instance permettant de résoudre le labyrithe en "profondeur"

            Paramètres:
                `start` (tuple) : cellule de départ du chemin
                `stop` (tuple) : celulle d'arrivée du chemin.
            Retour:
                `chemin` (list) : liste des coordonnées correspondant au chemin à parcourir.
            """
        pile = [start]
        pred = {}
        point_marque = {}
        chemin = []
        for i in range(self.height):
            for j in range(self.width):
                point_marque[(i, j)] = False
        point_marque[start] = True
        pred[start] = start
        fin = False
        while False in point_marque.values() and fin == False:
            c = pile.pop(0)
            if c == stop:
                fin = True
            else:
                voisin = self.get_reachable_cells(c)
                for elt in voisin:
                    if point_marque[elt] == False:
                        point_marque[elt] = True
                        pile.insert(0, elt)
                        pred[elt] = c
        c = stop
        while c != start:
            chemin.append(c)
            c = pred[c]
        chemin.append(start)
        return chemin


    def solve_bfs(self,start,stop):
        """
            Méthode d'instance permettant de résoudre le labyrithe en "profondeur"

            Paramètres:
                `start` (tuple) : cellule de départ du chemin
                `stop` (tuple) : celulle d'arrivée du chemin.
            Retour:
                `chemin` (list) : liste des coordonnées correspondant au chemin à parcourir.
            """
        file = [start]
        pred = {}
        point_marque = {}
        chemin = []
        for i in range(self.height):
            for j in range(self.width):
                point_marque[(i, j)] = False
        point_marque[start] = True
        pred[start] = start
        fin = False
        while False in point_marque.values() and fin == False:
            c = file.pop(len(file)-1)
            if c == stop:
                fin = True
            else:
                voisin = self.get_reachable_cells(c)
                for elt in voisin:
                    if point_marque[elt] == False:
                        point_marque[elt] = True
                        file.insert(0, elt)
                        pred[elt] = c
        c = stop
        while c != start:
            chemin.append(c)
            c = pred[c]
        chemin.append(start)
        return chemin

    def solve_rhr(self,start,stop):
        parcours = []
        marque = [start]
        pred = {start : start}
        while marque != []:
            c = marque.pop(0)
            if c == stop :
                marque = []
            voisins = self.get_reachable_cells(c)
            for i in range(len(voisins)):
                if voisins[i] not in marque and voisins[i] != pred[c]:
                    marque.append(voisins[i])
                    pred[voisins[i]] = c
        c = stop
        while c != start:
            parcours.append(c)
            c = pred[c]
        return parcours

    def distance_man(self,c1,c2):
        """
            Méthode d'instance permettant de trouver la plus courte distance de Manhattan entre deux points à l'aide des algorithmes de résolution.
            Paramètres:
                `start` (tuple) : cellule de départ du chemin
                `stop` (tuple) : celulle d'arrivée du chemin.
            Retour:
                `len` (int) : plus courte distance à parcourir.
            """
        return (c2[0] - c1[0]) + (c2[1] - c1[1])


    def distance_geo(self, c1, c2):
        """
        Méthode d'instance permettant de trouver la plus courte distance géographique entre deux points à l'aide des algorithmes de résolution.
        Paramètres:
            `start` (tuple) : cellule de départ du chemin
            `stop` (tuple) : celulle d'arrivée du chemin.
        Retour:
            `len` (int) : plus courte distance à parcourir.
        """
        distanceDfs = self.solve_dfs(c1, c2)
        distanceBfs = self.solve_bfs(c1, c2)
        distanceRhr=self.solve_rhr(c1, c2)
        solution = -1
        if len(distanceDfs) < len(distanceBfs)and len(distanceDfs) < len(distanceRhr):
            solution = len(distanceDfs)
        elif len(distanceBfs) < len(distanceDfs) and len(distanceBfs) < len(distanceRhr):
            solution = len(distanceBfs)
        elif len(distanceRhr)<len(distanceBfs) and len(distanceRhr) < len(distanceDfs):
            solution = len(distanceRhr)
        return solution

    ## Manque les 2 fonctions









