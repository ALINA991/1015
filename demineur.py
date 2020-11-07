'''creer : 
- fonction qui cree tableau de tuiles (+++ grille des pixel les un a cote des autres)
- fonction 'clic' qui fait l'action de 
        - deposer un drapeau (utiliser attendre clic) 
        - devoiler un case (boutton principal)
              - affiche nb de mines voisine (si pas de mine)
              - affiche mine rouge & toutes mine & termine le jeu (si mine) 
              
- fonction principale (hauteur, largeur) 
    - creer table de grandeur specifiée  
    - attendre le premier click 
    - positioner mines 
    - afficher nb de mines voisines apres 1er clic 
    - si joueur positionne drapeau --> click(Drapeau)
    - si joueru devoile case --> click(nbMine)
    - si jouer devoile mine --> click(Minerouge) + afficher reste des mines

'''
  


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
        
        if souris.boutton == 2 or (souris.boutton == 1 and souris.ctrl == True):
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
            if posMinX != x and posMinY != y : 
                grilleMine[posMineX, posMineY] = True
            else :              # si position de la mine à placer = position du premier click
               i -= 1           # ne pas placer de mine et i-1 pour quand meme placer le bon nombre de mines 
        
    return grilleMine

def nbMineVoisine(x,y, grilleMines):  #retourne le nb de mine autour de la tuile a la postion (x,y)
    posX = x 
    posY = y 
    
    nbMines = 0
    
    for i in range(posX - 1, posX +2):
        for j in range(posY - 1, posX +2):
            if grilleMine[i][j] == True:
                nbMines += 1
                
    return nbMines
  
  def positionerDrapeau(hauteur, largeur, grilleDrapeau): 
   
      while True : 
          posX, posY, drapeau = attendreClick() # est ce que le while True dans attendreClick() continue a tourner si je ne met pas de while true ici? 
      
          if drapeau = True and grilleDrapeau[posX, posX] == False :   #sil ny a pas encore de drapeau sur la tuile 
              afficherTuile(posX, posY, 13) # 13= numero de tuile avec drapeau  # FONCTION A DEFINIR !!!
              grilleDrapeau[posX, posY] = True 
          elif drapeau = True and grilleDrapeau[posX, posX] == True :    #sil y a deja un drapeau sur la tuile
              afficherTuile(posX, posY, 12) #12 = tuile non devoilee 
              grilleDrapeau[posX, posY] = False     #enlever le drapeau 
              
       return grilleDrapeau 
        
    
  def devoilerCase(grilleMine, grilleDrapeau):
    souris = getMouse()
    posX, posY, drapeau = attendreClick() 
    
    if grilleDrapeau[posX, posY] = True        # si drapeau : ne rien faire 
        break     #continue? 
    elif grilleMine = True         # si mine : terminer jeu
        afficherTuile(posX, posY, 10) # 10: mine sur fond rouge
        terminerJeu() # A DEFINIR
    else:
      nbMinesVoisines = nbMineVoisine(posX, posY, grilleMine)     # si pas de mine et pas de drapeau 
      afficherTuile(posX, posY, nbMinesVoisines)                  # afficher nombre de mines voisines 
    
    
def terminerJeu():
  ####? 
  

        
        
def demineur(hauteur, largeur, nbMines):   
  
  grilleDrapeau = grilleDeBooleens(hauteur, largeur) # a mettre a jour avec la fonction positionnerdrapeau()
  
  # on pourrais mettre parametre = Difficulté (1,2,3) (à la place de nbMine)
  # si difficulté = 1 ==> nbMines = x , si difficulté = 2, nbMine=y, ... (x,y, z calculé en fonction de la hauteur/largeur du jeu)
 
  
  # PREMIER CLICK --> get position du premier click
  # x, y = position premier click ( a utiliser dans placer mines) 
  
  grilleMine = placerMines(hauteur, largeur, nbMines, x, y) 
  
  while True: 
      posX, posY, drapeau = attendreClick()
      
      if drapeau = True: 
          grilleDrapeau = positionnerDrapeau(hauteur, largeur, grilleDrapeau) # est ce que c'est possible de mettre a jours grille drapeau comme ca? 
      elif souris.button == 1 and souris.ctrl == False :
          devoilerCase(posX, posY) #A DEFINIR 
        
      
  
  
  

  
    
    
    
