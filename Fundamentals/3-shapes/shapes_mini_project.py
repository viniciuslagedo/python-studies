def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    pointer = turtle.Turtle()
    pointer.shape("turtle")
    pointer.color("white")
    pointer.speed(2)

    pointer.right(65)
    pointer.forward(100)
    pointer.right(-130)
    pointer.forward(100)

    pointer.penup()
    pointer.setx(100)
    pointer.setheading(270)

    pointer.pendown()
    pointer.forward(100)
    pointer.left(90)
    pointer.forward(100)
        
    window.exitonclick()

draw_art()