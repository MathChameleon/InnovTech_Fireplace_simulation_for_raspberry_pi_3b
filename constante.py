#............................................Definition des types creer
Scenario = tuple[tuple[int, float]]
ScenariosCollection = tuple[Scenario]

#............................................Definition des pins
#LEDs
PIN_Y = 4
PIN_R = 17
PIN_W = 27

#boutons
PIN_BTN_BLACK = 24
PIN_BTN_RED = 23
PIN_BTN_ON_OFF = 25

#Afficheur 2x7segments
PIN_A = 6
PIN_B = 13
PIN_C = 19
PIN_D = 26
PIN_E = 21
PIN_F = 20
PIN_G = 16
PIN_LEFT = 22
PIN_RIGHT = 5


#............................................restranscription chiffre pour le 7 segments
valeur_segments = {
    0 : [PIN_A,PIN_B,PIN_C,PIN_D,PIN_E,PIN_F],
    1 : [PIN_B,PIN_C],
    2 : [PIN_A,PIN_B,PIN_D,PIN_E,PIN_G],
    3 : [PIN_A,PIN_B,PIN_C,PIN_D,PIN_G],
    4 : [PIN_B,PIN_C,PIN_F,PIN_G],
    5 : [PIN_A,PIN_C,PIN_D,PIN_F,PIN_G],
    6 : [PIN_A,PIN_C,PIN_D,PIN_E,PIN_F,PIN_G],
    7 : [PIN_A,PIN_B,PIN_C],
    8 : [PIN_A,PIN_B,PIN_C,PIN_D,PIN_E,PIN_F,PIN_G],
    9 : [PIN_A,PIN_B,PIN_C,PIN_D,PIN_F,PIN_G],
}



#............................................Scenarios
scenarios: ScenariosCollection = (
    # Colonne Rouge
    (
        (23, 1),
        (5, 0.5),
        (11, 1),
        (21, 1.5),
        (18, 0.5),
        (16, 1),
        (29, 0.5),
        (9, 0.5),
        (7, 1),
        (8, 0.5),
        (13, 1),
        (4, 0.5),
        (24, 1),
        (25, 1),
        (1, 1.5),
        (10, 0.5),
        (17, 1),
        (19, 0.5),
        (12, 1.5),
        (6, 0.5),
        (28, 1),
        (20, 0.5),
        (30, 1),
        (14, 1.5),
        (22, 1.5),
        (3, 0.5),
        (27, 0.5),
        (2, 1),
        (15, 1.5),
        (26, 0.5),
    ),
    # Colonne Jaune/Orange
    (
        (11, 0.5),
        (20, 1),
        (30, 0.5),
        (5, 1),
        (29, 1.5),
        (7, 0.5),
        (21, 1),
        (10, 0.5),
        (17, 0.5),
        (26, 1.5),
        (2, 0.5),
        (23, 1),
        (18, 1.5),
        (4, 0.5),
        (14, 1),
        (22, 0.5),
        (15, 1),
        (3, 0.5),
        (28, 1),
        (19, 0.5),
        (13, 0.5),
        (8, 1),
        (1, 0.5),
        (16, 1.5),
        (9, 0.5),
        (12, 1),
        (6, 0.5),
        (25, 1.5),
        (27, 0.5),
        (24, 1),
    ),
    # Colonne Blanc
    (
        (20, 0.5),
        (5, 0.5),
        (3, 1),
        (23, 0.5),
        (24, 0.5),
        (4, 1.5),
        (14, 0.5),
        (26, 0.5),
        (16, 1.5),
        (15, 0.5),
        (27, 1),
        (25, 0.5),
        (1, 1.5),
        (29, 1.5),
        (17, 0.5),
        (7, 1),
        (21, 0.5),
        (11, 0.5),
        (18, 1.5),
        (8, 0.5),
        (12, 1.5),
        (6, 0.5),
        (13, 1),
        (30, 0.5),
        (10, 1.5),
        (2, 0.5),
        (28, 1),
        (19, 0.5),
        (22, 1),
        (9, 0.5),
    ),
)
