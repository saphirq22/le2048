import numpy as np
#from getkey import getkey, keys
import tkinter as tk

nbLigne = 4
nbCol = 4
maGrille = np.zeros((nbLigne, nbCol))



interface = tk.Tk()
interface.geometry ("600x600")
titre = interface.title("2048")

buttonGauche = tk.Button(interface, text="gauche", width=50, height=50, command="rollLeft")
buttonDroite = tk.Button(interface, text="droite", width=50, height=50, command="rollRight")
buttonHaut = tk.Button(interface, text="Haut", width=50, height=50, command="rollUp")
buttonBas = tk.Button(interface, text="Bas", width=50, height=50, command="rollDown")

buttonGauche.pack()
buttonDroite.pack()
buttonHaut.pack()
buttonBas.pack()
interface.mainloop()
#interface.bind("<Up>", RollSomeGrid) # Flèche haut

def retPosition(uneLigne, uneCol, nbMax):
    maligne = np.random.randint(1,nbMax)
    maCol = np.random.randint(1,nbMax)
    while maligne == uneLigne and maCol == uneCol:
        maligne = np.random.randint(1,nbMax)
        maCol = np.random.randint(1,nbMax)
    return [maligne,  maCol]

def retValeurAlea():
    ValeurInit = [2,4]
    return np.random.choice(ValeurInit, 4, p=[0.8,0.2]) #replace = true

def Init_Grid():
    maPosL = retPosition(None, None, nbLigne)
    maPosC = retPosition(maPosL[0], maPosL[1] , nbLigne)
    maGrille[maPosL, maPosC] = retValeurAlea
    print (maGrille)

#def Add_New():
