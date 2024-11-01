from time import time
from matplotlib.pyplot import plot


# Complexité : O (hauteur)

def affichage (piles):

    print ("a |", " ".join (piles[0]))
    print ("b |", " ".join (piles[1]))
    print ("c |", " ".join (piles[2]))
        
    print ()


# Complexité : O (1)

def deplacer (piles, depart, arrivee):

    piles[arrivee].append (piles[depart][-1])
    piles[depart].pop ()


# Complexité : O (2 ^ hauteur)
# (Suite géométrique de raison 2)

def hanoiRec (piles, hauteur, depart, arrivee, passage):
    
    operations = 0
    
    
    # Cas récursif
    
    if hauteur != 0:
    
        operations += hanoiRec (piles, hauteur - 1, depart, passage, arrivee)
        deplacer (piles, depart, arrivee)
        operations += 1
        operations += hanoiRec (piles, hauteur - 1, passage, arrivee, depart)
        
    return operations


# Complexité : O (2 ^ hauteur)

def hanoi (hauteur):

    print ("Hauteur :", hauteur, '\n')
    
    temps = time ()


    # Complexité : O (hauteur)

    piles = [[
        str (crepe)
        for crepe in range (hauteur, 0, -1)
    ], list (), list()]
    
    
    # Complexité : O (2 ^ hauteur)
    
    affichage (piles)
    operations = hanoiRec (piles, hauteur, 0, 1, 2)
    affichage (piles)
    
    print ("Nombre d'opérations effectuées :", operations)
    
    temps = time () - temps
    print ("Temps écoulé (en ms) :", int (1000 * temps), '\n' + "-" * 42 + '\n')
    

# Complexité : O (2 ^ hauteur)

def main ():

    antecedents = list (range (24))
    images = list (map (hanoi, antecedents))
    
    plot (antecedents, images)


main ()
