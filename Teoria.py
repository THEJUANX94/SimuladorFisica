import pygame as pg

lista_teoria = ['El termometro es uno de los intrumentos de medicion de temperatura mas conocidos', 'La formula de cambio de temperatura de celsius a Fahrenheit es (°C x 9/5) + 32 = °F ', 'La formula de cambio de temperatura de celsius a Kelvin es °C + 273.15 =  K']

class Teoria:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pg.Rect(x, y, 10, 10)
        self.font = pg.font.Font(None, 24)
        self.text_color = (255, 255, 255)
        self.text = self.font.render(lista_teoria[0], True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.a = 1

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def update_text(self):
        if(self.a <= len(lista_teoria)-1):
            self.text = self.font.render(lista_teoria[self.a], True, self.text_color)
            self.a += 1
        else:
            self.a = 0
            self.text = self.font.render(lista_teoria[self.a], True, self.text_color)