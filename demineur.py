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
        
        
A MODIFIER : 
        - attendreclick() doit returner un enregistrement :DONE
        - nbMinevoisne doit prendre en compte au niveau des bors : moins de 8 tuiles voisines : DONE
        - si toutes tuiles devoilee il faut treminer le jeu : DONE 
        
        _ FONCTION AFFICHER GRILLE DE TUILES? --> pour terminer le jeu lorsque toute mines sont devoilee DONE MAIS SANS FONCTION 
                        VOIR SI MIEUX AVEC FONCTION 
                        il faut check si pour toutes tuiles != mine --> tuiles 
        - cheack pour position x,y de getMouse --> convertir en int en fonction de taille de grille de tuiles
        
        JE PENSE QUIL FAUT UNE FONCTION GRILLE DE TUILES ABSOLUMENT 
        PUIS ON POURRAS AVOIR DES (x,Y) qu'on va arrondir en fonction de la taille des tuiles (qui est en fonction de la taille de la grille de tuiles)
        

'''
import tuiles

colormap = tuiles.colormap
images= tuiles.images
 
def afficherImage(x, y,colormap, image):
    

    nbPixelParTuile = 16
    aAfficher = tuiles.images[image] 
    s =-1
    t = -1
    for i in range(x, x+nbPixelParTuile-1):
        t+=1
        for j in range(y, y + nbPixelParTuile-1):
            s+=1
            setPixel(i,j,colormap[aAfficher[s][t]]) 
        s=0
            
def afficherTuile(x,y,tuile):
        afficherImage(x*16,y*16, colormap, tuile)
        
        
def grilleDeTuiles(hauteur, largeur): 
    for i in range(hauteur):
        for j in range(largeur):
            afficherTuile(i,j, 12) #tuile non dévoilée
            
def attendreClic():
    #doit retourner position (x,y) de la souris
    #et drapeau = True si joueur veux positionner un drapeau (voir clics a faire)

    souris = getMouse() #contient [x, y, button, shift, ctrl, alt]
        
    posX = souris.x
    posY = souris.y
        
    if souris.button == 2 or (souris.button == 1 and souris.ctrl == True):
        drapeau = True 
    else :
        drapeau = False
        
    evenement = struct(posX = posX, posY = posY, drapeau = drapeau)
        
    sleep(0.01)    #pour pas surcharger le processeur
        
    return evenement

def grilleDeBooleens(largeur, hauteur):
    #retourne une grille remplie de False 
    #a mettre a jours lorsque joueur a positionne des drapeau 
    
    grille = [[False] * largeur] * hauteur
    return grille

def placerMines(largeur, hauteur, nbMines, x, y): #(x,y) position du premier click

    grilleMine = grilleDeBooleens(largeur, hauteur)   #grille remplie de False
    for i in range(nbMines):
        posMineX = int(math.floor(random() * largeur))
        posMineY = int(math.floor(random() * hauteur))
        print(posMineX, posMineY)
        
        if posMineX != x and posMineY != y :
            grilleMine[posMineX][posMineY] = True
            print(grilleMine)
        else :              # si position de la mine à placer = position du premier click
            i -= 1           # ne pas placer de mine et i-1 pour quand meme placer le bon nombre de mines 
        
    return grilleMine

def nbMineVoisine(x,y, grilleMine):  #retourne le nb de mine autour de la tuile a la postion (x,y)
      
        
    hauteur = getScreenHeight()/16
    largeur = getScreenWidth()/16
    

    posX = x 
    posY = y 
    
    nbMines = 0

    if posX == 0  :             #determiner si x est sur le bord *superieur 
        debutX = posX
        finX = posX +1    
    elif posX != 0 and posX != hauteur-1 : #*au milieur de la grille
        debutX = posX-1
        finX = posX +1
    elif posX == hauteur - 1:  #sur le bord inferieur
        debutX = posX -1
        finX = posX
     

    if posY == 0 :                      #determiner si y est sur le bord gauche
        debutY = posY 
        finY = posY +1 
    elif posY != 0 and posY != largeur - 1 :    #*au milieur de la grille
        debutY = posY-1
        finY = posY +1
    elif posY == largeur - 1:            #sur le bord droit
        debutY = posY-1
        finY = posY 
           
        
    for i in range(debutX, finX):   #calculer nb de mines voisines 
        for j in range(debutY, finY):
            if grilleMine[i][j] == True:
                nbMines += 1
                             
    return nbMines

def positionerDrapeau(grilleDrapeau, drapeau, posX, posY): #####
   
    
    if drapeau == True and grilleDrapeau[posX][posY] == False :   #sil ny a pas encore de drapeau sur la tuile 
        afficherTuile(posX, posY, 13) # 13= numero de tuile avec drapeau  # FONCTION A DEFINIR !!!
        return True
    elif drapeau == True and grilleDrapeau[posX][posY] == True :    #sil y a deja un drapeau sur la tuile
        afficherTuile(posX, posY, 12) #12 = tuile non devoilee 
        return False     #enlever le drapeau 
             
    

def devoilerCase(grilleMine, grilleDrapeau, grilleCase, drapeau, posX, posY):
    
    hauteur = int(getScreenHeight()/16)
    largeur = int(getScreenWidth()/16)
     
    fin = False  
    #utilisé dans la boucle while fin = False de la fonction principale
    if grilleDrapeau[posX][posY] == True :       # si drapeau : ne rien faire 
        return     #continue? 
        
    elif grilleMine[posX][posY] == True :        # si mine : terminer jeu
        afficherTuile(posX, posY, 10) # 10: mine sur fond rouge
        fin = terminerJeu(False, grilleMine, posX, posY) # A DEFINIR
        
    else:
        nbMinesVoisines = nbMineVoisine(posX, posY, grilleMine)     # si pas de mine et pas de drapeau 
        afficherTuile(posX, posY, nbMinesVoisines)  
        grilleCase[posX][posY] = True 
        
        #test = True                                     # test si toutes les tuiles non-mines sont devoilees
        #for i in range(hauteur):
            #for j in range(largeur):                 #si oui alors toutes les case de grilleCase 
                #if grilleCase[i][j] == grilleMine[i][j]:        #devrait etre l'inverse de grilleMine (pas un de ==)
                    #test = False 
                    #break
        #if test == True:
            #fin = terminerJeu(True, grilleMine, posX, posY)
                        
    return fin   

def terminerJeu(victoire, grilleMine, posX, posY):
    hauteur = int(getScreenHeight()/16)
    largeur = int(getScreenWidth()/16)
   
    if victoire == True: 
        alert('Vous avez gagné!')
                   
    if victoire ==  False:
        afficherTuile(posX,posY, 10) 
        for i in range(hauteur):
            for j in range(largeur):     #afficher toutes les mines restantes
                if grilleMine[i][j] == True :
                    afficherTuile(i,j, 9) 
        alert('Vous avez perdu!')   
        
    fin = True  
        
    return fin #fin devient True -> on sort de la boucle while fin = False de la fonction principale : fin du jeu 



def demineur(hauteur, largeur, nbMines): 
    
    
    colormap = tuiles.colormap
    images= tuiles.images
   
    setScreenMode(hauteur*16, largeur*16)  #grille de pixel 
        
    grilleDeTuiles(hauteur,largeur)
    grilleDrapeau = grilleDeBooleens(hauteur, largeur) # a mettre a jour avec la fonction positionnerdrapeau()
    grilleCase = grilleDeBooleens(hauteur, largeur) 
 
    
    premierClick = True
        
    while premierClick:
        
        evenement = attendreClic() # est ce que le while True dans attendreClick() continue a tourner si je ne met pas de while true ici? 
        posX = evenement.posX #VOIR SIL FAUT PAS CONVERTIR POSITIONS
        posY = evenement.posY
        posTuileX = math.floor(posX/16)
        posTuileY = math.floor(posY/16)
        drapeau = evenement.drapeau
        
        souris = getMouse()
        
        if souris.button == 1 and souris.ctrl == False :   #premier click
            grilleMine = placerMines(hauteur, largeur, nbMines, posTuileX, posTuileY) #on place les mines aleatoirement sauf a lendroit qui vient detre cliqué 
            devoilerCase(grilleMine, grilleDrapeau, grilleCase, drapeau, posTuileX, posTuileY)
            premierClick = False
        
        elif drapeau == True: 
            print(grilleDrapeau)
            grilleDrapeau[posTuileX][posTuileY] = positionnerDrapeau(grilleDrapeau, drapeau, posTuileX, posTuileY)
            print(grilleDrapeau)
            

    fin = False
    
    while fin == False : 
        evenement = attendreClic() 
        posX = evenement.posX             #VOIR SIL FAUT PAS CONVERTIR POSITIONS
        posY = evenement.posY
        posTuileX = math.floor(posX/16)
        posTuileY = math.floor(posY/16)
        drapeau = evenement.drapeau
      
        souris = getMouse()
        
        if drapeau == True: 
            print(grilleDrapeau)
            grilleDrapeau[posTuileX][posTuileY] = positionnerDrapeau(grilleDrapeau, drapeau, posTuileX, posTuileY) # est ce que c'est possible de mettre a jours grille drapeau comme ca? 
            print(grilleDrapeau)
        elif souris.button == 1 and souris.ctrl == False :
            fin = devoilerCase(grilleMine, grilleDrapeau, grilleCase, drapeau, posTuileX, posTuileY)
                
def testDemineur():
    setScreenMode(16*2,16*1)
    afficherImage(16,0, tuiles.colormap,4)
    assert exportScreen() == '\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#008#008#008#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#008#008#008#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#008#008#008#ccc#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#008#008#008#ccc#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#008#008#008#008#008#008#008#008#008#008#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#008#008#008#008#008#008#008#008#008#008#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#008#008#008#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000'
    setScreenMode(16*2,16*1)
    afficherImage(16,1, tuiles.colormap,5)
    assert exportScreen () =='\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#800#800#800#800#800#800#800#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#800#800#800#800#800#800#800#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#800#800#800#800#800#800#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#800#800#800#800#800#800#800#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#800#800#800#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#800#800#800#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#800#800#800#800#800#800#800#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#800#800#800#800#800#800#800#800#800#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000'
    setScreenMode(16*2,16*1)
    afficherImage(15,1, tuiles.colormap,11)
    assert exportScreen () =='\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#f00#f00#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#f00#f00#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#f00#f00#ccc#000#000#000#000#000#ccc#f00#f00#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#f00#f00#000#000#000#000#000#f00#f00#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#f00#f00#fff#000#000#f00#f00#000#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#000#f00#f00#000#f00#f00#000#000#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#000#000#000#000#000#f00#f00#f00#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#000#f00#f00#000#f00#f00#000#000#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#f00#f00#000#000#000#f00#f00#000#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#f00#f00#000#000#000#000#000#f00#f00#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#f00#f00#ccc#000#000#000#000#000#000#f00#f00#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#f00#f00#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#f00#f00#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#ccc#ccc#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000'
    setScreenMode(16*3,16*2)
    afficherImage(10,8, tuiles.colormap,9)
    assert exportScreen () == '\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#ccc#000#000#000#000#000#ccc#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#000#fff#fff#000#000#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#000#fff#fff#000#000#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#000#ccc#000#000#000#000#000#ccc#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000'
    setScreenMode(16*3,16*2)
    afficherImage(5,3, tuiles.colormap,7)
    assert exportScreen () == '\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#000#000#000#000#000#000#000#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#000#000#000#000#000#000#000#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#888#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#ccc#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000\n\
#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000#000'

    
    


    
testDemineur()
        
        
      
  
  
  

  
    
    
    
