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

            temperatura_text = self.font.render(f"Temp. Actual: {self.temperatura}°", True, self.text_color)


            text_rect = temperatura_text.get_rect()
            text_rect.center = (self.x, self.y)


            bg_width = text_rect.width + 20
            bg_height = text_rect.height + 10


            bg_rect = pg.Rect(text_rect.left - 10, text_rect.top - 5, bg_width, bg_height)


            pg.draw.rect(screen, self.background_color, bg_rect, border_radius=self.border_radius)


            pg.draw.rect(screen, self.border_color, bg_rect, self.border_width, border_radius=self.border_radius)


            screen.blit(temperatura_text, text_rect)
