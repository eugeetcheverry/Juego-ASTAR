import turtle
from PIL import Image, ImageFilter
import numpy as np

#Carga y redimensiona la imagen sin difuminar
imagen_original = Image.open("Logo.jpg")  # Reemplaza "Logo.jpg" con el nombre de tu archivo de imagen
imagen_redimensionada = imagen_original.resize((800, 600))  # Ajusta al tamaño de la ventana
imagen_redimensionada.save("fondo_sin_difuminar.gif")  # Guarda la imagen como .gif

#ventana de Turtle
wn = turtle.Screen()
wn.title('Ping Pong by ASTAR')
wn.setup(width=800, height=600)
wn.bgpic("fondo_sin_difuminar.gif")  # Establece la imagen de fondo directamente
wn.tracer(0)  # Mejora la actualización gráfica

# marcador
marcadorA = 0
marcadorB = 0
A_up = False
A_down = False
B_up = False
B_down = False


# jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

# jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

# pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("red")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0
pelota.dy = 0

# linea divisora
division = turtle.Turtle()
division.color("white")
division.penup()
division.goto(0, 300)
division.setheading(270)
division.pendown()
division.forward(600)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("JugadorA: 0     JugadorB: 0", align="center", font=("Courier", 24, "normal"))

# movimiento funciones
def jugadorA_up():
    global A_up, A_down
    A_up = True
    A_down = False

def jugadorA_down():
    global A_up, A_down
    A_up = False
    A_down = True

def jugadorB_up():
    global B_up, B_down
    B_up = True
    B_down = False

def jugadorB_down():
    global B_up, B_down
    B_up = False
    B_down = True

def start_set():
    pelota.dx = np.random.choice([-1,1])
    pelota.dy = np.random.choice([-1,1])

# teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")
wn.onkeypress(start_set, "space")

# main game loop
while True:
    wn.update()

    #Movimiento jugador A
    if A_up == True:
        y = jugadorA.ycor()
        if y < 250:
            jugadorA.sety(y + 1)
    if A_down == True:
        y = jugadorA.ycor()
        if y > -250:
            jugadorA.sety(y - 1)

    #Movimiento jugador B
    if B_up == True:
        y = jugadorB.ycor()
        if y < 250:
            jugadorB.sety(y + 1)
    if B_down == True:
        y = jugadorB.ycor()
        if y > -250:
            jugadorB.sety(y - 1)
    
    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx = 0
        pelota.dy = 0
        marcadorA += 1
        pen.clear()
        pen.write("JugadorA: {}     JugadorB: {}".format(marcadorA, marcadorB), align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx = 0
        pelota.dy = 0 
        marcadorB += 1
        pen.clear()
        pen.write("JugadorA: {}     JugadorB: {}".format(marcadorA, marcadorB), align="center", font=("Courier", 24, "normal"))

    # Colisiones con jugadores
    if (340 < pelota.xcor() < 350) and (jugadorB.ycor() - 50 < pelota.ycor() < jugadorB.ycor() + 50):
        pelota.dx *= -1
        pelota.dx *= 1.1  # Incrementa la velocidad en un 10%

    if (-350 < pelota.xcor() < -340) and (jugadorA.ycor() - 50 < pelota.ycor() < jugadorA.ycor() + 50):
        pelota.dx *= -1
        pelota.dx *= 1.1  # Incrementa la velocidad en un 10%