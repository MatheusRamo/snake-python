from random import randint
import turtle

# criando a janela
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=650, height=650)

# snake
tan_snake = 1

snake = turtle.Turtle()
snake.penup()
snake.goto(10,10)
snake.color("yellow")
snake.shape("square")
snake.shapesize(1, tan_snake)

# comida
food = turtle.Turtle()
food.penup()
food.speed(0)
food.goto(-110,10)
food.color("yellow")
food.shape("square")
food.shapesize(1, 1)

# pen
pen = turtle.Turtle()
pen.penup()
pen.goto(-300, 300)
pen.pen(pencolor="white", fillcolor="orange", pensize=3, speed=10)
pen.shape("classic")
pen.pendown()

def desenha_quadrado(pen, n):
    for i in range(4):
        pen.forward(n)
        pen.left(90)

# Desenha o board
def desenha_board(pen, tamanho):
    for row in range(tamanho):
        for column in range(tamanho):
            pen.begin_fill()
            pen.goto((-300+column*20), (300-row*20))
            pen.pendown()
            desenha_quadrado(pen,20)
            pen.end_fill()
        pen.penup()


# funções de movimento
def snake_right():
    x = snake.xcor()
    x += 20
    snake.setx(x)

def snake_left():
    x = snake.xcor()
    x-= 20
    snake.setx(x)

def snake_up():
    y = snake.ycor()
    y+= 20
    snake.sety(y)

def snake_down():
    y = snake.ycor()
    y -= 20
    snake.sety(y)

# configurações do teclado
window.listen()
window.onkey(snake_right, "Right")
window.onkey(snake_left, "Left")
window.onkey(snake_up, "Up")
window.onkey(snake_down, "Down")


# Colisão entre snake e food
def overlapping(min_a, max_a, min_b, max_b):
    return min_b <= max_a and min_a <= max_b

def colider(snake, food):
    x_snake = snake.xcor()
    x_food = food.xcor()

    y_snake = snake.ycor()
    y_food = food.ycor()
    
    colider_x = overlapping(x_snake, (x_snake+20), x_food, (x_food+20) )
    colider_y = overlapping(y_snake, (y_snake+20), y_food, (y_food+20) )

    return colider_x and colider_y

def gera_x():
    numero = randint(-15,15)
    x = 20*numero + 10
    return x

desenha_board(pen, 1)


# Main game loop
while True:
    window.update()
    if colider(snake, food):
        food.penup()
        food.goto(gera_x(), gera_x())
        tan_snake += 1
        snake.shapesize(1, tan_snake)

