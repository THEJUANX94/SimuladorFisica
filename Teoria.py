import pygame as pg

lista_teoria = ['El termometro es uno de los instrumentos de medicion de temperatura mas conocidos', 'La formula de cambio de temperatura de celsius a Fahrenheit es (°C x 9/5) + 32 = °F ',
                'La formula de cambio de temperatura de celsius a Kelvin es °C + 273.15 =  K','El punto de ebullicion del agua es de 100°C','El punto de ebullicion del alcohol etilico  es de 78.3°C',
                'El punto de ebullicion de la acetona es de 56.2°C','El punto de ebullicion del etanol es de 78.5°C','El punto de ebullicion del metanol  es de 64.6°C','El punto de ebullicion del aceite de oliva es de 360°C',
                'El punto de ebullicion del mercurio es de 356.9°C','El punto de congelacion del agua es de 0°C','El punto de congelacion del alcohol etilico es de -114.10°C','El punto de congelacion de la acetona es de -89.3°C',
                'El punto de congelacion del Etanol es de -114.10°C','El punto de congelacion del metanol es de -97.8°C','El punto de congelacion del aceite de oliva es de -10°C','El punto de congelacion del mercurio es de -38.9°C']

class Teoria:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pg.Rect(x, y, 10, 10)
        self.font = pg.font.Font(None, 24)
        self.title_font = pg.font.Font(None, 36)  # Fuente para el título
        self.title_text = self.title_font.render("TEMPERATURA DE LIQUIDOS", True, (255, 255, 255))
        self.text_color = (255, 255, 255)
        self.texts = [self.font.render(line, True, self.text_color) for line in lista_teoria]
        self.current_index = 0
        self.fade_timer = 0
        self.line_spacing = 30
        self.text_y = 120

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)


        screen.blit(self.title_text, (20, 20))


        if self.current_index < len(self.texts):
            screen.blit(self.texts[self.current_index], (20, self.text_y))
        if self.current_index + 1 < len(self.texts):
            screen.blit(self.texts[self.current_index + 1], (20, self.text_y + self.line_spacing))

    def update_text(self):

        self.current_index += 2
        if self.current_index >= len(self.texts):
            self.current_index = 0





