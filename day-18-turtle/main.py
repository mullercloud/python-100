from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

my_turtle.shape("turtle")
my_turtle.color("green")

# directions = [0, 90, 180, 270]

move = True


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def turtle_move():
    directions = random.randint(0, 360)

    my_turtle.color(random_color())
    my_turtle.pensize(1)
    my_turtle.speed(5)
    my_turtle.forward(100)
    my_turtle.right(directions)


while move:
    turtle_move()



screen.exitonclick()


