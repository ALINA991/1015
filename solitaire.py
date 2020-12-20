# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

''' A faire : 
- remplir init() avec case 4 à 52 : 
        - info utile : si on a les cartes x et y, elles ont la mˆeme couleur si x%4 = y%4, et elles ont la mˆeme valeur si x//4 = y//4.
        - trouver nom de cartes dans dossier 'cards' DONE
        - faire avec BOUCLES (voir descitption du tp ) DONE
        - voir demo ou on a créer un tableau en prog web DONE
        - faire en sorte de les mélanger aléatirement au chargement (random()? ) DONE
        
- lister document.querySelector("#caseN") avec chaque numero de carte -> permet d'Acceder a la carte 

- creer fonction clic() qui definir action a faire lorsque clic : 
        - déplacement au prochain emplacement possible :
                - 2 seulement tout a droite 
                - toute autre carte juste a droit de valeur just en dessous & meme signe 
                
- creer fonction deplacementPossible() pour vois si on peu cliquer sur la carte --> si oui mettre fond vert sur carte 
        - utiliser #carteN comme identificateur -> remplir innerHTML
        
- creer fonction brasser carte() 
        - avoir compteur pour brasser au max 3 fois -- afficher cmb de fois reste a lecran
        - brasser seulement cartes qui ne sont pas encore aligne a gauche a partir de 2
        - creer bouton 'brasser les cartes' et afficher a lecran du joueur
        
- creer pourton nouvelle partie qui apelle init() = nouvelle partie 

- fonction terminé jeu qui se fait apeller si : 
        - toute les cartes sont au bon endroit ( verification dans fonction deplacement possible? boucle while true? ) : 
                - afficher victoire
        - le joueur ne peux plus brasser (compteur = 0 ) ET il ne peux plus deplacer de cartes 
                - afficher perdu 
 ''' 
# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

""" 
Version actuelle : afficher cartes 
                   supprimer as
                   bouton nouvelle partie 
"""

import math
import random


cartes = [  "AH.svg", "AD.svg", "AS.svg", "AC.svg", "2H.svg", "2D.svg", "2S.svg", "2C.svg",
"3H.svg", "3D.svg", "3S.svg", "3C.svg", "4H.svg", "4D.svg", "4S.svg", "4C.svg",
"5H.svg", "5D.svg", "5S.svg", "5C.svg", "6H.svg", "6D.svg", "6S.svg", "6C.svg",
"7H.svg", "7D.svg", "7S.svg", "7C.svg", "8H.svg", "8D.svg", "8S.svg", "8C.svg",
"9H.svg", "9D.svg", "9S.svg", "9C.svg", "10H.svg", "10D.svg", "10S.svg", "10C.svg",
"JH.svg", "JD.svg", "JS.svg", "JC.svg", "QH.svg", "QD.svg", "QS.svg", "QC.svg", 
"KH.svg", "KD.svg", "KS.svg", "KC.svg"]

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def td(contenu, i): 
    if i == 0 or i == 1 or i == 2 or i == 3:
        return '<td id = "case' +str(i)+'"></td>'
    else:
        return '<td id = "case' +str(i)+'"><img src="cards/' + contenu + '"></td>'

def grouper(lst, taille):  # taille = taille maximale des groupes
    groupes = []
    accum = []
    for elem in lst:
        accum.append(elem)
        if len(accum) == taille:
            groupes.append(accum)
            accum = []
    if len(accum) > 0:
        groupes.append(accum)
    return groupes

def trJoin(lst): return tr(''.join(lst))
def tableJoin(lst): return table(''.join(lst))


idx=[]
for i in range(len(cartes)):
    idx.append(i)
    

def brasser(liste, listIdx):
    for i in range(len(liste)):
        idxAlea = int(math.floor(random.random()*52))
        inter = liste[i]        #brasser cartes
        liste[i] = liste[idxAlea]
        liste[idxAlea] = inter

        listIdx[i] = listIdx[idxAlea]  #brasser idx
        listIdx[idxAlea] = i
    return liste, listIdx

test, listIdx = brasser(cartes, idx)    #liste de cartes brasse et idx corrspond
#print(test)

def listeToTable(lst, taille):
    return tableJoin(list(map(trJoin, grouper(list(map(td, lst ,listIdx)), taille))))
#print(listeToTable(cartes, 13))

                    
def init():
    main = document.querySelector("#main")

    main.innerHTML = """
      <style>     
        #jeu table { float: none; }
        #jeu table td { border: 0; padding: 1px 2px; height: auto; }
        #jeu table td img { height: auto; }
      </style>  
      <div id="jeu"> """+ listeToTable(test, 13) + """
      <div>Vous pouvez encore</div> <button onclick="brasserCartes()">brasser les cartes</button><div>fois.</div>
      <button onclick="init()">Nouvelle partie</button>
      """

   
