import pigpio, asyncio
import maths
from constante import *

pi = pigpio.pi()

async def segment():
    """
    Permet de faire le compte à rebours de 25 secondes sur un afficheur 7 segments    
    Args:
        Aucun
    Return:
        Aucun
    """
    i=0 # variable pour faire le compte à rebours pendant 1 seconde
    secondes = 0 # variable pour le compte à rebours de 25 secondes
    while(secondes<=25): # tant que le compte à rebours de 25 secondes n'est pas fini
        nb_gauche = secondes//10 # chiffre des dizaines
        nb_droite = secondes%10 # chiffre des unités
        # on affiche les chiffres sur les 7 segments pendant 1 seconde 
        #(on prend en compte le temps d'execution de la raspberry pour faire le compte à rebours plus précis)
        while(i<=85): 
            # on affiche le chiffre des dizaines sur les segments de gauche et celui des unités sur les segments de droite 
            #(en faisant du multiplexage)
            for led in valeur_segments[nb_gauche]: # pour chaque segments du chiffre des dizaines
                pi.write(led,0) # on allume le segment
                pi.write(PIN_LEFT,1) # on allume le coté de gauche
                pi.write(PIN_RIGHT,0) # on eteint le coté de droite
                await asyncio.sleep(0.0001) #on attend 0.1ms pour que l'oeil puisse percevoir le chiffre
            for led in valeur_segments[nb_gauche]: # pour chaque segments du chiffre des dizaines
                pi.write(led,1) #on remet les segments du chiffre des dizaines à 1 pour les eteindre
            for led in valeur_segments[nb_droite]: # pour chaque segments du chiffre des unités
                pi.write(led,0) # on allume le segment
                pi.write(PIN_RIGHT,1) # on allume le coté de droite
                pi.write(PIN_LEFT,0) # on eteint le coté de gauche
                await asyncio.sleep(0.0001) #on attend 0.1ms pour que l'oeil puisse percevoir le chiffre
            for led in valeur_segments[nb_droite]: # pour chaque segments du chiffre des unités
                pi.write(led,1) #on remet les segments du chiffre des unités à 1 pour les eteindre
            i=i+1 # on augmente le compteur pour faire le compte à rebours pendant 1 seconde
        i=0 # on remet le compteur à 0 pour le prochain chiffre
        secondes = secondes+1 # on augmente le nombre de secondes pour faire le compte à rebours

async def lancement_afficheur():
    """
    Lance la tache asynchrone de l'afficheur
    Args:
        Aucun
    Return:
        Aucun
    """
    # on remet tous les segments à 1 pour les eteindre avant de lancer le compte à rebours
    for led in [PIN_A,PIN_B,PIN_C,PIN_D,PIN_E,PIN_F,PIN_G]:
        pi.write(led,1)
    # on lance le compte à rebours de 25 secondes sur l'afficheur 7 segments en asynchrone pour ne pas bloquer les autres taches
    async with asyncio.TaskGroup() as tg:
        tg.create_task(segment())