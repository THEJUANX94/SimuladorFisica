import pygame as pg
from tkinter import ttk
import tkinter as tk
from Boton import Button
from LogicaTermometro import getliquidList


pg.init()


screen = pg.display.set_mode((1250, 720))
pg.display.set_caption('Termómetro Simulador')


termometro_img = pg.image.load('temometro.png')
termometro_rect = termometro_img.get_rect(center=(200, 400))


button_liquids = Button(900, 100, "Escoge el liquido")

running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill((255, 255, 255))


    screen.blit(termometro_img, termometro_rect)


    button_liquids.draw(screen)
    button_liquids.update()

    if (button_liquids.clicked):
        main_window = tk.Tk()
        main_window.config(width=300, height=200)
        main_window.title("SELECCION DE LIQUIDO")
        combo = ttk.Combobox(
            state="readonly",
            values=getliquidList())
        combo.place(x=50, y=50)
        main_window.mainloop()

    pg.display.flip()
    clock.tick(30)

pg.quit()
