## Circuits et Parametres
import time
from numpy import linspace as ls
from math import floor, ceil

map = [[0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0], [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0], [0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0], [0, 0, 0, 7, 7, 7, 7, 7, 7, 0, 0], [0, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0], [0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0], [0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0]]

N = len(map) # map est une matrice caree
tableau = [[[0 for j in range(2)] for k in range(N)] for l in range(N)]

def print_map(map, x, y):
    for i in range(N):
        for j in range(N):
            if j == x and i == y:
                print("_  ",end="")
            elif map[i][j] == 0:
                print("   ",end="")
            elif map[i][j] == -1:
                print("-1 ",end="")
            elif map[i][j] >= 10:
                print(map[i][j],end=" ")
            else:
                print(map[i][j],end="  ")
        print("")
        
#Quantité initiales (v_max en norme infinie)
v_max = 5
v = (0, 0) # (v_x horizontale , v_y  verticale tjs stm positive dans les prochains coups) 
n = 0

## Algo dynamique
def vitesse_compatible(v1, v2): #teste si en arrivant dans une case a v1, en la supposant dans les bornes, on peut la quitter a v2
    vx1, vy1 = v1
    vx2, vy2 = v2
    bornes_vx = range(-v_max, v_max + 1)
    bornes_vy = range(1, v_max)
    if vx2 in bornes_vx and vy2 in bornes_vy:
        if vy2 in [vy1, vy1 + 1, vy1 - 1]:
            if vx2 in [vx1, vx1 + 1, vx1 - 1]:
                return True
    return False

def mouvement_possible(x, y, x2, y2, map):
    N = len(map)
    c = (x2 - x) / (y2 - y)
    absc = ls(y, y2, 10 * N)
    ordo = x + c * ( absc - y )
    for i in range(10 * N):
    #Il faut trouver la case correspondante:
        a = absc[i]
        o = ordo[i]
        if a - floor(a) < ceil(a) - a:
            case_y = floor(a)
            if o - floor(o) < ceil(o) - o:
                case_x = floor(o)
                if map[case_y][case_x] == 0:
                    return False
            elif o - floor(o) > ceil(o) - o:
                case_x = ceil(o)
                if map[case_y][case_x] == 0:
                    return False
            else:#intersection d'exactement 2 cases
                if map[case_y][floor(o)] == 0 and map[case_y][ceil(o)] == 0:
                    return False
        elif a - floor(a) > ceil(a) - a:
            case_y = ceil(a)
            if o - floor(o) < ceil(o) - o:
                case_x = floor(o)
                if map[case_y][case_x] == 0:
                    return False
            elif o - floor(o) > ceil(o) - o:
                case_x = ceil(o)
                if map[case_y][case_x] == 0:
                    return False
            else:#intersection d'exactement 2 cases
                if map[case_y][floor(o)] == 0 and map[case_y][ceil(o)] == 0:
                    return False
        else:#intersection d'au moins 2 cases
            if o - floor(o) < ceil(o) - o:
                case_x = floor(o)
                if map[floor(a)][case_x] == 0 and map[ceil(a)][case_x] == 0:
                    return False
            elif o - floor(o) > ceil(o) - o:
                case_x = ceil(o)
                if map[floor(a)][case_x] == 0 and map[ceil(a)][case_x] == 0:
                    return False
            else: #intersection de 4 cases
                if map[floor(a)][floor(o)] == 0 and map[floor(a)][ceil(o)] == 0 and map[ceil(a)][floor(o)] == 0 and map[ceil(a)][ceil(o)] == 0:
                    return False
    return True

def cases_accessibles(x, y, map): #renvoie la listes de (x', y') accessibles depuis x, y
    c_a = []
    for i in range(-v_max, v_max + 1):
        for j in range(1, v_max + 1):
            if 0<=x + i < N and y + j < N:
                if map[y + j][x + i] !=0:
                    if mouvement_possible(x, y, x + i, y + j, map):
                        c_a = [(x + i, y + j)] + c_a
    return c_a

def trajets_possibles(x, y, map, trajets):
    #map[x][y] != 0
    #y_arr = N - 1
    #renvoie la liste des (nb de cases, v_dep, [cases du trajet] )
    t = trajets[y][x] # pour l'instant t = [] car aucun trajet de (x, y) a (x_arr, N - 1)
    c_a = cases_accessibles(x, y, map)
    for case in c_a:
        x2, y2 = case
        v_nec = x2 - x, y2 - y
        t2 = trajets[y2][x2]
        for i in range(len(t2)):
        #ne fait rien si t2 vide, ie si aucun chemin ne mene a l'arrivee
            v_dep = t2[i][1]
            if vitesse_compatible(v_nec, v_dep):
                traj = [(x2, y2)] + t2[i][2]
                #on ajoute la case (x2, y2) au trajet car on part de (x, y)
                t = t + [(len(traj), v_nec, traj )]
                #on ajoute ce nouveau trajet de (x, y) a (x_arr, N - 1) dans la liste
                #des trajets de (x, y) a une case d'arrivee qcq
    return t

def plus_court_chemin(map):
    N = len(map)
    nb_ligne_arr = [i for i in range(N) if map[N - 1][i] != 0]
    trajets = [[[] for x in range(N) ] for y in range(N)]
    # liste des [(nb de cases, v_dep, [cases du trajet]), ...] pour ts x, y
    for j in nb_ligne_arr:
        trajets[N - 1][j] = [(0, (v_x, v_y), []) for v_x in range(-v_max, v_max + 1) for v_y in range(1, v_max + 1)]
        #on peut arriver dans ces case avec n'importe quelle vitesse
        #donc il faut faire en sorte que toutes les vitesses d'arrivees soient compatibles
        #donc on dit qu'on peut quitter ces cases avec n'importe quelle vitesse

    #On part de la dernière ligne et on remonte jusqu'a la premiere
    for y in range(N - 2, -1, -1):
        #A chaque ligne, on determine pour chaque case du circuit (case !=0)
        #en combien de coups (cases intermediaires) on peut atteindre une case N.
        ligne = map[y]
        for x in range(N):
            case = ligne[x]
            if case != 0:
                #On associe a cette case la liste des trajets possibles
                #pour atteindre une case N (avec la vitesse a avoir en quittant cette case)
                trajets[y][x] = trajets_possibles( x, y, map, trajets)
    trajets_totaux = []
    for x in range(N):
        if map[0][x] != 0: #on trouve la case depart
            for traj in trajets[0][x]:
                v_dep = traj[1]
                if vitesse_compatible((0, 0), v_dep):
                    trajets_totaux = [traj] + trajets_totaux
    trajet_opt = min(trajets_totaux)
    return trajet_opt
# A chaque case, on regarde toutes les autres cases accessibles (qui sont + proches de l'arrivee)
# et on prend les chemins de cette nouvelle case qui ont une vitesse de depart compatible avec
# la vitesse requise pour acceder a cette case.

def algorithme(map):
    t1 = time.clock()
    trajet = plus_court_chemin(map)
    etapes = trajet[2]
    for case in etapes:
        x, y = case
        print_map(map, x, y)
        print("")
    t2 = time.clock()
    temps = t2 - t1
    print("Nombre de coups = ", trajet[0], "\n", "Temps = ", temps)
   #(4, (1, 1), [(4, 1), (5, 3), (5, 6), (4, 10)])
