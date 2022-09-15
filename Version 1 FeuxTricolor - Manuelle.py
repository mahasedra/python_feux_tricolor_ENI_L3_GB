from tkinter import *
 
def CreerFeux(X,Y,Rayon,Couleur):
    Dessin.create_oval(X-Rayon,Y-Rayon,X+Rayon,Y+Rayon,fill=Couleur)
 
def ActionFeux():
    global Tour
    if Tour%4 == 0:
        CreerFeux(30,20,10,"light green")
        CreerFeux(30,50,10,"#000")
        CreerFeux(30,80,10,"#000")
        Tour=0
    elif Tour%4 ==1 or Tour%4 == 3:
        CreerFeux(30,20,10,"#000")
        CreerFeux(30,50,10,"orange")
        CreerFeux(30,80,10,"#000")
    elif Tour%4 ==2:
        CreerFeux(30,20,10,"#000")
        CreerFeux(30,50,10,"#000")
        CreerFeux(30,80,10,"red")
    Tour+=1

 
MonApp = Tk()
MonApp.title("Feux tricolor")


Dessin = Canvas(MonApp, bg ="light grey", width =100, height =150)
Dessin.grid(row =0, column =0)
Tour=0

Button(MonApp,text='Suivant',command=ActionFeux).grid(row =0, column =1,sticky=W)
Button(MonApp,text='Quitter',command=MonApp.destroy).grid(row =0, column =2,sticky=E)

ActionFeux()

MonApp.mainloop()
