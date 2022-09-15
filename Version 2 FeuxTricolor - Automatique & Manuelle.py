from tkinter import *
from tkinter import ttk

import time

def CreerFeux(X,Y,Rayon,Couleur):
    Dessin.create_oval(X-Rayon,Y-Rayon,X+Rayon,Y+Rayon,fill=Couleur)
 
def ActionFeux():
    global Tour
    if Tour%4 == 0:
        CreerFeux(30,20,10,"green")
        CreerFeux(30,50,10,"#000")
        CreerFeux(30,80,10,"#000")
        Tour=0
        Dessin.update()
    elif Tour%4 ==1 or Tour%4 == 3:
        CreerFeux(30,20,10,"#000")
        CreerFeux(30,50,10,"orange")
        CreerFeux(30,80,10,"#000")
        Dessin.update()
    elif Tour%4 ==2:
        CreerFeux(30,20,10,"#000")
        CreerFeux(30,50,10,"#000")
        CreerFeux(30,80,10,"red")
        Dessin.update()
    Tour+=1
def changeState():
    if (btn1['state'] == NORMAL):
        btn1['state'] = DISABLED
    else:
        btn1['state'] = NORMAL

def ChangerMode(event):
    global Boucle
    if ComboMode.get()== 'Automatique':
        BtnChangerMode['state'] = DISABLED
        Boucle = True
        while Boucle:
            time.sleep(1)
            ActionFeux()
    else:
        BtnChangerMode['state'] = NORMAL
        Boucle = False
        ActionFeux()
 
MonApp = Tk()
MonApp.title("Feux tricolor")
 
 
Dessin = Canvas(MonApp, bg ="light grey", width =100, height =150)
Dessin.grid(row =0, column =0)
Tour=0
Boucle=True
Button(MonApp,text='Quitter',command=MonApp.destroy).grid(row =2, column =2,sticky=E)
Button(MonApp,text='ch',command=ChangerMode).grid(row =2, column =3,sticky=E)

LabelMode = Label(MonApp, text = "Choix de mode")
LabelMode.grid(column=0, row=1)

ComboMode = ttk.Combobox(MonApp,values=["Manuelle","Automatique"])
ComboMode.grid(column=0, row=2)
ComboMode.current(0)
ComboMode.bind("<<ComboboxSelected>>", ChangerMode)

BtnChangerMode = Button(MonApp,text='Changer Feu', state = NORMAL, command=ActionFeux)
BtnChangerMode.grid(row =0, column =1)

ActionFeux()

MonApp.mainloop()
