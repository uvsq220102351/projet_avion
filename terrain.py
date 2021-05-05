import tkinter as tk
import random as rd
WIDTH,HEIGHT=1500,350
COTE=50
NB_COL,NB_LINE=30,7
def terrain():
    """les sièges grises et le couloir jaune"""
    for i in range(NB_COL):
        for j in range(NB_LINE):
            carre=cv.create_rectangle(i*COTE,j*COTE,(i+1)*COTE,(j+1)*COTE,fill="grey")
            if j==3:
                cv.itemconfigure(carre,fill="yellow")

racine=tk.Tk()
racine.title("avion")
cv=tk.Canvas(racine,height=HEIGHT,width=WIDTH)
cv.grid()
terrain()
racine.mainloop()