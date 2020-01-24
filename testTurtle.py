import turtle

def scrivi_quadrato():
    lato = 25
    angolo = 90
    for _ in range(4):
        turtle.forward(lato)
        turtle.right(angolo)

turtle.shape("turtle")

rotation = 0

for _ in range(1):
    turtle.right(rotation)
    scrivi_quadrato()
    rotation = rotation +15

turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)

turtle.exitonclick()


