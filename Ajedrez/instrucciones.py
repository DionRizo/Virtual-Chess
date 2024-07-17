from pygame.locals import *
import pygame

class Instrucciones:
    WIDTH = 800
    HEIGHT = 600
    BLACK = (0, 0, 0)
    GREEN = (153, 204, 255)
    RED = (255, 51, 51)
    ORANGE = (255, 153, 102)
    WHITE = (255, 255, 255)
    default_font=None
    screen =None
    def __init__(self):
        pygame.init()
        # Display
        self.default_font = pygame.font.Font(None, 24)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.WHITE)
        # Window titlebar
        pygame.display.set_caption('Instrucciones')


    def clear(self):
        self.screen.fill((0,0,0))
        pygame.display.flip()

    def texto(self, text, font, surface, x, y, main_color, background_color):
        textobj = font.render(text, True, main_color, background_color)
        textrect = textobj.get_rect()
        textrect.centerx = x
        textrect.centery = y
        surface.blit(textobj, textrect)


    def pantalla(self):
        while True:
            title_font = pygame.font.Font('freesansbold.ttf', 65)
            big_font = pygame.font.Font(None, 36)
            self.texto('* HAY 6 TIPOS DE PIEZAS, CADA UNO TIENE SU FORMA DE MOVERSE:', self.default_font, self.screen,
            self.WIDTH / 2, self.HEIGHT / 7.9, self.BLACK , self.WHITE)
            self.texto('1. REY: es la pieza más importante, sólo puede avanzar una casilla en cualquier dirección', self.default_font, self.screen,
            self.WIDTH / 2.1, self.HEIGHT / 4.95, self.ORANGE , self.WHITE)
            self.texto('2. REINA: puede moverse en cualquier dirección y tantas casillas como desee', self.default_font, self.screen,
            self.WIDTH / 2.39, self.HEIGHT / 3.68, self.ORANGE , self.WHITE)
            self.texto('3. TORRE: Puede moverse de forma horizontal y vertical, todas las casillas que desee.', self.default_font, self.screen,
            self.WIDTH / 2.20, self.HEIGHT / 2.9, self.ORANGE , self.WHITE)
            self.texto('4. ALFIL: Se mueve únicamente de forma diagonal, todas las casillas que desee.', self.default_font, self.screen,
            self.WIDTH / 2.36, self.HEIGHT / 2.45, self.ORANGE , self.WHITE)
            self.texto("5. CABALLO: Se mueve dos casillas arriba/abajo (+) otra hacia los lados, dibujando una 'L'", self.default_font, self.screen,
            self.WIDTH / 2.12,self.HEIGHT / 2.10, self.ORANGE , self.WHITE)
            self.texto('6. PEÓN: Se mueve solo hacia adelante, captura en diagonal. Al iniciar avanza dos, luego una. ', self.default_font, self.screen,
            self.WIDTH / 2.01, self.HEIGHT / 1.85, self.ORANGE , self.WHITE)
            self.texto('** NINGUNA PIEZA PUEDE PASAR POR ENCIMA DE OTRA DE SU MISMO COLOR **', self.default_font, self.screen,
            self.WIDTH / 2, self.HEIGHT / 1.40, self.RED , self.WHITE)
            self.texto('PARA DESHACER LA JUGADA PREVIA PRESIONA [S]', self.default_font, self.screen,
            self.WIDTH / 2, self.HEIGHT / 1.65, self.RED , self.WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.clear()
                    return