#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pilas

ALTO = 600
ANCHO = 800

fullscreen = True

pilas.iniciar(ancho=ANCHO, alto=ALTO, pantalla_completa=True)


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


def salir(evento):
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

pilas.eventos.pulsa_tecla.conectar(salir)

idea = Item()

pilas.ejecutar()
