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
            time.sleep(Vitesse)
        elif Tour%4 ==2:
            CreerFeux(30,20,10,"#000")
            CreerFeux(30,50,10,"#000")
            CreerFeux(30,80,10,"red")
            Dessin.update()
            time.sleep(Vitesse)
        Tour+=1
        
def ChangerVitesse(event):
    global Vitesse
    if ComboVitesse.get() == "Très rapide":
        Vitesse=0.1
    if ComboVitesse.get() == "Rapide":
        Vitesse=1
    if ComboVitesse.get() == "Normale":
        Vitesse=5
    if ComboVitesse.get() == "Long":
        Vitesse=10
    if ComboVitesse.get() == "Très long":
        Vitesse=20


MonApp = Tk()
MonApp.title("Feux tricolor")
 
 
Dessin = Canvas(MonApp, bg ="light grey", width =100, height =120)
Dessin.grid(row =0, column =0)
Tour=0
#supposons la durée normale d'un feu vert et rouge est égale à 5 secondes pour la démonstration
Vitesse=5
Boucle=True

Button(MonApp,text='Quitter',command=MonApp.destroy).grid(row =2, column =2,sticky=E)

LabelVitesse = Label(MonApp, text = "Choix de vitesse")
LabelVitesse.grid(column=0, row=1)


ComboVitesse = ttk.Combobox(MonApp,values=["Très rapide","Rapide","Normale","Long","Très Long"])
ComboVitesse.grid(column=0, row=2)
ComboVitesse.current(2)
ComboVitesse.bind("<<ComboboxSelected>>", ChangerVitesse)


ActionFeux()
    
MonApp.mainloop()
