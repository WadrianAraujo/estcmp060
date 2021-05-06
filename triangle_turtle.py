import turtle

# Metodo para obter a janela
wn = turtle.Screen()
# Criando objeto tess
tess = turtle.Turtle()


def triangle(x,y):

    # Caneta
    tess.penup()
    # Usado para mover o cursor para
    # as posiçoes x e y
    tess.goto(x, y)
    # utilizado para desenhar
    tess.pendown()

    for i in range(3):
        # Move o cursor em 100 unidades
        tess.forward(100)
        # gira o cursor em 120 graus para a esquerda
        tess.left(120)
        # Move o cursor em 100 unidades
        tess.forward(100)


# Função para enviar a posição do cursor para triangle
turtle.onscreenclick(triangle, 1)
turtle.listen()

# Mantem a tela ligada
turtle.done()