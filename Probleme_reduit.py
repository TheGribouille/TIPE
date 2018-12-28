## Circuits et Parametres
map = [[0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0], [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0], [0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0], [0, 0, 0, 7, 7, 7, 7, 7, 7, 0, 0], [0, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0], [0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0], [0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0]]

N = len(map) # map est une matrice caree
tableau = [[[0 for j in range(2)] for k in range(N)] for l in range(N)]

def print_map(map):
    for i in range(N):
        for j in range(N):
            if map[i][j] == 0:
                print("   ",end="")
            elif map[i][j] >= 10:
                print(map[i][j],end=" ")
            else:
                print(map[i][j],end="  ")
        print("")
        
#Quantité initiales (v_max en norme infinie)
v_max = 5
v = (0, 0) # (v_x horizontale , v_y  verticale tjs stm negative dans les prochains coups) 
n = 0

## Algo dynamique
def vitesse_compatible(v1, v2): #teste si en arrivant dans une case a v1, en la supposant dans les bornes, on peut la quitter a v2
    vx1, vy1 = v1
    vx2, vy2 = v2
    bornes_vx = range(-v_max, v_max + 1)
    bonres_vy = range(1, v_max)
    if vx2 in bornes_vx and vy2 in bornes_vy:
        if vy2 in [vy1, vy1 + 1, vy1 - 1]:
            if vx2 in [vx1, vx1 + 1, vx1 - 1]:
                return True
    return False

def cases_accessibles(x, y, map): #renvoie la listes de (x', y') accessibles depuis x, y
    c_a = []
    for i in range(-v_max, v_max + 1):
        for j in range(1, v_max + 1):
            if 0<=x + i < N and y + j < N:
                if map[x + i][y + j] !=0:
                    if "aucune case O ne bloque le chemin":
                        c_a = (x + i, y + j) + c_a
    return c_a

def trajets_possibles(x, y, x_arr, map, trajets):
    #map[x][y] != 0
    #y_arr = N - 1
    #renvoie la liste des (v_dep, [cases du trajet], nb de cases)
    t = trajets[x][y] # pour l'instant = [] car aucun trajet de (x, y) a (x_arr, N - 1)
    c_a = cases_accessibles(x, y, map)
    for case in c_a:
        x2, y2 = case
        v_dep = y2 - y, x2 - x
        traj = (x2, y2) + trajets[x2][y2][1]
        #on ajoute la case (x2, y2) au trajet car on part de (x, y)
        t = t + (v_dep, traj, len(traj))
        #on ajoute ce nouveau trajet de (x, y,) a (x_arr, N - 1) dans la liste
        #des trajet de (x, y) a une case d'arrivee qcq
    trajets[x][y] = t
    return trajets

#On part de la dernière ligne et on remonte jusqu'a la premiere
def plus_courts_chemin(map):
    N = len(map)
    nb_ligne_arr = [i for i in range(N) if map[N - 1][i] != 0]
    trajets = [] # liste des (v_dep, [cases du trajet], nb de cases)
    for nb_ligne in range(N - 1, -1, -1):
        #A chaque ligne, on determine pour chaque case du circuit (case !=0) en combien de coups on peut atteindre une case N.
        #Il faut definir un coup et en donner les parametres.
        ligne = map[nb_ligne]
        for nb_colonne in range(N):
            case = ligne[nb_colonne]
            if case != 0:
                #On associe a cette case la liste des trajets possibles
                #pour atteindre une case N avec la vitesse a avoir en quittant cette case
                li_traj_poss = []
                for i in nb_ligne_arr:
                    li = trajets_possibles( nb_ligne, nb_colonne, i) + li
                
# A chaque case, on regarde toutes les autres cases accessibles (qui sont + proches de l'arrivee)
# et on prend les chemins de cette nouvelle case qui ont une vitesse de depart compatible avec
# la vitesse requise pour acceder a cette case.
