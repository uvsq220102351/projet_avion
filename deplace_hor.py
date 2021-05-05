import tkinter as tk
import random as rd
WIDTH,HEIGHT=1500,350
COTE=50
NB_COL,NB_LINE=30,7
nombre_de_passager =[]
liste_nombre_random=[i for i in range(0,180)]
def terrain():
    """les sièges grises et le couloir jaune"""
    for i in range(NB_COL):
        for j in range(NB_LINE):
            carre=cv.create_rectangle(i*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE,fill="grey")
            if j==3:
                cv.itemconfigure(carre,fill="yellow")

#générateur de siège
tab=[[0]*NB_COL for i in range (NB_LINE)]
for i in range(NB_LINE):
    for j in range(NB_COL):
        if i==3: #couloir
            break
        else:
            a=rd.choice(liste_nombre_random)
            liste_nombre_random.remove(a)
            tab[i][j]=a 

def afficher_tableau(tab):
    """Affiche un tableau"""
    for i in range(NB_LINE):
        for j in range(NB_COL):
            print(tab[i][j], end=" ")
        print()

#position des numéros aléatoires (sièges)
no_de_siege= [0,0]
def position_siege(x):
    """fonction renvoie la position [NB_LINE,NB_COL] de sige"""
    for i in range (NB_LINE):
        for j in range(NB_COL):
            if tab[i][j]==x:
                no_de_siege[0]=i+1
                no_de_siege[1]=j+1
    return no_de_siege
print(position_siege(1))

def creer_balle():
    """générer les passagers, chaque passager a une siège différente"""
    global cercle
    cercle=cv.create_oval(0,3*COTE,COTE,(3+1)*COTE,fill="blue",)  
    dx,dy=50,50
    return [cercle,dx,dy]

cpt_horizontal,ctp_vertical=0,0
def deplacement_horizontal(balle):
    #for de i à k avec k le rang 
    #r = passager[x][1]
    global cpt_horizontal
    cv.move(balle[0],balle[1],0) #déplacement horizontalement
    id_after=cv.after(500,lambda:deplacement_horizontal(balle))
    cpt_horizontal+=1
    if cpt_horizontal==(int(no_de_siege[1])-1):
        balle[1]=0
        cv.after_cancel((id_after))


racine=tk.Tk()
racine.title("avion")
cv=tk.Canvas(racine,height=HEIGHT,width=WIDTH)
cv.grid()
terrain()
bouton=tk.Button(racine,)
balle=creer_balle()
deplacement_horizontal(balle)
racine.mainloop()
