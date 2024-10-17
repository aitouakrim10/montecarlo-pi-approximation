#!/usr/bin/env python3 
""" Deuxième partie : génération d'images PPM puis d'un GIF """
import sys
from  random import choice
import subprocess
from  approximate_pi import appartient_au_cercle_unitaire ,generer_points
try:
    RED     = "255 0 0      "
    BLEU    = "0 0 255      "
    WHITE   = "255 255 255      "
    BLACK   = "0 0 0      "
    ORANGE  = "170  0  0 "
    subprocess.run("rm -f ./images/*.ppm  ./images/pii_value.gif ", shell=True, check=True)
    taille_image = int(sys.argv[1])
    nombre_des_points =int(sys.argv[2])*10//100
    nombre_de_chiffres_apres_la_virgule = int(sys.argv[3])
    largeur = taille_image //(40)
    hauteur = 2*largeur
    if taille_image  >= 100:
        if int(sys.argv[2]) >=100:
            if 1<=int(sys.argv[3])<=5:
                def multiple(point,valeur):
                    """renvoie le point dont les cordonneé sont celle de 'point' multiplier par 'valeur' et prendre just les paties entieres des valeurs """
                    point.x = (point.x*valeur)//1
                    point.y = (point.y*valeur)//1

                def fonction_adaptage(var):
                    """fonction utulise pour adapter les points pour le traçage """
                    return  ((taille_image*var-1)/(2) + taille_image/2)//1




                def transfert_points(point):
                    """pour representer les point il faut faire une adaptage car on a un grande nombre des point et un nombre de pixels et determiner """   
                    point.x= int(fonction_adaptage(point.x)//1)
                    point.y=int(fonction_adaptage(point.y)//1)
                    return point

                def segmant_horizontale(list0,abcisse,ordonee,taille):
                    """allumer une segmant verticale"""
                    for i in range(taille):
                        #for eps in range(taille_image//100) :
                        list0[abcisse-1][i+ordonee]=BLACK
                        list0[abcisse][i+ordonee]=BLACK
                        list0[abcisse+1][i+ordonee]=BLACK
                def segmant_verticale(list1,abcisse,ordonee,taille):
                    """allumer une segmant horizontale """
                    for i in range(taille):
                        #for eps in range(taille_image//100) :
                        list1[abcisse+i][ordonee-1]=BLACK
                        list1[abcisse+i][ordonee]=BLACK
                        list1[abcisse+i][ordonee+1]=BLACK



                if int(sys.argv[2]) > 500000:
                    L= [ORANGE,RED,ORANGE,RED,ORANGE, ORANGE]
                else :
                    L= [WHITE,ORANGE,RED,WHITE,WHITE,WHITE]
                def eteindre_segmant_horizontale(list0,abcisse,ordonee,taille):
                    """allumer une segmant verticale"""
                    for i in range(taille):
                        #for eps in range(taille_image//100) :
                        list0[abcisse-1][i+ordonee]=choice(L)
                        list0[abcisse][i+ordonee]=choice(L)
                        list0[abcisse+1][i+ordonee]=choice(L)
                def eteindre_segmant_verticale(list1,abcisse,ordonee,taille):
                    """allumer une segmant horizontale """
                    for i in range(taille):
                        #for eps in range(taille_image//100) :
                        list1[abcisse+i][ordonee+1]=choice(L)
                        list1[abcisse+i][ordonee]=choice(L)
                        list1[abcisse+i][ordonee-1]=choice(L)



                def virgule(liste3,ordonner,taille):
                    """tracer la virgule"""
                    for i in range(taille):
                        for j in range(taille) :
                            liste3[taille_image//2+hauteur-j][ordonner+i]=BLACK

                def allumer_chiffre(data,nomber,ordonner):
                    """tracer un chiffre"""
                    if nomber=='0':
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        #segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur) 
                    elif nomber == "1":
                        #segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        #segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        #segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="2":
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="3":
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="4":        
                        #segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        #segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="5":
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)

                    elif nomber=="6":
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="7":
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        #segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        #segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="8":
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    else:
                        segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)



                def eteindre_chiffre(data,nomber,ordonner):
                    """tracer un chiffre"""
                    if nomber=='0':
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        #eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur) 
                    elif nomber == "1":
                        #eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        #eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        #eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="2":
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="3":
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="4":        
                        #eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        #eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="5":
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)

                    elif nomber=="6":
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="7":
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        #eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        #eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        #eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    elif nomber=="8":
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)
                    else:
                        eteindre_segmant_horizontale(data,taille_image//2-hauteur,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2,ordonner,largeur)
                        eteindre_segmant_horizontale(data,taille_image//2+hauteur,ordonner,largeur)

                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner,hauteur)
                        #eteindre_segmant_verticale(data,taille_image//2,ordonner,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2-hauteur,ordonner+largeur,hauteur)
                        eteindre_segmant_verticale(data,taille_image//2,ordonner+largeur,hauteur)



                def taper_pi(data,pi_str,debut,fichier):
                    """graver la valeur de oi dans l'image"""
                    file = open(fichier,'w',encoding='UTF-8')
                    espace =taille_image*3//100 +largeur
                    #pi_str = str(pi_valeur)+"0000"
                    gomme =debut
                    allumer_chiffre(data,"3",debut)
                    debut += taille_image*2//100 + largeur 
                    virgule(data,debut,int(taille_image*1.5)//120)
                    debut += taille_image*2//100
                    for ind in range(nombre_de_chiffres_apres_la_virgule) :
                        allumer_chiffre(data,pi_str[2+ind],debut) 
                        debut += espace
                    file .write("P3\n"+str(taille_image)+" " +str(taille_image)+"\n255\n")
                    for i in range (taille_image):
                        ligne ="".join(data[i])
                        file .write(ligne +"\n" )
                    eteindre_chiffre(data,"3",gomme)
                    gomme += taille_image*2//100 + largeur 
                    #virgule(data,debut,taille_image*2//100)
                    gomme += taille_image*2//100
                    for ind in range(nombre_de_chiffres_apres_la_virgule) :
                            eteindre_chiffre(data,pi_str[2+ind],gomme) 
                            gomme += espace    
                    file.close()
                def generate_ppm_file():
                    """generer une fichier.ppm """
                    data=[[WHITE for i in range(taille_image)] for i in range(taille_image)]
                    N,n=0,0
                    for ind in range(10):
                        liste = generer_points(nombre_des_points)
                        N+=nombre_des_points
                        for point in liste :
                            if appartient_au_cercle_unitaire(point):
                                n+=1
                                point=transfert_points(point)
                                data[point.x][point.y]= RED
                            else :         
                                point =transfert_points(point) 
                                data[point.x][point.y]= BLEU
                        pi_str =str(4*n/N)+'0000'
                        nom_fichier =f'./images/img{ind}_3-{pi_str[2:nombre_de_chiffres_apres_la_virgule+2]}.ppm'
                        taper_pi(data,pi_str,3*taille_image//10,nom_fichier)
                generate_ppm_file()
                subprocess.run(" convert -delay 50  ./images/*.ppm ./images/pii_value.gif   ", shell=True, check=True)
            else:
                print("le nombre de chiffres après la virgule est un entier  entre 1 et 5 ")    
        else:
            print("le nombre des points doit etre un entier  superieur à 100")
    else :
        print(" la taille d'image doit etre un entier  superieur à 100 ")


except (IndexError ,ValueError) :
    print("syntaxe: draw.py  [taille d'image : entier >= 100 ] [nombre de points : entier>=100] [nombre de chiffres après la virgule:1<=entier<=5]")              
            
           
#generate_ppm_file()
#subprocess.run("convert -delay 50  *.ppm pii_value.gif   ", shell=True, check=True)








          
#def generate_ppm_file(data,pi_str,debut,fichier):
#    """graver la valeur de oi dans l'image"""
#    file = open(fichier,'w',encoding='UTF-8')
#    espace =taille_image*3//100 +largeur
#    data1=deepcopy(data)
#    #pi_str = str(pi_valeur)+"0000"
#    #gomme =debut
#    allumer_chiffre(data1,"3",debut)
#    debut += taille_image*2//100 + largeur 
#    virgule(data1,debut,int(taille_image*1.5)//100)
#    debut += taille_image*2//100
#    for ind in range(nombre_de_chiffres_apres_la_virgule) :
#        allumer_chiffre(data1,pi_str[2+ind],debut) 
#        debut += espace
#    file .write("P3\n"+str(taille_image)+" " +str(taille_image)+"\n255\n")
#    for i in range (taille_image):
#        ligne ="".join(data1[i])
#        file .write(ligne +"\n" )
#    #eteindre_chiffre(data,"3",gomme)
#    #gomme += taille_image*2//100 + largeur 
#    ##virgule(data,debut,taille_image*2//100)
#    #gomme += taille_image*2//100
#    #for ind in range(nombre_de_chiffres_apres_la_virgule) :
#    #    eteindre_chiffre(data,pi_str[2+ind],gomme) 
#    #    gomme += espace    
#    file.close()


#def main():
#    """generer une fichier.ppm """
#    data=[[WHITE for i in range(taille_image)] for i in range(taille_image)]
#    N,n=0,0
#    for ind in range(10):
#        liste = generer_points(nombre_des_points)
#        N+=nombre_des_points
#        for point in liste :
#            if appartient_au_cercle_unitaire(point):
#                n+=1
#                point=transfert_points(point)
#                data[point.x][point.y]= RED
#            else :         
#                point =transfert_points(point) 
#                data[point.x][point.y]= BLEU
#        pi_str =str(4*n/N)+'0000'
#        nom_fichier =f'img{ind}_3-{pi_str[2:nombre_de_chiffres_apres_la_virgule+2]}.ppm'
#        generate_ppm_file(data,pi_str,3*taille_image//10,nom_fichier) 
#
#
#main()
#subprocess.run("convert -delay 50  *.ppm pi_value.gif   ", shell=True, check=True)

