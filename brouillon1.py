import tkinter as tk
import random as rd
WIDTH,HEIGHT=350,1500
COTE=30
nombre_de_passager =[]
tab=[[0]*30 for i in range(0,7)]

r=30
s=7
place=[[0]*r for i in range(0,s)]
T=[0]*180
for i in range(s):
    for j in range(r):
        if i==3:
            break
        stop=1
        while stop:
            a=rd.randint(1,180)
            if (not T[a-1]):
                place[i][j]=a
                stop=0
                T[a-1]=1
                #print(T)
#print(place[0][1])
for i in place:
    print(' '.join([str(j) for j in i]))

def terrain():
    """les sièges grises et le couloir jaune"""
    for i in range(7):
        for j in range(30):
            carre=cv.create_rectangle(i*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE,fill="grey")
            if i==3:
                cv.itemconfigure(carre,fill="yellow")

#carré où se localise un passager est égal à 1 par ex tab[i][j]=1 sinon tab[i][j]=0

def creer_balle():
    """générer les passagers, chaque passager a une siège différente"""
    global cercle
    while len(nombre_de_passager) < 180:
        cercle=cv.create_oval(3*COTE,0,(3+1)*COTE,COTE,fill="blue",)  
        nombre_de_passager.append(cercle)
    dx=-30
    dy=0
    return [cercle,dx,dy]
    
def deplacement(balle):
    """aller à la siège"""
    if a==1: 
        cv.move(balle[0],0,balle[2])
    cv.after(1000,lambda:deplacement(balle))
    
racine=tk.Tk()
racine.title("avion")
cv=tk.Canvas(racine,height=HEIGHT,width=WIDTH)
cv.grid()
terrain()
bouton=tk.Button(racine,)
balle=creer_balle()
bouton=tk.Button(racine, text="move",command=deplacement(balle))
bouton.grid()
racine.mainloop()