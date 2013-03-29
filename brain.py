#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pilas
import random

ALTO = 600
ANCHO = 800

fullscreen = True

pilas.iniciar(ancho=ANCHO, alto=ALTO, pantalla_completa=True)


class Etiqueta(pilas.actores.Actor):

    def __init__(self, texto):
        x, y = generar_posicion_offscreen()
        pilas.actores.Actor.__init__(self, x=x, y=y)
        ancho, alto = pilas.mundo.motor.obtener_area_de_texto(texto, 14)
        aspecto = pilas.imagenes.cargar_superficie(ancho=ancho + 15,
                                                    alto=alto + 5)
        aspecto.pintar(pilas.colores.azul)
        aspecto.texto(texto, x=5, y=15, magnitud=14,
                        color=pilas.colores.blanco)
        self.imagen = aspecto
        self.aprender(pilas.habilidades.Arrastrable)
        self.x = [0], 0.5
        self.y = [0], 0.5


class Item(object):
    """Define las unidades de información"""

    def __init__(self, x=0, y=0, elemento=''):
        self.aspecto = pilas.actores.Actor(x=x, y=y)
        self.elemento = elemento
        self.etiquetas = []
        self.texto = ''

    def add_etiqueta(self, etiqueta):
        self.etiquetas.append(etiqueta)

    def add_texto(self, texto):
        self.texto += texto

    def definir_imagen(self, imagen):
        self.imagen = imagen


def gestionar_tecla(evento):
    global fullscreen
    if evento.codigo == pilas.simbolos.q:
        pilas.terminar()
    elif evento.codigo == pilas.simbolos.f:
        if fullscreen:
            pilas.atajos.modo_ventana()
            fullscreen = False
        else:
            pilas.atajos.modo_pantalla_completa()
            fullscreen = True


def generar_posicion_offscreen():
    '''Genera un punto al azar fuera de la ventana'''
    x = random.randint(-ANCHO, ANCHO)
    if abs(x) <= ANCHO / 2:
        y = random.choice([ALTO, -ALTO])
    else:
        y = random.randint(-ALTO, ALTO)
    return x, y

pilas.eventos.pulsa_tecla.conectar(gestionar_tecla)

idea = Item()
etiqueta = Etiqueta(u"1ESA")

pilas.ejecutar()
