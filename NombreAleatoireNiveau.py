import time
from random import *

secret = 0
coup = 0
code = 222
code = int (code)
secret = int (secret)
coup = int (coup)
choix=-1

while (choix != 0) :
    print ("Choisir le niveau :")
    print ("\t0 - pour quitter")
    print ("\t1 - 1 chiffre ")
    print ("\t2 - 2 chiffre  ")
    print ("\t3 - 3 chiffre  ")
    print ("\t4 - 4 chiffre  ")
    print ("\t5 - 5 chiffre  ")

    while (choix != 0 and choix != 1 and choix != 2 and choix != 3 and choix != 4 and choix !=5) :
        choix = input ("Choix du niveau  : ")
        choix = int (choix)
        if (choix != 0):
            if (choix==1):
                code = randint(0,10)
            elif (choix==2):
                code = randint(0,100)
            elif (choix==3):
                code = randint(0,1000)
            elif (choix==4):
                code = randint(0,10000)
            elif (choix==5):
                code = randint(0,100000)
        else :
            print ("Merci d'avoir jouer")      
    
        while (secret != code and choix !=0):
                time.sleep(0.5)  
                secret = input ("Entrer le secret :")  
                secret = int (secret)
                coup = coup+1
                if (secret > code):
                    print ("  C'est moins ")
                    print ("  Le nombre de coup est de :" , coup)

                elif (secret  < code ):
                    print ("  C'est plus")
                    print ("  Le nombre coup est de : ", coup)

                else : 

                    time.sleep(1)
                    print ("Le code est bon ")
                    print ("Le nombre coup est de : ", coup)
                    exec(open("Code_simple.py").read())





