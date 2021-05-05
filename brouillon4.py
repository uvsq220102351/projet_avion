import tkinter as tk
import random as rd
WIDTH,HEIGHT=350,1500
COTE=30
nombre_de_passager =[]


def terrain():
    """les sièges grises et le couloir jaune"""
    for i in range(7):
        for j in range(30):
            carre=cv.create_rectangle(i*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE,fill="grey")
            if i==3:
                cv.itemconfigure(carre,fill="yellow")

def creer_balle():
    """générer les passagers, chaque passager a une siège différente"""
    global cercle
    cercle=cv.create_oval(3*COTE,0,(3+1)*COTE,COTE,fill="blue",)  
    dx=30
    dy=30
    return [cercle,dx,dy]

def deplacement(creer_balle):
    #for de i à k avec k le rang 
    #r = passager[x][1]
    for i in range(3):
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
