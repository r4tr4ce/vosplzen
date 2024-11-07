import turtle

def vykresli(x, y, n):
    """
    Vykreslí iniciály 'JP' následované pravidelným n-úhelníkem pomocí knihovny turtle.
    
    Parameters:
    x (int): X-souřadnice levého horního rohu vykreslované oblasti.
    y (int): Y-souřadnice levého horního rohu vykreslované oblasti.
    n (int): Počet stran pravidelného n-úhelníku, který bude vykreslen za iniciály JP.
    """
    # Nastavení výchozí pozice turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Kreslení písmena J
    turtle.setheading(-90) # otočení směrem dolů
    turtle.forward(15)
    turtle.circle(25, 180)
    turtle.forward(70)

    # Přesun na místo pro vykreslení písmena P
    turtle.penup()
    turtle.goto(x + 80, y + 55)
    turtle.pendown()

    # Kreslení písmena P
    turtle.setheading(-90) # otočení směrem dolů
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)
    turtle.circle(-25, 180)

    # Přesun na místo pro vykreslení n-úhelníku
    turtle.penup()
    turtle.goto(x + 150, y - 50)  # posun vpravo níže od iniciál
    turtle.pendown()

    # Kreslení pravidelného n-úhelníku
    angle = 360 / n
    side_length = 40  # Délka strany

    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.done()

vykresli(-100, 100, 6)
