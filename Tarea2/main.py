import random, time, pygame, sys
from pygame.locals import *
from funciones import *
from constantes import *

def main():
    global RELOGFPS, PANTALLA, FUENTEBASICA, FUENTETITULO
    pygame.init()
    RELOGFPS = pygame.time.Clock()
    PANTALLA = pygame.display.set_mode((ANCHOPANTALLA, LARGOPANTALLA))
    FUENTEBASICA = pygame.font.Font('freesansbold.ttf', 18)
    FUENTETITULO = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption(TITULO)

    mostrarTextoPantalla(TITULO)
    while True: # LOOP DEL JUEGO
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load('music/tetrisb.mid')
        else:
            pygame.mixer.music.load('music/tetrisc.mid')
        pygame.mixer.music.play(-1, 0.0)
        marcador=iniciarJuego()
        pygame.mixer.music.stop()
        mostrarTextoPantalla('Game Over')


def iniciarJuego():

    # AJUSTES PARA INICIO DEL JUEGO
    tablero = obtenerTableroEnBlanco()
    ultMovPiezaCayendo = time.time()
    ultMovSecundario = time.time()
    ultimoTiempoDeCaida = time.time()
    movimientoHaciaAbajo = False
    movimientoHaciaIzquierda = False
    movimientoHaciaDerecha = False
    marcaLlevada = 0
    nivel, frecuenciaCaida = calculoNivelYFrecuenciaCaida(marcaLlevada)

    piezaCayendo = obtenerNuevaPieza()
    piezaSiguiente = obtenerNuevaPieza()

    while True: # LOOP DEL JUEGO

        if piezaCayendo == None:
            # SI NO HAY UNA PIEZA CAYENDO EN EL JUEGO, SE INICIA UNA NUEVA EN LA PARTE SUPERIOR
            piezaCayendo = piezaSiguiente
            piezaSiguiente = obtenerNuevaPieza()
            ultimoTiempoDeCaida = time.time() # REINICIO EL TIEMPO DE ultimoTiempoDeCaida

            if not esPosicionValida(tablero, piezaCayendo):
                return (nivel*frecuenciaCaida) # SI NO SE PUEDE PONER MAS PIEZAS EN EL TABLERO, SE ACABA EL JUEGO

        verificaSalida()
        for event in pygame.event.get(): # EVENTO DURANTE EL PROGRAMA
            if event.type == KEYUP:
                if (event.key == K_p):
                    # PARA PAUSAR EL JUEGO
                    PANTALLA.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    mostrarTextoPantalla('Pausa') # AL PRESIONAR LA TECLA p PARA PAUSAR
                    pygame.mixer.music.play(-1, 0.0)
                    ultimoTiempoDeCaida = time.time()
                    ultMovPiezaCayendo = time.time()
                    ultMovSecundario = time.time()

                elif (event.key == K_LEFT or event.key == K_a):
                    movimientoHaciaIzquierda = False #MOVIMEINTO HACIA LA IZQUIERDA
                elif (event.key == K_RIGHT or event.key == K_d):
                    movimientoHaciaDerecha = False #MOVIMIENTO HACIA LA DERECHA
                elif (event.key == K_DOWN or event.key == K_s):
                    movimientoHaciaAbajo = False #MOVIMIENTO HACIA ABAJO

            elif event.type == KEYDOWN:
                # SE CAMBIA DE POSICION LA PIEZA
                if (event.key == K_LEFT or event.key == K_a) and esPosicionValida(tablero, piezaCayendo, adjX=-1):
                    piezaCayendo['x'] -= 1
                    movimientoHaciaIzquierda = True
                    movimientoHaciaDerecha = False
                    ultMovSecundario = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and esPosicionValida(tablero, piezaCayendo, adjX=1):
                    piezaCayendo['x'] += 1
                    movimientoHaciaDerecha = True
                    movimientoHaciaIzquierda = False
                    ultMovSecundario = time.time()

                # ROTACION DE LA PIEZA
                elif (event.key == K_UP or event.key == K_w):
                    piezaCayendo['rotacion'] = (piezaCayendo['rotacion'] + 1) % len(PIEZAS[piezaCayendo['forma']])
                    if not esPosicionValida(tablero, piezaCayendo):
                        piezaCayendo['rotacion'] = (piezaCayendo['rotacion'] - 1) % len(PIEZAS[piezaCayendo['forma']])
                elif (event.key == K_q): # rotate the other direction
                    piezaCayendo['rotacion'] = (piezaCayendo['rotacion'] - 1) % len(PIEZAS[piezaCayendo['forma']])
                    if not esPosicionValida(tablero, piezaCayendo):
                        piezaCayendo['rotacion'] = (piezaCayendo['rotacion'] + 1) % len(PIEZAS[piezaCayendo['forma']])

                # CREA LA CAIDA RAPIDA DE LAS PIEZAS
                elif (event.key == K_DOWN or event.key == K_s):
                    movimientoHaciaAbajo = True
                    if esPosicionValida(tablero, piezaCayendo, adjY=1):
                        piezaCayendo['y'] += 1
                    ultMovPiezaCayendo = time.time()

                # CREA LA CAIDA INSTANTANEA DE LAS PIEZAS
                elif event.key == K_SPACE:
                    movimientoHaciaAbajo = False
                    movimientoHaciaIzquierda = False
                    movimientoHaciaDerecha = False
                    for i in range(1, LARGOTABLERO):
                        if not esPosicionValida(tablero, piezaCayendo, adjY=i):
                            break
                    piezaCayendo['y'] += i - 1

        # CONTROL DE MOVIMEINTO DE LAS PIEZAS SEGUN EL USUARIO
        if (movimientoHaciaIzquierda or movimientoHaciaDerecha) and time.time() - ultMovSecundario > FRECUENCIAMOVFORMAS:
            if movimientoHaciaIzquierda and esPosicionValida(tablero, piezaCayendo, adjX=-1):
                piezaCayendo['x'] -= 1
            elif movimientoHaciaDerecha and esPosicionValida(tablero, piezaCayendo, adjX=1):
                piezaCayendo['x'] += 1
            ultMovSecundario = time.time()

        if movimientoHaciaAbajo and time.time() - ultMovPiezaCayendo > FRECUENCIAMOVCAIDA and esPosicionValida(tablero, piezaCayendo, adjY=1):
            piezaCayendo['y'] += 1
            ultMovPiezaCayendo = time.time()

        # SE DEJA CAERA LA PEIZA SI ES NECESARIO
        if time.time() - ultimoTiempoDeCaida > frecuenciaCaida:
            # COMPRUEBA SI LA PIEZA ATERRIZO
            if not esPosicionValida(tablero, piezaCayendo, adjY=1):
                # SI LA PIEZA CAYO, LA FIJA EN EL TABLERO
                agregarTablero(tablero, piezaCayendo)
                marcaLlevada += removerLineaCompleta(tablero)
                nivel, frecuenciaCaida = calculoNivelYFrecuenciaCaida(marcaLlevada)
                piezaCayendo = None
            else:
                # SI LA PIEZA NO CAYO, LA SIGUE BAJANDO
                piezaCayendo['y'] += 1
                ultimoTiempoDeCaida = time.time()

        # DIBUJA LA PANTALLA
        PANTALLA.fill(BGCOLOR)
        drawtablero(tablero)
        insertaEstado(marcaLlevada, nivel)
        dibujadorPiezaSiguiente(piezaSiguiente)
        if piezaCayendo != None:
            dibujadorDePiezas(piezaCayendo)

        pygame.display.update()
        RELOGFPS.tick(FPS)


