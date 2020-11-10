'''
Auteurs : Ziad Khafagy - 20161904, Alina Weinberger 20066963
Date : 9.11.2020

Description : 
        Ce fichier permet de creer le jeu interactif demineur. Les regles du jeu
        peuvent etre trouver sur le web.
        
        Fonction principale demineur():
                Cette fonction permet d'attendre le premier click du joueur sur 
                une grille de tuiles avant de placer des mines aléatoirement.
                Ensuite le joueur devoiles les cases une à une, lorsqu'il
                n'y a plus de tuiles à devoiler ou lorsqu'une mine est 
                devoilée, le jeu est terminé.
            

'''
import tuiles

colormap = tuiles.colormap
images= tuiles.images
 
def afficherImage(x, y,colormap, image):      #permet d'afficher une image
                                               #sur une grille de pixel

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
            
def afficherTuile(x,y,tuile):      #affiche une image sur un grille de tuiles 
                                                #une tuile = 16*16 pixels
        afficherImage(x*16,y*16, colormap, tuile)               
        
        
def grilleDeTuiles(hauteur, largeur):  #affiche la grille entiere de tuiles non-
                                        #devoilées en début de jeu 
    for i in range(hauteur):
        for j in range(largeur):
            afficherTuile(i,j, 12) # 12 = tuile non dévoilée
            
def attendreClic():             # retourne la position de la souris et indique
                                # si le joueur veux positionner un drapeau 

    souris = getMouse()  #contient [x, y, button, shift, ctrl, alt]
        
    posX = souris.x
    posY = souris.y
        
    if souris.button == 2 or (souris.button == 1 and souris.ctrl == True):
        drapeau = True 
    else :
        drapeau = False
        
    evenement = struct(posX = posX, posY = posY, drapeau = drapeau)
        
    sleep(0.01)          #pour ne pas surcharger le processeur
        
    return evenement

def grilleDeBooleens(largeur, hauteur): #retourne une grille remplie de False 
                                          
    grille = [[False] * largeur] * hauteur
    return grille

def placerMines(largeur, hauteur, nbMines, x, y):   #place aléatoirement
                                                    #un nombre de fixe mines                                    
    grilleMine = grilleDeBooleens(largeur, hauteur) 

    for i in range(nbMines):
                
        posMineX = int(math.floor(random() * largeur))#nombre entre 0 & largeur
        posMineY = int(math.floor(random() * hauteur))#nombre entre 0 & hauteur
        
        if posMineX != x and posMineY != y :
            grilleMine[posMineX][posMineY] = True
         
        else :              # si position de la mine = position du premier clic
            i -= 1          # ne pas placer de mine  
                            #i-1 pour quand meme placer le bon nombre de mines
        
    return grilleMine


def nbMineVoisine(x,y, grilleMine):  # retourne le nombre de mine
                                     # autour de la tuile (x,y)
    hauteur = getScreenHeight()/16
    largeur = getScreenWidth()/16

    posX = x 
    posY = y 
    
    nbMines = 0         #compteur
                                #determiner si x est:
    if posX == 0  :                         # *sur le bord *superieur 
        debutX = posX
        finX = posX +1    
    elif posX != 0 and posX != hauteur-1 :  # *au milieur de la grille
        debutX = posX-1
        finX = posX +1
    elif posX == hauteur - 1:               # *sur le bord inferieur
        debutX = posX -1
        finX = posX
     
                                #determiner si y est:
    if posY == 0 :                               # *sur le bord gauche
        debutY = posY 
        finY = posY +1 
    elif posY != 0 and posY != largeur - 1 :     # *au milieur de la grille
        debutY = posY-1
        finY = posY +1
    elif posY == largeur - 1:                    # *sur le bord droit
        debutY = posY-1
        finY = posY 
           
        
    for i in range(debutX, finX):               #calculer nb de mines voisines 
        for j in range(debutY, finY):
            if grilleMine[i][j] == True:
                nbMines += 1
                             
    return nbMines

def posDrapeau(grilleDrapeau, drapeau, posX, posY): #retourne un booleen  
                                                  # qui sert à mettre a jour la 
                                                  # grille de Drapeau 
                        
    if drapeau == True and grilleDrapeau[posX][posY] == False : #pas de drapeau 
        afficherTuile(posX, posY, 13)                      #afficher un drapeau
        return True

    elif drapeau == True and grilleDrapeau[posX][posY] == True :#deja un drapeau
        afficherTuile(posX, posY, 12)            #12 = tuile non devoilee 
        return False                                         #enlever le drapeau 
             
    

