import pygame as pg

class Button:
    def __init__(self, x=0, y=0, text="", width=200, height=50, elev=6, font_size=24):
        self.font = pg.font.Font(None, font_size)
        self.text = self.font.render(text, True, (26,35,46))
        self.text_rect = self.text.get_rect()
        self.bottom_rect = pg.Rect((x + elev, y + elev), (width, height))
        self.top_rect = pg.Rect((x, y), (width, height))
        self.text_rect.center = self.top_rect.center

        self.hover = False
        self.pressed = False
        self.clicked = False
        self.elev = elev
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self):
        self.clicked = False
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.hover = True
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed is True:
                    self.pressed = False
                    self.clicked = True
        else:
            self.pressed = False
            self.hover = False

    def draw(self, display):
        top_rect_color = "#317bcf" if self.hover else (255,255,255)
        bottom_rect_color = "#1a232e"
        shadow_color = (0, 0, 0, 50)

        pg.draw.rect(display, shadow_color, self.bottom_rect, border_radius=12)
        pg.draw.rect(display, bottom_rect_color, self.bottom_rect, border_radius=12)
        pg.draw.rect(display, top_rect_color, self.top_rect, border_radius=12)
        display.blit(self.text, self.text_rect)

def create_gradients(width, height, start_color, end_color):
    gradient_surface = pg.Surface((width, height))
    for y in range(height):
        color = [
            start_color[i] + (end_color[i] - start_color[i]) * y // height
            for i in range(3)
        ]
        pg.draw.line(gradient_surface, color, (0, y), (width, y))
    return gradient_surface
