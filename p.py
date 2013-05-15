import pilas

pilas.iniciar()


def testear_click(evento):
    if (evento.boton == 1):
        if m.colisiona_con_un_punto(evento.x, evento.y):
            m.x = [300], 0.1
            m.y = [200], 0.1
            m.escala = [1], 0.1


def testear_over(evento):
    if m.colisiona_con_un_punto(evento.x, evento.y):
        m.escala = [2], 0.1
    else:
        m.escala = [1], 0.1


m = pilas.actores.Mono()

pilas.escena_actual().click_de_mouse.conectar(testear_click)
pilas.escena_actual().mueve_mouse.conectar(testear_over)

pilas.ejecutar()