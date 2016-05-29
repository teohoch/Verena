FPS = 25
ANCHOPANTALLA = 640
LARGOPANTALLA = 480
TAMANIOCAJA = 20
ANCHOTABLERO = 10
LARGOTABLERO = 20
BLANK = '.'
TITULO="PyTetris USM"
FRECUENCIAMOVFORMAS = 0.15
FRECUENCIAMOVCAIDA = 0.1

MARGENX = int((ANCHOPANTALLA - ANCHOTABLERO * TAMANIOCAJA) / 2)
MARGENARRIBA = LARGOPANTALLA - (LARGOTABLERO * TAMANIOCAJA) - 5


BLANCO        = (255, 255, 255)
GRIS          = (185, 185, 185)
NEGRO         = (  0,   0,   0)
ROJO          = (155,   0,   0)
ROJOCLARO     = (175,  20,  20)
VERDE         = (  0, 155,   0)
VERDECLARO    = ( 20, 175,  20)
AZUL          = (  0,   0, 155)
AZULCLARO     = ( 20,  20, 175)
AMARILLO      = (155, 155,   0)
AMARILLOCLARO = (175, 175,  20)

COLORBORDE = AZUL
BGCOLOR = NEGRO
COLORTEXTO = BLANCO
TEXTOCOLORESOMBRA = GRIS
COLORES      = (AZUL, VERDE, ROJO, AMARILLO)
COLORESCLAROS = (AZULCLARO, VERDECLARO, ROJOCLARO, AMARILLOCLARO)
assert len(COLORES) == len(COLORESCLAROS)

ANCHOTEMPLATE = 5
LARGOTEMPLATE = 5

FORMA_S_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

FORMA_Z_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

FORMA_I_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

FORMA_O_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

FORMA_J_TEMPLATE= [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

FORMA_L_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

FORMA_T_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIEZAS = {'S': FORMA_S_TEMPLATE,
          'Z': FORMA_Z_TEMPLATE,
          'J': FORMA_J_TEMPLATE,
          'L': FORMA_L_TEMPLATE,
          'I': FORMA_I_TEMPLATE,
          'O': FORMA_O_TEMPLATE,
          'T': FORMA_T_TEMPLATE}