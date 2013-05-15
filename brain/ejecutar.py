# -*- coding: utf-8 -*-


import pilas

ALTO = 720
ANCHO = 1280

pilas.iniciar(titulo='Brain', ancho=ANCHO, alto=ALTO, pantalla_completa=True)

import escaparate
pilas.cambiar_escena(escaparate.EscenaEscaparate())

pilas.ejecutar()
