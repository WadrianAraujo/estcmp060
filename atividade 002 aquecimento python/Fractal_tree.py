from turtle import *

# Velocidade do turtle
speed('fastest')

# Gira a direçao do cursor
rt(-90)

# O angulo entre a base e o ramo da arvore 'Y'
angle = 30


# função para imprimir o 'Y'
def y(sz, level):

    if level > 1:
        # Escolha da cor
        colormode(255)
        # Define a cor depedendo do nivel atual
        pencolor(0, 255//level, 0)
        # Desenhando a base
        fd(sz)
        rt(angle)
        # Recursividade para as subarvores a direita
        y(0.8 * sz, level-1)
        pencolor(0, 255//level, 0)
        lt(2 * angle)
        # Recursividade para as subarvores a esqueda
        y(0.8 * sz, level-1)
        pencolor(0, 255//level, 0)
        rt(angle)
        fd(-sz)


# Tamanho ,nivel
y(80, 7)
