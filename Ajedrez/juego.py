import os
import pygame as p
from Ajedrez import movimientos
from pygame.locals import *
import time

p.init()
ventana = (480, 480)  #400 o 500 son buenas opciones para el tablero
dimension = 8  #usualmente la dimension del ajerdrez es de 8 * 8
cuadrado = 430 // dimension #los cuadrados del tablero
fps = 25 #será para las animaciones
piezas = {} #lista de las piezas
juegoIniciado = False
pantalla=None

'''
Carga las imagenes de la carpeta 'piezas'.
'''
def cargar_imagenes():
    piezas2 = ["Np","Bp","Nr","Br","Nq","Bq","Nt","Bt","Ba","Na","Nc","Bc",]
    for pieza in piezas2:
        piezas[pieza] = p.transform.scale(p.image.load("piezas/" + pieza + ".png"), (cuadrado, cuadrado))


'''
Funcion principal donde inicializa el tablero y donde se pueden ejecutar los movimientos.
'''
def graficas():
    global pantalla
    blanco = (255, 255, 255)
    pantalla = p.display.set_mode((ventana))
    tiempo = p.time.Clock()
    pantalla.fill(blanco)
    edj = movimientos.estado_de_juego()
    movimiento_valido = edj.movimientos_validos()
    movimeinto_hecho = False
    cargar_imagenes()
    ejecutar = True
    cuadrado_seleccionado = () #no se escoge un cuadrado al inicio.
    click = [] #tendra en cuenta los clics de los jugadores
    gameover = False
    while ejecutar:
        for i in p.event.get():
            if i.type == p.QUIT:
                clear()
                ejecutar = False
            elif i.type == p.KEYDOWN:
                if not gameover:
                    if i.key == p.K_w:
                        lugar = p.mouse.get_pos() #lugares en el plano del raton(mouse)
                        columna = lugar[1] // cuadrado
                        fila = lugar[0] // cuadrado
                        if cuadrado_seleccionado == (fila, columna):
                            cuadrado_seleccionado = ()
                            click = []
                        else:
                            cuadrado_seleccionado = (fila, columna)
                            click.append(cuadrado_seleccionado)
                        if len(click) == 2:
                            mover = movimientos.movimiento(click[0], click[1], edj.tablero)
                            print(mover.historial())
                            for i in range(len(movimiento_valido)):
                                if mover == movimiento_valido[i]:
                                    edj.moverse(movimiento_valido[i])
                                    movimeinto_hecho = True
                                    cuadrado_seleccionado = ()
                                    click = []
                            if not movimeinto_hecho:
                                click = [cuadrado_seleccionado]
                    elif i.key == p.K_s:  # Cuando se presione "E" se desahara el movimiento.
                        edj.quitar_movimiento()
                        movimeinto_hecho = True
                    elif i.key == p.K_a:
                        edj = movimientos.estado_de_juego()
                        movimiento_valido = edj.movimientos_validos()
                        cuadrado_seleccionado = ()
                        click = []
                        movimeinto_hecho = False



        if movimeinto_hecho:
            movimiento_valido = edj.movimientos_validos()
            movimeinto_hecho = False


        dibujar(pantalla, edj, movimiento_valido, cuadrado_seleccionado)




        if edj.jaque_mate:
            gameover = True
            if edj.movimiento_blanco:
                escribir(pantalla, "Negros ganan por ¡JAQUE MATE!", " ")
                escribir(pantalla, " ", "Presiona  'A' para volver a empezar")
                for i in p.event.get():
                    if i.type == p.KEYDOWN:
                        if i.key == p.K_a:
                            edj = movimientos.estado_de_juego()
                            movimiento_valido = edj.movimientos_validos()
                            cuadrado_seleccionado = ()
                            click = []
                            movimeinto_hecho = False
                            gameover = False
            else:
                escribir(pantalla, "Blancos ganan por ¡JAQUE MATE!", " ")
                escribir(pantalla, " ", "Presiona  'A' para volver a empezar")
                for i in p.event.get():
                    if i.type == p.KEYDOWN:
                        if i.key == p.K_a:
                            edj = movimientos.estado_de_juego()
                            movimiento_valido = edj.movimientos_validos()
                            cuadrado_seleccionado = ()
                            click = []
                            movimeinto_hecho = False
                            gameover = False





        tiempo.tick(fps)
        p.display.flip()


#Esto sera para poder ver los movimientos de las piezas antes de realizarlos.


def resaltar(pantalla, edj, movimiento_valido, cuadrado_seleccionado):
    if cuadrado_seleccionado != ():
        j, i = cuadrado_seleccionado
        if edj.tablero[j][i][0] == ('B' if edj.movimiento_blanco else 'N'):
            #resaltar pieza seleccionada
            s = p.Surface((cuadrado, cuadrado))
            s.set_alpha(100) #transparencia
            s.fill(p.Color(138,43,226))
            pantalla.blit(s, (j * cuadrado, i * cuadrado))





def dibujar(pantalla,edj, movimiento_valido, cuadrado_seleccionado):
    bienvenida(pantalla)
    tablero(pantalla)
    dibujar_piezas(pantalla, edj.tablero)
    resaltar(pantalla, edj, movimiento_valido, cuadrado_seleccionado)

