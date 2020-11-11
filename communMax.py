''' 
Auteure : Alina Weinberger - 20066963
Date : 11.11.2020

Ce programme permet de trouver la plus longue sequence de caracteres
commune a deux textes. 

'''
def communMax(txt1,txt2):
    
    commun =''
    communMax=''
    
    if len(txt1) >= len(txt2):    #definir le plus cours des textes
        plusLong = txt1          #pour minimiser les iterations
        plusCours = txt2
    else:
        plusLong = txt2
        plusCours = txt1  
        
    long1 = len(plusLong)
    long2 = len(plusCours)
    
    debut = 0 
    
    for i in range(long2):  #iterer sur le mot le plus cours
        
        chercher = True  # Vrai tant qu'on peut trouver la meme lettre 
        while chercher:  # a differents emplacement dans le 2eme mot
            
            if plusLong[i] in plusLong: #si lettre trouvé dans 2 eme mot
                commun = ''
                s = i 
                t = plusLong.find(plusCours[i],debut) #chercher l'index de
                                                      #la lettre depuis debut
                
                if t == -1: #si on ne trouve pas la lettre apres l'index debut
                    chercher = False
                    debut = 0
                    continue   # passer a la prochaine lettre 
                    
                while t < long1 and s < long2 and plusCours[s] == plusLong[t]: 
                           #tant que les lettres suivantes identiques aussi 
                    commun += plusLong[t]
                    s+=1
                    t+=1
                    
                debut = t  # mise a jour pour rechercher le prochain 
                           # emplacement de la meme lettre dans 2eme mot
                    
                if len(commun) > len(communMax): #ne retenir que la plus longue 
                    communMax = commun           #des sequences communes
                    commun = ''
                    
    return communMax

def communMaxTest():
    assert(communMax('A','A') == 'A')
    assert(communMax('','') == '')
    assert(communMax('XYZ','WFZ') == 'Z')
    assert(communMax('abc', 'ABC') == '')
    assert(communMax('abc','abc') == 'abc')
    assert(communMax('AABAACAD','AACAAB') == 'AACA')
    assert(communMax('AABAACAD','AACAABAABAA') == 'AABAA')
    assert(communMax('ACATAGGTCGTGCACTCC', 'GAGAACCGAGGTAAAGGGTC') == 'AGGT')
    
communMaxTest()
    