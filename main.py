import pigpio, asyncio
import maths
from constante import *
from led import *
from afficheur import *

pi = pigpio.pi()
pi.set_pull_up_down(PIN_BTN_ON_OFF, pigpio.PUD_DOWN)

async def main():
    """
    Lance le lancement des leds et de l'afficheur en meme temps

    Args:
        Aucun
    Return:
        Aucun
    """
    # on lance les scenarios des leds et de l'afficheur en asynchrone pour pouvoir les faire en meme temps
    async with asyncio.TaskGroup() as tg:
        tg.create_task(lancement_led())
        tg.create_task(lancement_afficheur())


if __name__ == "__main__":
    # on lance la fonction main qui lance les scenarios des leds et de l'afficheur en meme temps dans une boucle infinie
    while True:
        # on verifie si le bouton on/off est appuyé pour lancer les scenarios des leds et de l'afficheur
        if pi.read(PIN_BTN_ON_OFF) == 1:
            asyncio.run(main())
        # sinon on eteint les leds et l'afficheur pour economiser de l'energie et pour ne pas surcharger la raspberry
        else:
            for led in [PIN_Y, PIN_R, PIN_W,PIN_LEFT,PIN_RIGHT]:
                pi.write(led, 0)
            for led in [PIN_A,PIN_B,PIN_C,PIN_D,PIN_E,PIN_F,PIN_G]:
                pi.write(led,1)
            