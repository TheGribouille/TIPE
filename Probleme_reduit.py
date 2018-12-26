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

#On veut que n ( = ligne sur laquelle se trouve la voiture ) soit N - 1 = 10 ici

for nb_ligne in range(n - 1, -1, -1):
    ligne = map[nb_ligne]
    for nb_colonne in range(N):
        case = map[nb_ligne][nb_colonne]
        if case != 0:
            
            
