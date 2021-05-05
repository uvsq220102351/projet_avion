#importation
import random as rd
#chaque carré est lié à un nombre aléatoire de 0 à 180 
NB_COL,NB_LINE=30,7
liste_nombre_random=[i for i in range(0,180)]
tab=[[0]*NB_COL for i in range (NB_LINE)]
for i in range(NB_LINE):
    for j in range(NB_COL):
        if i==3: #couloir
            break
        else:
            a=rd.choice(liste_nombre_random)
            liste_nombre_random.remove(a)
            tab[i][j]=a
print(tab)   

def afficher_tableau(x):
    """Affiche un tableau"""
    for i in range(NB_LINE):
        for j in range(NB_COL):
            print(tab[i][j], end=" ")
        print()
print(afficher_tableau(tab))

#position des numéros aléatoires (sièges)
siege=[[0]*2 for i in range (180)]
for i in range (NB_LINE):
    for j in range(NB_COL):
        siege[tab[i][j]-1][0] = i+1
        siege[tab[i][j]-1][1] = j+1
for i in siege:
    print(' '.join([str(j) for j in i]))