def devoilerCase(grilleMine, grilleDrapeau, grilleCase, drapeau, posX, posY):
    
    hauteur = int(getScreenHeight()/16)
    largeur = int(getScreenWidth()/16)
     
    fin = False  
      #fin : utilise dans la boucle while fin = False de la fonction principale
        
    if grilleDrapeau[posX][posY] == True :  # si drapeau : ne rien faire 
        return     #continue? 
        
    elif grilleMine[posX][posY] == True :   # si mine : terminer jeu
        afficherTuile(posX, posY, 10)
        fin = terminerJeu(False, grilleMine, posX, posY) 
        
    else:
        nbMinesVoisines = nbMineVoisine(posX, posY, grilleMine)     
        afficherTuile(posX, posY, nbMinesVoisines)  
        grilleCase[posX][posY] = True 
        
#lidee est la mais ne marche malheureusement pas comme prevu
        #test = True      # test si toutes les tuiles non-mines sont devoilees
        #for i in range(hauteur):                #si oui grilleCase devrait
            #for j in range(largeur):            # etre l'oppose de grilleMine
                #if grilleCase[i][j] == grilleMine[i][j]:        
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
        afficherTuile(posX,posY, 10) #afficher la mine cliquee en rouge
        for i in range(hauteur):
            for j in range(largeur):     #afficher toutes les mines restantes
                if grilleMine[i][j] == True :
                    afficherTuile(i,j, 9) 
        alert('Vous avez perdu!')   
        
    fin = True  
        
    return fin  #fin devient True 
                #on sort de la boucle principale de la fonction principale


def demineur(hauteur, largeur, nbMines): 
    
    
    colormap = tuiles.colormap
    images= tuiles.images
   
    setScreenMode(hauteur*16, largeur*16)  #grille de pixel 
        
    grilleDeTuiles(hauteur,largeur)             
    grilleDrapeau = grilleDeBooleens(hauteur, largeur) # a mettre a jour
    grilleCase = grilleDeBooleens(hauteur, largeur)    # a mettre a jour
 
    
    premierClick = True
        
    while premierClick:
        
        evenement = attendreClic() 
        posX = evenement.posX                   #position du pixel
        posY = evenement.posY
        posTX = math.floor(posX/16)             #position de la tuile
        posTY = math.floor(posY/16)
        drapeau = evenement.drapeau
        
        souris = getMouse()
        
        if souris.button == 1 and souris.ctrl == False :   #premier clic
            grilleMine = placerMines(hauteur, largeur, nbMines, posTX, posTY)
            devoilerCase(grilleMine,grilleDrapeau,grilleCase,drapeau,posTX,posTY)
            premierClick = False
        
        elif drapeau == True: #joueur veux poser un drapeau
            grilleDrapeau[posTX][posTY]=posDrapeau(grilleDrapeau,drapeau,posTX,posTY)
            
            

    fin = False
    while fin == False :       #boucle principale
                
        evenement = attendreClic() 
        
        posX = evenement.posX             #position du pixel
        posY = evenement.posY
        
        posTX = math.floor(posX/16)       #position de la tuile
        posTY = math.floor(posY/16)
        
        drapeau = evenement.drapeau
        souris = getMouse()
        
        if drapeau == True: 
            print(grilleDrapeau)
            grilleDrapeau[posX][posTY]=posDrapeau(grilleDrapeau,drapeau,posTX,posTY) 
            print(grilleDrapeau)
        elif souris.button == 1 and souris.ctrl == False :
            fin=devoilerCase(grilleMine,grilleDrapeau,grilleCase,drapeau,posTX,posTY)
                
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

    
    

    assert placerMines(2,2,0,1,2) == [[False, False], [False, False]]
    assert placerMines(2,3,0,1,2) == [[False, False], [False, False],[False, False]]
    assert placerMines(2,4,0,1,2) == [[False, False], [False, False],[False, False],[False, False]]
    assert placerMines(2,5,0,1,2) == [[False, False], [False, False],[False, False],[False, False],[False, False]]
    assert placerMines(2,6,0,1,2) == [[False, False], [False, False],[False, False],[False, False],[False, False],[False, False]]
    assert grilleDeBooleens(1,2) == [[False], [False]]
    assert grilleDeBooleens(2,2) == [[False,False], [False,False]]
    assert grilleDeBooleens(3,5) == [[False,False,False], [False,False,False],[False,False,False],[False,False,False],[False,False,False]]
    assert grilleDeBooleens(3,2) == [[False,False,False], [False,False,False]]
    assert grilleDeBooleens(8,5) == [[False,False,False,False,False,False,False,False], [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False],
                                 [False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False]]
testDemineur()
        
        
      
  
  
  

  
    
    
    
