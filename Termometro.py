import pygame as pg
import time
import os
from tkinter import ttk
import tkinter as tk
from Boton import Button
from LogicaTermometro import *
from Probeta import Probeta
from Temperatura_Marcador import TemperaturaMarcador
from Boton_Aumentar import BotonAumentar
from Teoria import Teoria

pg.init()
screen = pg.display.set_mode((1250, 600))
pg.display.set_caption('Termómetro Simulador')

termometro_img = pg.image.load('temometro.png')

ice_texture = pg.image.load("ice.jpg")
imagen_redimensionada = pg.transform.scale(ice_texture, (50, 160))
imagen_redimensionada.set_alpha(0)

termometro_rect = termometro_img.get_rect(center=(400, 600))
termometro_img = pg.transform.scale(termometro_img, (250, 250))

estufa_img = pg.image.load('ESTUFA.png')
estufa_rect = estufa_img.get_rect(center=(900, 650))
estufa_img = pg.transform.scale(estufa_img, (250, 250))

button_liquids = Button(900, 100, "Escoge el liquido")
button_info = Button(900, 40, "Mas informacion")
boton_aumentar = BotonAumentar(806, 555)
boton_disminuir = BotonAumentar(720, 555, is_plus=False)

probeta = Probeta(750, 290, 50, 200)
temperatura_marcador = TemperaturaMarcador(310, 290)

probeta.liquid_level = 0.8
temperatura_estandar = get_temperatura_estandar('Agua')
temperatura_marcador.update_temperatura(temperatura_estandar)
probeta.update_liquido('Agua')
probeta.liquid_color = (135, 206, 235)
nueva_temperatura = 20
nombre_liquido = 'Agua'

teoria = Teoria(400, 100)
ultimo_tiempo_ejecucion = time.time()
tiempo_vaciado = None
DURACION_VACIADO = 5
running = True
clock = pg.time.Clock()


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if boton_aumentar.is_clicked(pg.mouse.get_pos()):
                # Aumentar la temperatura en la cantidad deseada
                nueva_temperatura = temperatura_marcador.temperatura + 1  # Aumentar en 1
                temperatura_marcador.update_temperatura(nueva_temperatura)
                imagen_redimensionada.set_alpha(0)
                # Verificar si la temperatura alcanzó el límite máximo

                if nueva_temperatura >= get_temperatura_max(probeta.nombre_liquido):

                    probeta.liquid_level = 0.4
                    temperatura_marcador.update_temperatura(nueva_temperatura)

                    # Activar el temporizador para el vaciado de la probeta
                    tiempo_vaciado = time.time() + DURACION_VACIADO

            elif boton_disminuir.is_clicked(pg.mouse.get_pos()):

                    # Verificar si la temperatura alcanzó el límite minimo
                    if nueva_temperatura <= get_temperatura_min(probeta.nombre_liquido):
                        nueva_temperatura = temperatura_marcador.temperatura + 1
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        nueva_temperatura = temperatura_marcador.temperatura - 1
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        imagen_redimensionada.set_alpha(100)
                        
                    else:
                        nueva_temperatura = temperatura_marcador.temperatura - 1  # Disminuye en 1
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        imagen_redimensionada.set_alpha(0)
            else: pass

    # Verificar si se debe vaciar la probeta
    if tiempo_vaciado and time.time() >= tiempo_vaciado:
        # Vaciar la probeta después de 5 segundos
        probeta.liquid_level = 0
        tiempo_vaciado = None  # Reiniciar el temporizador
    if time.time() - ultimo_tiempo_ejecucion > 5:
        teoria.update_text()
        ultimo_tiempo_ejecucion = time.time()
                        
    screen.fill((12,34,63))

    screen.blit(termometro_img, termometro_rect)
    screen.blit(estufa_img, estufa_rect)
    
    button_liquids.draw(screen)
    button_info.draw(screen)
    button_liquids.update()
    button_info.update()
    
    

    if button_liquids.clicked:
        tiempo_vaciado = None
        main_window = tk.Tk()
        main_window.config(width=300, height=200)
        main_window.title("SELECCION DE LIQUIDO")

        combo = ttk.Combobox(main_window, state="readonly", values=getliquidList(),width=30)
        combo.place(x=60, y=60)


        def on_select():

            nombre_liquido = combo.get().strip()
            if probeta.liquid_level == 0:
                probeta.liquid_level = 0.8
            temperatura_estandar = get_temperatura_estandar(nombre_liquido)
            temperatura_marcador.update_temperatura(temperatura_estandar)
            probeta.update_liquido(nombre_liquido)
            if probeta.liquid_level == 0.4:
                probeta.liquid_level = 0.8
            # Cambiar el color de la probeta según el líquido seleccionado
            if nombre_liquido == 'Agua':
                probeta.liquid_color = (135, 206, 235)  # Azul
            elif nombre_liquido == 'Alcohol etílico':
                probeta.liquid_color = (0, 255, 255)  # Azul celeste
            elif nombre_liquido == 'Acetona':
                probeta.liquid_color = (132, 112, 255)  # Azul púrpura
            elif nombre_liquido == 'Etanol':
                probeta.liquid_color = (173, 216, 230)  # Azul claro
            elif nombre_liquido == 'Metanol':
                probeta.liquid_color = (135, 206, 235)  # Azul celeste (similar al alcohol etílico)
            elif nombre_liquido == 'Aceite de oliva':
                probeta.liquid_color = (255, 255, 0)  # Amarillo
            elif nombre_liquido == 'Mercurio':
                probeta.liquid_color= (169, 169, 169)  # Gris oscuro
            main_window.destroy()
        confirm_button = ttk.Button(main_window, text="Aceptar", command=on_select)
        confirm_button.place(x=100, y=100)
        main_window.mainloop()

    if button_info.clicked:
        window = tk.Tk()
        window.title("Presentation")

        def abrir_diapositivas():
            archivo_ppt = 'Celsius & Fahrenheit_ Temperature Lesson by Slidesgo.pptx'
            try:
                # Attempt to open the file using system default application
                os.startfile(archivo_ppt)
                window.destroy()
            except FileNotFoundError:
                print("Presentation file not found.")
                window.destroy()


        def abrir_documento_pdf():
            archivo_pdf = 'AYUDA.pdf'
            try:
                # Attempt to open the PDF file using system default application
                os.startfile(archivo_pdf)
                window.destroy()
            except FileNotFoundError:
                print("PDF file not found.")
                window.destroy()

        boton_abrir = tk.Button(window, text="Abrir diapositivas", command=abrir_diapositivas)
        boton_abrir.pack()

        boton_abrir_pdf = tk.Button(window, text="Abrir documento PDF", command=abrir_documento_pdf)
        boton_abrir_pdf.pack()
        window.mainloop()
    
    
    probeta.draw(screen)
    screen.blit(imagen_redimensionada, (750, 330))
    temperatura_marcador.draw(screen)
    boton_aumentar.draw(screen)
    boton_disminuir.draw(screen)
    teoria.draw(screen)
    pg.display.flip()
    clock.tick(30)

pg.quit()
