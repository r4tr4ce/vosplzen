import turtle

def vykresli(x, y, n):
    turtle.penup()
    turtle.goto(x, y)  
    turtle.pendown()
    
    turtle.write("LB", font=("Arial", 20, "bold"))

    side_length = 100 / (n * 1.5)  
    angle = 360 / n  

    turtle.penup()
    turtle.goto(x + 60, y + 5)  
    turtle.pendown()

    for _ in range(n):
        turtle.forward(side_length)
        turtle.left(angle)

    turtle.done()

vykresli(-100, 100, 6)  
