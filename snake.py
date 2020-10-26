import turtle

# creating a window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)

# snake
snake = turtle.Turtle()
snake.color("red")
snake.shape("square")
snake.shapesize(2, 2)
snake.penup()

# food
food = turtle.Turtle()
food.goto(-80,0)
food.color("blue")
food.shape("square")
food.speed(0)
food.shapesize(2, 2)
food.penup()


# funções de movimento
def snake_right():
    x = snake.xcor()
    x += 5
    snake.setx(x)

def snake_left():
    x = snake.xcor()
    x-= 5
    snake.setx(x)

def snake_up():
    y = snake.ycor()
    y+= 5
    snake.sety(y)

def snake_down():
    y = snake.ycor()
    y -= 5
    snake.sety(y)

# configurações do teclado
window.listen()
window.onkey(snake_down, "s")
window.onkeypress(snake_right, "Right")
window.onkeypress(snake_left, "Left")
window.onkeypress(snake_up, "Up")
window.onkeypress(snake_down, "Down")


# Colisão entre snake e food

def overlapping(min_a, max_a, min_b, max_b):
    return min_b <= max_a and min_a <= max_b

def colider(snake, food):
    x_snake = snake.xcor()
    x_food = food.xcor()

    y_snake = snake.ycor()
    y_food = food.ycor()
    
    colider_x = overlapping(x_snake, (x_snake+40), x_food, (x_food+40) )
    colider_y = overlapping(y_snake, (y_snake+40), y_food, (y_food+40) )

    return colider_x and colider_y

# Main game loop

while True:
    window.update()
    if colider(snake, food):
        food.color("white")
    else:
        food.color("blue")