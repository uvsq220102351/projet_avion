
import random as rd
r=30
s=7
place=[[0]*r for i in range(0,s)]
T=[0]*180
for i in range(s):
    for j in range(r):
        if i==3: # le couloir
            break
        stop=1 # compteur : si = 1 passager non attribué, si = 0 passager trouvé, on passe au suivant
        while stop:
            a=rd.randint(1,180)
            if (not T[a-1]): #dans T, =0 quand pas attribué, =1 quand attribué
                place[i][j]=a
                stop=0 # passager trouvé, = 0 pour sortir du while
                T[a-1]=1 # passager placé
                #print(T)
print(place[0][1])
for i in place:
    print(' '.join([str(j) for j in i]))

passager =[[0]*2 for i in range(180)]

for i in range (s):
    for j in range(r):
        passager[place[i][j]-1][0] = i+1
        passager[place[i][j]-1][1] = j+1

#passager[siege,rang] avec chaque indice = n°passager -1
for i in passager:
    print(' '.join([str(j) for j in i]))