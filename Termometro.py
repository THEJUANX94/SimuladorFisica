import pygame as pg
import time
import os
from tkinter import ttk, messagebox
import tkinter as tk
from Boton import Button
from LogicaTermometro import *
from Probeta import Probeta
from Temperatura_Marcador import TemperaturaMarcador
from Boton_Aumentar import BotonAumentar
from Teoria import Teoria

entrar_presionado = False

def mostrar_bienvenida():
    def on_enter():
        global entrar_presionado
        entrar_presionado = True
        ventana_bienvenida.destroy()

    def abrir_diapositivas():
        archivo_pdf = 'PresentacionTemperatura.pdf'
        try:
            os.startfile(archivo_pdf)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo PDF no se encontró.")

    def abrir_tutorial():
        archivo_pdf = 'AYUDA.pdf'
        try:
            os.startfile(archivo_pdf)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo PDF de ayuda no se encontró.")

    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.title("TEMPERATURA DE LIQUIDOS")
    ventana_bienvenida.geometry("450x350")
    ventana_bienvenida.configure(bg='white')

    label_bienvenido = tk.Label(ventana_bienvenida,
                                text="¡BIENVENIDO!",
                                bg='white', fg='darkblue', font=("Arial", 16, "bold"))
    label_bienvenido.pack(pady=10)

    label_texto = tk.Label(ventana_bienvenida,
                           text="Nuestra aplicación te permitirá interactuar con diferentes líquidos \n"
                                "y así saber qué pasa cuando cambia su temperatura.\n"
                                "¿Estás listo?",
                           bg='white', font=("Arial", 12))
    label_texto.pack(pady=10)


    boton_entrar = tk.Button(ventana_bienvenida, text="ENTRAR", command=on_enter, bg='darkblue', fg='white',
                             font=("Arial", 12), relief='sunken', borderwidth=1)
    boton_entrar.pack(pady=10)

    boton_teoria = tk.Button(ventana_bienvenida, text="TEORÍA", command=abrir_diapositivas, bg='darkblue', fg='white',
                             font=("Arial", 12), relief='sunken', borderwidth=1)
    boton_teoria.pack(pady=10)
    boton_tutorial = tk.Button(ventana_bienvenida, text="TUTORIAL DE LA APP", command=abrir_tutorial, bg='darkblue', fg='white',
                               font=("Arial", 12), relief='sunken', borderwidth=1)
    boton_tutorial.pack(pady=10)

    label_texto_ult = tk.Label(ventana_bienvenida,
                           text="Desarrollado por: Juan Sebastian Martinez Noreña, Brayan Alejandro Cifuentes Quiroga\nKatlyn Galvis Rodríguez,Mileth Yonady Martinez Rojas,Laura Sofia Moreno Alonso\n",
                           bg='white', font=("arial", 8))
    label_texto_ult.pack(pady=10)

    ventana_bienvenida.mainloop()


mostrar_bienvenida()


if entrar_presionado:
    pg.init()
    screen = pg.display.set_mode((1150, 600))
    background_image = pg.image.load('fondo.jpg')
    background_image = pg.transform.scale(background_image, (1150, 600))
    pg.display.set_caption('Termómetro Simulador')
    termometro_img = pg.image.load('temometro.png')

    ice_texture = pg.image.load("ice.jpg")
    imagen_redimensionada = pg.transform.scale(ice_texture, (50, 160))
    imagen_redimensionada.set_alpha(0)

    smoke_texture = pg.image.load("smoke.png")
    imagen_redimensionada2 = pg.transform.scale(smoke_texture, (50, 160))
    imagen_redimensionada2.set_alpha(0)

    termometro_rect = termometro_img.get_rect(center=(400, 600))
    termometro_img = pg.transform.scale(termometro_img, (250, 250))

    estufa_img = pg.image.load('ESTUFA.png')
    estufa_rect = estufa_img.get_rect(center=(900, 650))
    estufa_img = pg.transform.scale(estufa_img, (250, 250))

    button_liquids = Button(900, 100, "ESCOGE EL LIQUIDO")
    button_info = Button(900, 40, "VOLVER AL MENU")
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

    teoria = Teoria(20, 70)
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

                    nueva_temperatura = temperatura_marcador.temperatura + 20
                    temperatura_marcador.update_temperatura(nueva_temperatura)
                    imagen_redimensionada.set_alpha(0)

                    if nueva_temperatura >= get_temperatura_max(probeta.nombre_liquido):
                        probeta.liquid_level = 0.4
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        imagen_redimensionada2.set_alpha(100)
                        # Activar el temporizador para el vaciado de la probeta
                        tiempo_vaciado = time.time() + DURACION_VACIADO

                elif boton_disminuir.is_clicked(pg.mouse.get_pos()):

                    if nueva_temperatura <= get_temperatura_min(probeta.nombre_liquido):
                        nueva_temperatura = temperatura_marcador.temperatura + 1
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        nueva_temperatura = temperatura_marcador.temperatura - 1
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        imagen_redimensionada.set_alpha(100)
                        imagen_redimensionada2.set_alpha(0)
                    else:
                        nueva_temperatura = temperatura_marcador.temperatura - 1  # Disminuir en 1
                        temperatura_marcador.update_temperatura(nueva_temperatura)
                        imagen_redimensionada.set_alpha(0)
                else:
                    pass


        if tiempo_vaciado and time.time() >= tiempo_vaciado:

            imagen_redimensionada2.set_alpha(0)
            probeta.liquid_level = 0
            tiempo_vaciado = None

        if time.time() - ultimo_tiempo_ejecucion > 5:
            teoria.update_text()
            ultimo_tiempo_ejecucion = time.time()

        screen.blit(background_image, (0, 0))
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

            combo = ttk.Combobox(main_window, state="readonly", values=getliquidList(), width=30)
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
                elif nombre_liquido =='Aceite de oliva':
                    probeta.liquid_color=(255,255,0)
                elif nombre_liquido == 'Etanol':
                    probeta.liquid_color = (173, 216, 230)  # Azul claro
                elif nombre_liquido == 'Metanol':
                    probeta.liquid_color = (135, 206, 235)  # Azul
                elif nombre_liquido=='Mercurio':
                    probeta.liquid_color=(128,128,128)

            btn = tk.Button(main_window, text="Seleccionar", command=lambda: [on_select(), main_window.destroy()])
            btn.place(x=120, y=100)

            main_window.mainloop()
        if button_info.clicked:
            mostrar_bienvenida()

        probeta.draw(screen)
        temperatura_marcador.draw(screen)
        screen.blit(imagen_redimensionada, (750, 330))
        screen.blit(imagen_redimensionada2, (750, 330))
        teoria.draw(screen)
        boton_aumentar.draw(screen)
        boton_disminuir.draw(screen)
        pg.display.flip()
        clock.tick(30)

    pg.quit()