def creadorDeTextos(texto, fuente, color):
    flotante = fuente.render(texto, True, color)
    return flotante, flotante.get_rect()


def exterminio():
    pygame.quit()
    sys.exit()


def compTeclaPresionada():
    # Comprueba si la tecla Arrbia o Abajo esta precionada
    verificaSalida()
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def mostrarTextoPantalla(texto,situacion=True,record=0):
    if situacion:
        # Esta funcion esta encargada de motras los textos en pantalla
        tituloFlotante, tituloRect = creadorDeTextos(texto, FUENTETITULO, TEXTOCOLORESOMBRA)
        tituloRect.center = (int(ANCHOPANTALLA / 2), int(LARGOPANTALLA / 2))
        PANTALLA.blit(tituloFlotante, tituloRect)

        # Dibuja el texto
        tituloFlotante, tituloRect = creadorDeTextos(texto, FUENTETITULO, COLORTEXTO)
        tituloRect.center = (int(ANCHOPANTALLA / 2) - 3, int(LARGOPANTALLA / 2) - 3)
        PANTALLA.blit(tituloFlotante, tituloRect)

        # Dibuja el inicio para comenzar
        presionarTeclaFlotante, presionarTeclaRect = creadorDeTextos('Presiona una tecla para empezar.', FUENTEBASICA, COLORTEXTO)
        presionarTeclaRect.center = (int(ANCHOPANTALLA / 2), int(LARGOPANTALLA / 2) + 100)
        PANTALLA.blit(presionarTeclaFlotante, presionarTeclaRect)
    else:# Esta funcion esta encargada de motras los textos en pantalla
        tituloFlotante, tituloRect = creadorDeTextos(texto, FUENTETITULO, TEXTOCOLORESOMBRA)
        tituloRect.center = (int(ANCHOPANTALLA / 2), int(LARGOPANTALLA / 2)-50)
        PANTALLA.blit(tituloFlotante, tituloRect)

        # Dibuja el texto
        tituloFlotante, tituloRect = creadorDeTextos(texto, FUENTETITULO, COLORTEXTO)
        tituloRect.center = (int(ANCHOPANTALLA / 2) - 3, int(LARGOPANTALLA / 2) - 3 -50)
        PANTALLA.blit(tituloFlotante, tituloRect)

        # Dibuja record
        tituloFlotante, tituloRect = creadorDeTextos("Record: %s" % record, FUENTETITULO, COLORTEXTO)
        tituloRect.center = (int(ANCHOPANTALLA / 2) - 3, int(LARGOPANTALLA / 2) + 50)
        PANTALLA.blit(tituloFlotante, tituloRect)

        # Dibuja el inicio para comenzar
        presionarTeclaFlotante, presionarTeclaRect = creadorDeTextos('Presiona una tecla para empezar.', FUENTEBASICA, COLORTEXTO)
        presionarTeclaRect.center = (int(ANCHOPANTALLA / 2), int(LARGOPANTALLA / 2) + 120)
        PANTALLA.blit(presionarTeclaFlotante, presionarTeclaRect)


    while compTeclaPresionada() == None:
        pygame.display.update()
        RELOGFPS.tick()


