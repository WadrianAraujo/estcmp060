import turtle
import math


def fiboplot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    x.pencolor("blue")  # Escolhendo a cor do desenho da plotagem

    # Algoritmo para o primeiro quadrado
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Processamento do Fibonacci
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Geração dos proximo quadrados
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # Processamento do Fibonacci
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Retornando a caneta para a posição inicial da espiral
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    x.pencolor("red")  # Mudando a cor da caneta

    # Grafico espiral de Fibonacci
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b

# factor representa o multiplicador
# que baseia a expansão ou encolhimento do grafico


factor = 10

# Recebendo quantos vezes o algoritmo executara interaçoes
n = int(input("Insira o numero de interaçoes (apenas numeros > 1):"))

# Desenhando a experial de Fibonacci
# e imprimindo o numero do Fibonacci correspondente
if n > 1:
    print("Serie Fibonacci para", n, "elementes :")
    x = turtle.Turtle()
    x.speed(100)
    fiboplot(n)
    turtle.done()
else:
    print("O numero de interaçoes precisa ser > 0")
