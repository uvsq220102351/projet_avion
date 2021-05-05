import tkinter as tk
import random as rd
WIDTH,HEIGHT=1500,350
COTE=50
NB_COL,NB_LINE=30,7 #nombre de colonnes et de lignes du tableau tab
liste_nombre_random=[i for i in range(0,180)]
liste_de_bagage=[0,1,2]
nombre_de_passager=[]

#terrain d'avion
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
no_de_siege= [0,0,0]
def position_siege(x):
    for i in range (NB_LINE):
        for j in range(NB_COL):
            if tab[i][j]==x:
                no_de_siege[0]=i+1
                no_de_siege[1]=j+1
    no_de_siege[2]=rd.choice(liste_de_bagage)
    return no_de_siege
print(position_siege(1))

#générateur de passager
def generateur_passager():
    """quand (4,1) est vide, un passager apparaît jusquà 180 passagers"""
    global passager,nombre_de_passager
    while len(nombre_de_passager) < 180: 
        for i in range(NB_LINE):
            for j in range(NB_COL):
                tab[3][1]==0  
                passager=cv.create_oval(0,3*COTE,COTE,(3+1)*COTE,fill="blue")
                position_siege(len(nombre_de_passager))
                nombre_de_passager.append(passager)
    dx,dy=COTE,COTE #une unité de déplacement
    return [passager,dx,dy]

#déplacement du passager
cpt_horizontal,ctp_vertical=0,0
def deplacement_horizontal(balle):
    #for de i à k avec k le rang 
    #r = passager[x][1]
    global cpt_horizontal,ctp_vertical
    cv.move(balle[0],balle[1],0) #déplacement horizontalement
    id_after=cv.after(500,lambda:deplacement_horizontal(balle))
    cpt_horizontal+=1
    if cpt_horizontal==(int(no_de_siege[1])-1):
        balle[1]=0
        cv.after_cancel((id_after))
    #pause pour la mise de bagage
    #stop quand il y a un passager devant
    if int((no_de_siege[0]))==1:
        cv.move(balle[0],0,-balle[2])
        ctp_vertical+=1
        if ctp_vertical==3:
            balle[1]=0
            cv.after_cancel((id_after))
    if int((no_de_siege[0]))==2:
        cv.move(balle[0],0,-balle[2])
        ctp_vertical+=1
        if ctp_vertical==2:
            balle[1]=0
            cv.after_cancel((id_after))
    if int((no_de_siege[0]))==3:
        cv.move(balle[0],0,-balle[2])
        ctp_vertical+=1
        if ctp_vertical==1:
            balle[1]=0
            cv.after_cancel((id_after))
    if int((no_de_siege[0]))==5:
        cv.move(balle[0],0,balle[2])
        ctp_vertical+=1
        if ctp_vertical==1:
            balle[1]=0
            cv.after_cancel((id_after))
    if int((no_de_siege[0]))==6:
        cv.move(balle[0],0,balle[2])
        ctp_vertical+=1
        if ctp_vertical==2:
            balle[1]=0
            cv.after_cancel((id_after))
    if int((no_de_siege[0]))==7:
        cv.move(balle[0],0,balle[2])
        ctp_vertical+=1
        if ctp_vertical==3:
            balle[1]=0
            cv.after_cancel((id_after))
    #échanger la place
    

racine=tk.Tk()
racine.title("avion")
cv=tk.Canvas(racine,height=HEIGHT,width=WIDTH)
cv.grid()
terrain()
bouton=tk.Button(racine,)
balle=generateur_passager()
bouton.grid()
deplacement_horizontal(balle)
racine.mainloop()