def verificaSalida():
    for event in pygame.event.get(QUIT): # Obtiene la salida de los eventos
        exterminio() # Cierra el juego
    for event in pygame.event.get(KEYUP): # comprueba si esta presiona la tecla ESC
        if event.key == K_ESCAPE:
            exterminio() # Cierra el juego
        pygame.event.post(event)

def convertirApixelCoord(boxx, boxy):
    # Convierte las coordenas XY del tablero
    # y las coodrina con la pantalla
    return (MARGENX + (boxx * TAMANIOCAJA)), (MARGENARRIBA + (boxy * TAMANIOCAJA))


def dibujarCaja(boxx, boxy, color, pixelx=None, pixely=None):
    # Dibuja una casilla (Cada pieza del juego tiene cuatro cajas)
    # en las coordenadas xy en el tablero , y si se especifican las coordenadas pixelX y pixely
    # se especifican , se dibuja segun la indicacion de estas.
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertirApixelCoord(boxx, boxy)
    pygame.draw.rect(PANTALLA, COLORES[color], (pixelx + 1, pixely + 1, TAMANIOCAJA - 1, TAMANIOCAJA - 1))
    pygame.draw.rect(PANTALLA, COLORESCLAROS[color], (pixelx + 1, pixely + 1, TAMANIOCAJA - 4, TAMANIOCAJA - 4))


def drawtablero(tablero):
    # Dibuja los bordes del tablero
    pygame.draw.rect(PANTALLA, COLORBORDE, (MARGENX - 3, MARGENARRIBA - 7, (ANCHOTABLERO * TAMANIOCAJA) + 8, (LARGOTABLERO * TAMANIOCAJA) + 8), 5)

    # Colaca el fondo del tablero
    pygame.draw.rect(PANTALLA, BGCOLOR, (MARGENX, MARGENARRIBA, TAMANIOCAJA * ANCHOTABLERO, TAMANIOCAJA * LARGOTABLERO))
    # Dibuja las casillas individuales del tablero
    for x in range(ANCHOTABLERO):
        for y in range(LARGOTABLERO):
            dibujarCaja(x, y, tablero[x][y])


def insertaEstado(marcaLlevada, nivel):
    # Dibuja las marcas de record llevadas en el juego
    marcaLlevadaFlotante = FUENTEBASICA.render('Marca: %s' % marcaLlevada, True, COLORTEXTO)
    marcaLlevadaRect = marcaLlevadaFlotante.get_rect()
    marcaLlevadaRect.topleft = (ANCHOPANTALLA - 150, 20)
    PANTALLA.blit(marcaLlevadaFlotante, marcaLlevadaRect)

    nivelActual = FUENTEBASICA.render('Nivel: %s' % nivel, True, COLORTEXTO)
    rectNivel = nivelActual.get_rect()
    rectNivel.topleft = (ANCHOPANTALLA - 150, 50)
    PANTALLA.blit(nivelActual, rectNivel)

def dibujadorDePiezas(pieza, pixelx=None, pixely=None):
    formarDibujo = PIEZAS[pieza['forma']][pieza['rotacion']]
    if pixelx == None and pixely == None:
        # Si no se ha especificado el pixelX y pixely , utilza la ubicacion
        # almacenada en la estructura de datos "pieza"
        pixelx, pixely = convertirApixelCoord(pieza['x'], pieza['y'])

    # Dibuja cada una de las cajas que componen la pieza
    for x in range(ANCHOTEMPLATE):
        for y in range(LARGOTEMPLATE):
            if formarDibujo[y][x] != BLANK:
                dibujarCaja(None, None, pieza['color'], pixelx + (x * TAMANIOCAJA), pixely + (y * TAMANIOCAJA))

def dibujadorPiezaSiguiente(pieza):
    siguienteFlotante = FUENTEBASICA.render('Siguiente:', True, COLORTEXTO)
    siguienteRect = siguienteFlotante.get_rect()
    siguienteRect.topleft = (ANCHOPANTALLA - 120, 80)
    PANTALLA.blit(siguienteFlotante, siguienteRect)
    dibujadorDePiezas(pieza, pixelx=ANCHOPANTALLA-120, pixely=100)

def calculoNivelYFrecuenciaCaida(marca):
    # Retorna el nivel en el que se encuentra el jugador 
    # y el aumento de segundos que deben pasar para 
    # aumentar la frecuencia de caida de una pieza.
    nivel = int(marca / 10) + 1
    frecuenciaCaida = 0.27 - (nivel * 0.02)
    return nivel, frecuenciaCaida
    
if __name__ == '__main__':
    main()