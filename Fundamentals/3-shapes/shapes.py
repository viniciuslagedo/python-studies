import turtle

def draw_square(this_turtle):
    for i in range(1, 5):
        this_turtle.forward(100)
        this_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    pointer = turtle.Turtle()
    pointer.color("white")
    pointer.speed(2)

    for i in range(1, 37):
        draw_square(pointer)
        pointer.right(10)

draw_art()