# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

''' A faire : 
- remplir init() avec case 4 à 52 : 
        - info utile : si on a les cartes x et y, elles ont la mˆeme couleur si x%4 = y%4, et elles ont la mˆeme valeur si x//4 = y//4.
        - trouver nom de cartes dans dossier 'cards'
        - faire avec BOUCLES (voir descitption du tp ) 
        - voir demo ou on a créer un tableau en prog web 
        - faire en sorte de les mélanger aléatirement au chargement (random()? ) 
        
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
def idCartes(i):                # retourne id et nom de carte pour init()
    cartes = [  AH.svg, AD.svg, AS.svg, AC.svg, 2H.svg, 2D.svg, 2S.svg, 2C.svg,
                3H.svg, 3D.svg, 3S.svg, 3C.svg, 4H.svg, 4D.svg, 4S.svg, 4C.svg,
                5H.svg, 5D.svg, 5S.svg, 5C.svg, 6H.svg, 6D.svg, 6S.svg, 6C.svg,
                7H.svg, 7D.svg, 7S.svg, 7C.svg, 8H.svg, 8D.svg, 8S.svg, 8C.svg,
                9H.svg, 9D.svg, 9S.svg, 9C.svg, 10H.svg, 10D.svg, 10S.svg, 10C.svg,
                JH.svg, JD.svg, JS.svg, JC.svg, QH.svg, QD.svg, QS.svg, QC.svg, 
                KH.svg, KD.svg, KS.svg, KC.svg]
     return "case" + i , cartes[i]

                         #fonctions de demo 11 
def table(contenu): return '<table>' + contenu + '</table>'   #creer tableau         
def tr(contenu): return '<tr>' + contenu + '</tr>'             # balise tr pour row de tab
def td(contenu): return '<td>' + contenu + '</td>'             # balise pour 1 element de tab

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

def trJoin(lst): return tr(''.join(lst))               #chqnger tout ca pour que cq nous affiche bien ce auon veux
def tableJoin(lst): return table(''.join(lst))          # ex inclure dans chaque balise td  "id = idCartes(i)[0]" (boucle)
                                                        # et entre td et /td mettre <img src="cards/idCartes(i)[1]"> 
                                                        # en utilisant fonction idCartes definie plus haut

def listeToTable(lst, taille):
    return tableJoin(list(map(trJoin, grouper(list(map(td, cartes), taille))))

    cartes = [  AH.svg, AD.svg, AS.svg, AC.svg, 2H.svg, 2D.svg, 2S.svg, 2C.svg,
                3H.svg, 3D.svg, 3S.svg, 3C.svg, 4H.svg, 4D.svg, 4S.svg, 4C.svg,
                5H.svg, 5D.svg, 5S.svg, 5C.svg, 6H.svg, 6D.svg, 6S.svg, 6C.svg,
                7H.svg, 7D.svg, 7S.svg, 7C.svg, 8H.svg, 8D.svg, 8S.svg, 8C.svg,
                9H.svg, 9D.svg, 9S.svg, 9C.svg, 10H.svg, 10D.svg, 10S.svg, 10C.svg,
                JH.svg, JD.svg, JS.svg, JC.svg, QH.svg, QD.svg, QS.svg, QC.svg, 
                KH.svg, KD.svg, KS.svg, KC.svg]
                     
listeToTable(cartes,12)
                     
def init():
    main = document.querySelector("#main")
    main.innerHTML = """
                
        #jeu table { float: none; }
        #jeu table td { border: 0; padding: 1px 2px; height: auto; }
        #jeu table td img { height: auto; }
      </style>
      <div id="jeu">
        <table>
          <tr>
            <td id="case0"><img src="cards/2S.svg"></td>
            <td id="case1"><img src="cards/QH.svg"></td>
          </tr>
          <tr>
            <td id="case2"><img src="cards/JC.svg"></td>
            <td id="case3"><img src="cards/10D.svg"></td>
          </tr>
        </table>
      </div>"""

    case0 = document.querySelector("#case0")
    case0.setAttribute("style", "background-color: lime")
