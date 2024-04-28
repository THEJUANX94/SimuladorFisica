import pygame as pg

class BotonAumentar:
    def __init__(self, x, y, radio=12, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.rect = pg.Rect(x - radio, y - radio, radio * 2, radio * 2)
        self.font = pg.font.Font(None, 24)
        self.text_color = (255, 255, 255)
        self.text = self.font.render("+", True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radio)
        screen.blit(self.text, self.text_rect)

    def update(self):
        pass

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
