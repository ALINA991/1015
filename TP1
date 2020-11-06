import tuiles

#J'avais mis ces initialisation (haut, larg) dans le corps de la fonction afficherImage au debut 
#mais plusieurs fonction utilise des parametre hauteur et largeur
#so spécifier au debut dans script? ou j'ai mal compris qqchose? 
hauteur = getScreenHeight()                 
largeur = getScreenWidth()

def afficherImage(x, y, colormap, image):  # pas sur si j'ai pas codé la fonction afficherTuile??
                                           # a quoi sert x, y, et meme colormap si on peu specifier 
                                             #tuiles.colormap dans le corps de la fonction  
      

    aAfficher = tuiles.images[image]     #sort la grille de valeur de couleur (dans colormap) 
                                         #correspondant a l'image qu'on veux
    for i in range(larg):
        for j in range(haut):
            setPixel(j,i,colormap[aAfficher[i][j]])  #set chaque pixel pour afficher l'image
            
def attendreClic():
    #doit retourner position (x,y) de la souris
    #et drapeau = True si joueur veux positionner un drapeau (voir clics a faire)
    
    while True: 
        souris = getMouse() #contient [x, y, button, shift, ctrl, alt]
        
        posX = souris.x
        posY = souris.y
        
        if souris.boutton == 2 or (souris.boutton == 1 and ctrl == True):
            drapeau = True 
        else :
            drapeau = False
        sleep(0.01)    #pour pas surcharger le processeur
        
    return posX, posY, drapeau

def grilleDeBooleens(largeur, hauteur):
    #retourne une grille remplie de False 
    #a mettre a jours lorsque joueur a positionne des drapeau 
    
    grille = [[False] * largeur] * hauteur
    return grille 

def placerMines(largeur, hauteur, nbMines, x, y): #(x,y) garantie False = position de prmier clic? 

    grilleMine = grilleDeBooleens(largeur, hauteur)   #grille remplie de False
    for i in range(nbMines):
        posMineX = math.floor(random() * largeur)
        posMineY = math.floor(random() * hauteur)
        grilleMine[posMineX, posMineY] = True
        
    return grilleMine

def nbMineVoisine(x,y, mines):  #retourne le nb de mine autour de la tuile a la postion (x,y)
    posX = x 
    posY = y 
    grilleMine = tableauDeMines #a definir à lexterieur avec fontion placerMines
    nbMines = 0
    
    for i in range(posX - 1, posX +2):
        for j in range(posY - 1, posX +2):
            if grilleMine[i][j] == True:
                nbMines += 1
                
    return nbMines
