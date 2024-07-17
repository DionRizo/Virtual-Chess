import pygame as p
from pygame.locals import *
from instrucciones import *
from juego import *

p.init()

WIDTH = 800
HEIGHT = 600

BLACK = (102, 153, 255)
GREEN = (153, 204, 255)
RED = (255, 51, 51)
YELLOW = (255, 153, 102)
WHITE= (255,255,255)

screen = p.display.set_mode((WIDTH, HEIGHT))
#screen.fill("White")
p.display.set_caption('Ajedrez')

default_font = p.font.Font(None, 80)
big_font = p.font.SysFont(None, 50)

def texto(text, font, surface, x, y, main_color, background_color=WHITE):
    textobj = font.render(text, True, main_color, background_color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobj, textrect)

def menu():


    texto('AJEDREZ', default_font, screen,
          WIDTH / 2, HEIGHT / 3, YELLOW, WHITE)
    texto("INSTRUCCIONES [presiona  'I' ]", big_font, screen,
          WIDTH / 2, HEIGHT / 2, YELLOW, WHITE)
    texto("JUGAR [presiona 'J' ]",
          big_font, screen, WIDTH / 2, HEIGHT / 1.5, YELLOW, WHITE)
    p.display.update()

def pantalla():
    menu()
    while True:
        for i in p.event.get():
            if i.type == p.KEYDOWN:
                if i.key == p.K_i:
                    xInst = Instrucciones()
                    xInst.pantalla()
                    p.display.flip()
                    p.display.update()
                    menu()
            if i.type == QUIT:
                return
        for i in p.event.get():
            if i.type == p.KEYDOWN:
                if i.key == p.K_j:
                    graficas()
                    p.display.flip()
                    p.display.update()
                    menu()




def main_loop():
    running = True
    while running:
        for event in p.event.get():
            if event.type == QUIT:
                running = False




pantalla()
p.quit()