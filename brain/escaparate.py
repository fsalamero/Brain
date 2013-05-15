# -*- coding:utf-8 -*-

import pilas
import random


ALTO = 720
ANCHO = 1280

fullscreen = True


class Escaparate(object):
    '''Contiene todos los elementos que se han de mostrar'''

    def __init__(self):
        # Elementos del escaparate
        self.listado = []

    def add(self, *k):
        for elemento in k:
            self.listado.append(elemento)

    def mostrar(self):
        '''Recorre el listado de elementos y los muestra equidistantes'''

        margen = 20  # espacio mínimo intermedio
        total = 0
        for elemento in self.listado:
            total += elemento.obtener_ancho()
        cuantos = len(self.listado)
        total += margen * (cuantos - 1)
        posicion = -total / 2
        for elemento in self.listado:
            elemento.mostrar(izquierda=posicion)
            posicion += elemento.obtener_ancho() + margen


class Etiqueta(pilas.actores.Actor):
    '''Define las etiquetas para las relaciones entre elementos'''

    def __init__(self, texto):
        x, y = generar_posicion_offscreen()
        pilas.actores.Actor.__init__(self, x=x, y=y)
        ancho, alto = pilas.mundo.motor.obtener_area_de_texto(texto, 14)
        aspecto = pilas.imagenes.cargar_superficie(ancho=ancho,
                                                    alto=alto)
        aspecto.pintar(pilas.colores.azul)
        aspecto.texto(texto, magnitud=14,
                        color=pilas.colores.blanco)
        self.imagen = aspecto
        self.aprender(pilas.habilidades.Arrastrable)

    def mostrar(self, izquierda=0):
        self.izquierda = [izquierda], 0.3
        self.y = [0], 0.3


class Item(pilas.actores.Actor):
    """Define las unidades de información"""

    def __init__(self, elemento=''):
        x, y = generar_posicion_offscreen()
        pilas.actores.Actor.__init__(self, x=x, y=y)
        self.elemento = elemento
        self.etiquetas = []
        self.texto = ''
        self.aprender(pilas.habilidades.Arrastrable)

    def add_etiqueta(self, etiqueta):
        self.etiquetas.append(etiqueta)

    def add_texto(self, texto):
        self.texto += texto

    def definir_imagen(self, imagen):
        self.imagen = imagen

    def mostrar(self, izquierda=0):
        self.izquierda = [izquierda], 0.3
        self.y = [0], 0.3


class EscenaEscaparate(pilas.escena.Base):
    '''Escena que muestra los objetos por defecto'''

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        self.grupo = Escaparate()
        idea = Item()
        etiqueta1 = Etiqueta(u"1ESA")
        etiqueta2 = Etiqueta(u"Quiero un camión")
        etiqueta3 = Etiqueta(u"Había una vez, un circoooo")
        self.grupo.add(idea, etiqueta1, etiqueta2, etiqueta3)
        self.grupo.mostrar()
        pilas.eventos.pulsa_tecla.conectar(self.gestionar_tecla)

    def gestionar_tecla(self, evento):
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

