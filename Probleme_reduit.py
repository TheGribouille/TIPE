# Probleme tres simplifie resolu de maniere exacte.

## Circuits et Parametres
map = [[0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0], [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0], [0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0], [0, 0, 0, 7, 7, 7, 7, 7, 7, 0, 0], [0, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0], [0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0], [0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0]]

N = len(map) # map est une matrice caree
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

#On veut que n ( = ligne sur laquelle se trouve la voiture ) soit N - 1 = 10 ici.
#On trouvera les chemins et nb de coups necessaires pour chaque case d'arrivee. On en prend le min.

#On part de la dernière ligne et on remonte jusqu'a la premiere
for nb_ligne in range(N - 1, -1, -1):
    #A chaque ligne, on determine pour chaque case du circuit (case !=0) en combien de coups on peut l'atteindre depuis chacune des cases possibles du circuit. Il faut definir un coup et en donner les parametres.
    ligne = map[nb_ligne]
    for nb_colonne in range(N):
        case = map[nb_ligne][nb_colonne]
        if case != 0:
            #On trouve les lignes possibles:
            #On parcourt les lignes stm inferieures, car v_y stm negatif, d'ou on peut atteindre case au pire avec v = v_max
            for lignes_poss in range(ligne - 1, ligne - v_max - 1, -1):
                #Dans chacune des lignes_poss, on trouve les cases_poss:
                
                
