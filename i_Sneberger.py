import turtle

pen = turtle.Turtle()

def draw_shape(x, y, n):
    # Zacatek ohraniceni
    pen.pencolor("red")
    pen.penup()
    pen.goto(-100, 100)
    pen.pendown()
    pen.setheading(0)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.penup()
    # Konec ohraniceni
    
    # Zacatek F
    pen.pencolor("blue")
    pen.goto(x, y-90)
    pen.pendown()
    pen.setheading(90)
    pen.forward(80)
    pen.right(90)
    pen.forward(20)
    pen.penup()
    pen.goto(x, y-45)
    pen.pendown()
    pen.forward(20)
    pen.penup()
    # Konec F
    
    # Zacatek S
    pen.goto(x+23, y-62)
    pen.pendown()
    pen.right(90)
    pen.forward(15)
    pen.left(30)
    pen.forward(15)
    pen.left(110)
    pen.forward(15)
    pen.left(40)
    pen.forward(15)
    pen.left(30)
    pen.forward(30)
    pen.right(30)
    pen.forward(15)
    pen.right(30)
    pen.forward(15)
    pen.right(110)
    pen.forward(15)
    pen.right(40)
    pen.forward(15)
    pen.penup()
    # Konec S
    
    # Zacatek hacku
    pen.goto(x+23, y)
    pen.pendown()
    pen.setheading(330)
    pen.forward(13)
    pen.left(65)
    pen.forward(13)
    pen.penup()
    # Konec hacku
    
    # Zacatek devitiuhelniku
    pen.pencolor("purple")
    pen.goto(x + 47, y - 37)
    pen.pendown()
    side_length = 17
    
    for _ in range(n):
        pen.forward(side_length)
        pen.right(360 / n)
    # Konec devitiuhelniku
    pen.hideturtle()

pen.speed(5)
turtle.title("Vykreslení iniciálů FŠ a 9-úhelníku")

draw_shape(-95, 95, 9)

turtle.done()