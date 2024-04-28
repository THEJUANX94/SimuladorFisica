import pygame as pg

class Probeta:
    def __init__(self, x, y, width, height, border_color=(0, 0, 0), border_width=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_color = border_color
        self.border_width = border_width
        self.fill_color = (255, 255, 255)
        self.liquid_color = (255, 255, 255)
        self.liquid_level = 0.8
        self.border_radius = 10
        self.nombre_liquido = None


        self.nombre_liquido_font = pg.font.Font(None, 24)
        self.nombre_liquido_text_color = (0, 0, 0)
        self.nombre_liquido_bg_color = (255, 255, 255)
        self.nombre_liquido_border_color = (0, 0, 0)
        self.nombre_liquido_border_radius = 10
        self.nombre_liquido_border_width = 2

    def draw(self, screen):
        # Dibujar la probeta con esquinas redondeadas
        probeta_rect = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, self.fill_color, probeta_rect, border_radius=self.border_radius)

        # Dibujar el líquido encima del fondo blanco
        liquid_height = int(self.height * self.liquid_level)
        liquid_rect = pg.Rect(self.x, self.y + self.height - liquid_height, self.width, liquid_height)
        pg.draw.rect(screen, self.liquid_color, liquid_rect, border_radius=self.border_radius)

        # Dibujar los bordes de la probeta con esquinas redondeadas
        pg.draw.rect(screen, self.border_color, probeta_rect, self.border_width, border_radius=self.border_radius)

        # Mostrar el nombre del líquido seleccionado en un recuadro
        if self.nombre_liquido:

            nombre_liquido_text = self.nombre_liquido_font.render(f"Líquido: {self.nombre_liquido}", True, self.nombre_liquido_text_color)


            text_rect = nombre_liquido_text.get_rect()
            text_rect.topleft = (self.x + 10, self.y - 30)


            bg_width = text_rect.width + 20
            bg_height = text_rect.height + 10


            bg_rect = pg.Rect(text_rect.left - 10, text_rect.top - 5, bg_width, bg_height)


            pg.draw.rect(screen, self.nombre_liquido_bg_color, bg_rect, border_radius=self.nombre_liquido_border_radius)


            pg.draw.rect(screen, self.nombre_liquido_border_color, bg_rect, self.nombre_liquido_border_width, border_radius=self.nombre_liquido_border_radius)


            screen.blit(nombre_liquido_text, text_rect)

    def update_liquido(self, nombre_liquido):
        self.nombre_liquido = nombre_liquido