def tablero(pantalla):
    global colores
    colores = [p.Color(139,125,107), p.Color("Brown")]
    for i in range(dimension): #fila
        for j in range(dimension): #columna
           color = colores[((i + j) % 2)]
           p.draw.rect(pantalla,color,p.Rect(j* cuadrado, i * cuadrado, cuadrado, cuadrado))
    posiciones = p.font.SysFont("Arial", 32, True, False)
    objetosDeTexto = posiciones.render("A", 0, p.Color(102, 0, 102))
    lugar = (440, 10)
    objetosDeTexto2 = posiciones.render("B", 0, p.Color(102, 0, 102))
    lugar2 = (440, 65)
    objetosDeTexto3 = posiciones.render("C", 0, p.Color(102, 0, 102))
    lugar3 = (440, 120)
    objetosDeTexto4 = posiciones.render("D", 0, p.Color(102, 0, 102))
    lugar4 = (440, 170)
    objetosDeTexto5 = posiciones.render("E", 0, p.Color(102, 0, 102))
    lugar5 = (440, 220)
    objetosDeTexto6 = posiciones.render("F", 0, p.Color(102, 0, 102))
    lugar6 = (440, 270)
    objetosDeTexto7 = posiciones.render("G", 0, p.Color(102, 0, 102))
    lugar7 = (440, 320)
    objetosDeTexto8 = posiciones.render("H", 0, p.Color(102, 0, 102))
    lugar8 = (440, 380)
    objetosDeTexto9 = posiciones.render("1", 0, p.Color(102, 0, 102))
    lugar9 = (15, 430)
    objetosDeTexto10 = posiciones.render("2", 0, p.Color(102, 0, 102))
    lugar10 = (70, 430)
    objetosDeTexto11 = posiciones.render("3", 0, p.Color(102, 0, 102))
    lugar11 = (125, 430)
    objetosDeTexto12 = posiciones.render("4", 0, p.Color(102, 0, 102))
    lugar12 = (175, 430)
    objetosDeTexto13 = posiciones.render("5", 0, p.Color(102, 0, 102))
    lugar13 = (230, 430)
    objetosDeTexto14 = posiciones.render("6", 0, p.Color(102, 0, 102))
    lugar14 = (285, 430)
    objetosDeTexto15 = posiciones.render("7", 0, p.Color(102, 0, 102))
    lugar15 = (340, 430)
    objetosDeTexto16 = posiciones.render("8", 0, p.Color(102, 0, 102))
    lugar16 = (390, 430)


    pantalla.blit(objetosDeTexto, lugar)
    pantalla.blit(objetosDeTexto2, lugar2)
    pantalla.blit(objetosDeTexto3, lugar3)
    pantalla.blit(objetosDeTexto4, lugar4)
    pantalla.blit(objetosDeTexto5, lugar5)
    pantalla.blit(objetosDeTexto6, lugar6)
    pantalla.blit(objetosDeTexto7, lugar7)
    pantalla.blit(objetosDeTexto8, lugar8)
    pantalla.blit(objetosDeTexto9, lugar9)
    pantalla.blit(objetosDeTexto10, lugar10)
    pantalla.blit(objetosDeTexto11, lugar11)
    pantalla.blit(objetosDeTexto12, lugar12)
    pantalla.blit(objetosDeTexto13, lugar13)
    pantalla.blit(objetosDeTexto14, lugar14)
    pantalla.blit(objetosDeTexto15, lugar15)
    pantalla.blit(objetosDeTexto16, lugar16)





def dibujar_piezas(pantalla, tablero):
    for i in range(dimension):
        for j in range(dimension):
            pieza = tablero[j][i]
            if pieza != "--":
                pantalla.blit(piezas[pieza], p.Rect(j*cuadrado, i*cuadrado, cuadrado, cuadrado))





def escribir(pantalla, texto, texto2):
    font = p.font.SysFont("Arial", 22, True, False)
    objetosDeTexto = font.render(texto, 0, p.Color("Purple"))
    lugar = p.Rect(0, 0, 480, 480).move(450/2 - objetosDeTexto.get_width()/2, 450/2 - objetosDeTexto.get_height()/2)
    pantalla.blit(objetosDeTexto, lugar)
    objetosDeTexto = font.render(texto, 0, p.Color("Black"))
    pantalla.blit(objetosDeTexto, lugar.move(2, 2))
    objetosDeTexto = font.render(texto2, 0, p.Color("Purple"))
    lugar = p.Rect(0, 0, 480, 480).move(450 / 2 - objetosDeTexto.get_width() / 2, 540 / 2 - objetosDeTexto.get_height() / 2)
    pantalla.blit(objetosDeTexto, lugar)
    objetosDeTexto = font.render(texto2, 0, p.Color("Black"))
    pantalla.blit(objetosDeTexto, lugar.move(2, 2))

def bienvenida(pantalla):
    objetosDeTexto2 = True
    objetosDeTexto = True
    global juegoIniciado
    if objetosDeTexto2 and objetosDeTexto == True:
        posiciones = p.font.SysFont("Arial", 20, True, False)
        objetosDeTexto = posiciones.render("Bienvenido al Ajedrez", 0, p.Color(0, 0, 0))
        lugar = (100, 10)
        if not juegoIniciado:
            objetosDeTexto2 = posiciones.render("Presiona 'D' para comenzar a jugar", 0, p.Color(0, 0, 0))
            lugar2 = (10, 100)
            pantalla.blit(objetosDeTexto, lugar)
            pantalla.blit(objetosDeTexto2, lugar2)
            p.display.flip()
            p.display.update()
            for i in p.event.get():
                if i.type == p.KEYDOWN:
                    if i.key == p.K_d:
                        juegoIniciado=True


def clear():
    global pantalla
    pantalla.fill((0,0,0))
    p.display.flip()









