import pigpio, asyncio
import maths
from constante import *

pi = pigpio.pi()

# setup pwm de chaque led : frequence ->200 et range-> 100(car on veut un pourcentage)
pi.set_PWM_frequency(PIN_Y, 200)
pi.set_PWM_range(PIN_Y, 100)
pi.set_PWM_frequency(PIN_R, 200)
pi.set_PWM_range(PIN_R, 100)
pi.set_PWM_frequency(PIN_W, 200)
pi.set_PWM_range(PIN_W, 100)
#on met les btns en pull down 
pi.set_pull_up_down(PIN_BTN_RED, pigpio.PUD_DOWN)
pi.set_pull_up_down(PIN_BTN_BLACK, pigpio.PUD_DOWN)

manual_value=0 # variable globale pour la commande manuel de l'utilisateur à ajouter à la valeur du scenario


async def manual_control():
    """
    Lit les boutons pour augmenter ou diminuer la valeur de l'intensité lumineuse(de la commande manuel)

    Args:
        Aucun
    Return:
        Aucun
    """
    global manual_value # on utilise la variable globale pour pouvoir y avoir acces partout
     # on limite la valeur de la commande manuel à 70 pour ne pas depasser les 100% d'intensité lumineuse
    if (pi.read(PIN_BTN_RED) == 1) and (manual_value < 70):
        manual_value += 1 
    # on limite la valeur de la commande manuel à 0 pour ne pas avoir une intensité lumineuse négative
    elif (pi.read(PIN_BTN_BLACK) == 1) and (manual_value > 0):
        manual_value -= 1

async def read_buttons():
    """
    Appel la fonction de lecture des boutons pour la commande manuel de l'utilisateur toutes les 50ms

    Args:
        Aucun
    Return:
        Aucun
    """
    # on lit les boutons toutes les 50ms pour ne pas surcharger la raspberry et pour l'utilisateur 
    while True:
        await manual_control() # on lit les boutons pour la commande manuel de l'utilisateur
        await asyncio.sleep(0.05)  # on lit les boutons toutes les 50ms

async def led_write(pin: int, scenario_led: Scenario):
    """
    Envoit un signal PWM du scenario avec une interpollation lineaire entre chaque valeur du scenario
    et y ajoute la valeur de la commande manuel de l'utilisateur pour controler l'intensité lumineuse de la led
    Args:
        pin (int): Le pin de la led à controler
        scenario_led (Scenario): Le scenario à appliquer sur la led
    Return:
        Aucun
    """
    # pour chaque valeur du scenario
    for i in range(29):
        #fait une interpollation lineaire entre la valeur actuelle et celle d'apres 
        #sur le temps donner par le scenario
        async for value in maths.lerp_over_time(
            scenario_led[i][0], scenario_led[i + 1][0], scenario_led[i][1], 0.01
        ):
            pi.set_PWM_dutycycle(pin, value+manual_value)# on ajoute la valeur de la commande manuel à la valeur du scenario 


async def lancement_led():
    """
    Lance la tache asynchrone des leds et des boutons
    Args:
        Aucun
    Return:
        Aucun
    """
    btn_task = asyncio.create_task(read_buttons())#on lance la tache de la lecture des boutons
    # on lance les scenarios des leds en asynchrone pour pouvoir controler les boutons en meme temps 
    #et ne pas bloquer la lecture des boutons pendant les scenarios
    async with asyncio.TaskGroup() as tg:
        tg.create_task(led_write(PIN_R, scenarios[0]))
        tg.create_task(led_write(PIN_Y, scenarios[1]))
        tg.create_task(led_write(PIN_W, scenarios[2]))
    btn_task.cancel() # on arrete la lecture des boutons une fois le scenario fini