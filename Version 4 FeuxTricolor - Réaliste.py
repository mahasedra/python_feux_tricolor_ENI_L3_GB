from tkinter import *
from tkinter import ttk
import time

def CreerFeux(X,Y,Rayon,Couleur):
    Dessin.create_oval(X-Rayon,Y-Rayon,X+Rayon,Y+Rayon,fill=Couleur)
 
def ActionFeux():
    global Tour
    global Boucle
    while Boucle :
        if Tour%4 == 0:
            CreerFeux(30,20,10,"green")
            CreerFeux(30,50,10,"#000")
            CreerFeux(30,80,10,"#000")
            a=0
            Dessin.update()
            time.sleep(Vitesse)
        elif Tour%4 ==1 or Tour%4 == 3:
            CreerFeux(30,20,10,"#000")
            CreerFeux(30,50,10,"orange")
            CreerFeux(30,80,10,"#000")
            Dessin.update()
            time.sleep(Vitesse/4)
        elif Tour%4 ==2:
            CreerFeux(30,20,10,"#000")
            CreerFeux(30,50,10,"#000")
            CreerFeux(30,80,10,"red")
            Dessin.update()
            time.sleep(Vitesse)
        Tour+=1

MonApp = Tk()
MonApp.title("Feux tricolor")
 
 
Dessin = Canvas(MonApp, bg ="light grey", width =100, height =120)
Dessin.grid(row =0, column =0)
Tour=0
#supposons la durée normale d'un feu vert et rouge est égale à 5 secondes pour la démonstration
Vitesse=5
Boucle=True

Button(MonApp,text='Quitter',command=MonApp.destroy).grid(row =1, column =1,sticky=E)

ActionFeux()

MonApp.mainloop()
