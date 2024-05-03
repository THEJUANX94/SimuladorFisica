import pygame as pg

class TemperaturaMarcador:
    def __init__(self, x, y, font_size=24):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font = pg.font.Font(None, font_size)
        self.text_color = (255, 255, 255)
        self.background_color = (64, 64, 64)
        self.border_color = (255, 0, 0)
        self.border_radius = 10
        self.border_width = 2
        self.temperatura = None

    def update_temperatura(self, temperatura):
        self.temperatura = temperatura

    def draw(self, screen):
        if self.temperatura is not None:

            temperaturaC_text = self.font.render(f"Temp. °C: {self.temperatura}°", True, self.text_color)
            temperaturaF_text = self.font.render(f"Temp. °F: {round(self.temperatura * (9/5) + 32)}°", True, self.text_color)
            temperaturaK_text = self.font.render(f"Temp. K: {self.temperatura + 273.15}°", True, self.text_color)


            text_rectC = temperaturaC_text.get_rect()
            text_rectC.center = (self.x, self.y)
            bg_width = text_rectC.width + 40
            bg_height = text_rectC.height + 10
            bg_rectC = pg.Rect(text_rectC.left - 10, text_rectC.top - 5, bg_width, bg_height)
            pg.draw.rect(screen, self.background_color, bg_rectC, border_radius=self.border_radius)
            pg.draw.rect(screen, self.border_color, bg_rectC, self.border_width, border_radius=self.border_radius)
            
            text_rectF = temperaturaC_text.get_rect()
            text_rectF.center = (self.x, self.y + 40)
            bg_width = text_rectF.width + 40
            bg_height = text_rectF.height + 10
            bg_rectF = pg.Rect(text_rectF.left - 10, text_rectF.top - 5, bg_width, bg_height)
            pg.draw.rect(screen, self.background_color, bg_rectF, border_radius=self.border_radius)
            pg.draw.rect(screen, self.border_color, bg_rectF, self.border_width, border_radius=self.border_radius)
            
            text_rectK = temperaturaC_text.get_rect()
            text_rectK.center = (self.x, self.y + 80)
            bg_width = text_rectK.width + 40
            bg_height = text_rectK.height + 10
            bg_rectK = pg.Rect(text_rectK.left - 10, text_rectK.top - 5, bg_width, bg_height)
            pg.draw.rect(screen, self.background_color, bg_rectK, border_radius=self.border_radius)
            pg.draw.rect(screen, self.border_color, bg_rectK, self.border_width, border_radius=self.border_radius)


            screen.blit(temperaturaC_text, text_rectC)
            screen.blit(temperaturaF_text, text_rectF)
            screen.blit(temperaturaK_text, text_rectK)
