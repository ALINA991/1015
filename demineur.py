'''creer : 
- fonction qui cree tableau de tuiles (+++ grille des pixel les un a cote des autres)
- fonction 
        - deposer un drapeau (utiliser attendre clic) : DONE 
        - devoiler un case (boutton principal) :DONE 
              - affiche nb de mines voisine (si pas de mine) :DONE
              - affiche mine rouge & toutes mine & termine le jeu (si mine) :DONE 
              
- fonction principale (hauteur, largeur) : 
    - creer table de grandeur specifiée  
    - attendre le premier click 
    - positioner mines 
    - afficher nb de mines voisines apres 1er clic 
    - si joueur positionne drapeau --> positionnerdrapeau()
    - si joueru devoile case --> devoilerCase()
    - si jouer devoile mine --> devoilerCase() # va voir que mine = True dans le tableau de Mine et terminer jeu
    
RESTE A VOIR : 
        - comment afficher grille de pixel 
        - crrer afficherTuiles() & comprendre difference avec afficher image
        - est ce qu'on peu mettre a jour grilleDrapeau en le mettant comme parametre dans sa propre fonction??
                        => grilleDrapeau = positionnerDrapeau(hauteur, largeur, grilleDrapeau) possible pour mettre a jour? 
        - est ce que fonction getMouse() retourne des position x, y qu'on peu actually utiliser en tant que index dans des tableau 
                ex: pour mettre a jour le tableau grilleDrapeau lorsque joueur positionne drapeau 
        - faire fonctions TESTs()

'''
  


import tuiles


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

def placerMines(largeur, hauteur, nbMines, x, y): #(x,y) position du premier click

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
     
    fin = False                 #utilisé dans la boucle while fin = False de la fonction principale
        
    souris = getMouse()
    posX, posY, drapeau = attendreClick() 
    
    if grilleDrapeau[posX, posY] = True :       # si drapeau : ne rien faire 
        break     #continue? 
    elif grilleMine = True :        # si mine : terminer jeu
        afficherTuile(posX, posY, 10) # 10: mine sur fond rouge
        fin = terminerJeu() # A DEFINIR
    else:
      nbMinesVoisines = nbMineVoisine(posX, posY, grilleMine)     # si pas de mine et pas de drapeau 
      afficherTuile(posX, posY, nbMinesVoisines)                  # afficher nombre de mines voisines 
        
    return fin                          # si on a pas cliqué sur une mine, fin = False et on continue 
                                        # voir le while fin = False de la fonction demineur (fonction principale)
    
    
def terminerJeu():
        
  for i in range(grilleMine.shape[0])
        for j in range(grilleMine.shape[1]):     #afficher toutes les mines restantes
                if grilleMine[i][j] == True 
                        afficherTuile(i,j, 10) 
  alert('Vous avez perdu!')    
  fin = True  
        
  return fin #fin devient True -> on sort de la boucle while fin = False de la fonction principale : fin du jeu 

                        

                   
                        
  

        
        
def demineur(hauteur, largeur, nbMines):   
        
  # FONCTION CREER GRILLE DE PIXELS 
  # AFFICHER TUILES NON DEVOILEE PARTOUT
  
  grilleDrapeau = grilleDeBooleens(hauteur, largeur) # a mettre a jour avec la fonction positionnerdrapeau()
        
   #contient [x, y, button, shift, ctrl, alt]
  
  # on pourrais mettre parametre = Difficulté (1,2,3) (à la place de nbMine)
  # si difficulté = 1 ==> nbMines = x , si difficulté = 2, nbMine=y, ... (x,y, z calculé en fonction de la hauteur/largeur du jeu)

  # PREMIER CLICK --> get position du premier click
  # x, y = position premier click ( a utiliser dans placer mines) 
        
  premierClick = True
        
  while premierClick:
        posX, posY, drapeau = attendreClick()
        
        if drapeau = True: 
            grilleDrapeau = positionnerDrapeau(hauteur, largeur, grilleDrapeau)
        
        elif souris. souris.button == 1 and souris.ctrl == False :   #premier click
            grilleMine = placerMines(hauteur, largeur, nbMines, posX, posY) #on place les mines aleatoirement sauf a lendroit qui vient detre cliqué 
            devoilerCase(grilleMine, grilleDrapeau) 
            premierClick = False
        
  
  while fin == False : 
      posX, posY, drapeau = attendreClick()
      
      if drapeau = True: 
          grilleDrapeau = positionnerDrapeau(hauteur, largeur, grilleDrapeau) # est ce que c'est possible de mettre a jours grille drapeau comme ca? 
      elif souris.button == 1 and souris.ctrl == False :
          fin = devoilerCase(posX, posY) #A DEFINIR 
                

        
        
      
  
  
  

  
    
    
    
