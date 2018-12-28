# Probleme tres simplifie resolu de maniere exacte.

## Circuits et Parametres
map = [[0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0], [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0], [0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0], [0, 0, 0, 7, 7, 7, 7, 7, 7, 0, 0], [0, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0], [0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0], [0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0]]

# map est une matrice caree
tableau = [[[0 for j in range(2)] for k in range(N)] for l in range(N)]

def print_map(map):
    for i in range(N):
        for j in range(N):
            if map[i][j] == 0:
                print("  ",end="")
            elif map[i][j] >= 10:
                print(map[i][j],end="")
            else:
                print(map[i][j],end=" ")
        print("")
    
    
        
#Quantité initiales (v_max en norme infinie)
v_max = 5
v = (0, 0) # (v_x horizontale , v_y  verticale tjs stm negative) 
n = 0


## Algo dynamique
def vitesse_compatible(v1, v2): #teste si en arrivant dans une case a v1, en la supposant dans les bornes, on peut la quitter a v2
    vx1, vy1 = v1
    vx2, vy2 = v2
    bornes_vx = range(-v_max, v_max + 1)
    bonres_vy = range(-v_max, 0)
    if vx2 in bornes_vx and vy2 in bornes_vy:
        if vy2 in [vy1, vy1 + 1, vy1 - 1]:
            if vx2 in [vx1, vx1 + 1, vx1 - 1]:
                return True
    return False

def cases_accessible()

def trajets_possibles(x_dep, y_dep, x_arr): #y_arr = N - 1
    #renvoie la liste des 3-uplets:
        #listes des case intermediaires,
        #nombre de coups (nombre de cases intermediaires),
        #vitesse a avoir en quittant la case
    traj_poss = []
    
#On trouvera les chemins et nb de coups necessaires pour arriver a chaque case d'arrivee.
#On en prend le min.

#On part de la dernière ligne et on remonte jusqu'a la premiere
def plus_courts_chemin(map):
    N = len(map)
    nb_ligne_arr = [i for i in range(N) if map[N - 1][i] != 0]
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
                    li += trajets_possibles( nb_ligne, nb_colonne, i)
                
# A chaque case, on regarde toutes les autres cases accessibles (qui sont + proches de l'arrivee)
# et on prend les chemins de cette nouvelle case qui ont une vitesse de depart compatible avec
# la vitesse requise pour acceder a cette case.
