#!/usr/bin/env python3
""" Première partie : cœur de la simulation """
from  math import sqrt
from random import uniform
from sys import argv
class Point :
    """creer la classe Point"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
def norm(point1,point2):
    """calculer la norme de [point1 point2]"""
    return sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)
def generer_points(nomb):
    """generer <n> points avec x appartenant à [-1,1] et y appartenant à [-1,1]"""
    ensemble_des_points = []
    for _ in range(nomb):
        ordonnee=uniform(-1,1)
        abcisse=uniform(-1,1)
        point = Point(abcisse,ordonnee)
        ensemble_des_points.append(point)    
    return  ensemble_des_points 

def appartient_au_cercle_unitaire(point)  :
    """return True si le point appartient au cercle et return False si non """
    ref =Point(0,0)
    return  norm(ref,point) <= 1 
    

def approximation_pi(nomb):
    """application de la methode de monte-carlo pour donner une approximation de pi """   
    points= generer_points(nomb)
    compteur = 0
    for point in points :
        if appartient_au_cercle_unitaire(point) :
            compteur+=1
    pii = 4*compteur/nomb
    return pii 



nombre = int(argv[1])    
print(approximation_pi(nombre))


