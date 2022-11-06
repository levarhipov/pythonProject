# My Python Programs

Using Turtle to draw 

    import turtle
    t = turtle.Pen()
    turtle.bgcolor("black")
    sides = 6
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for x in range(360):
        t.pencolor(colors[x%sides])
        t.forward(x * 3/sides + x)
        t.left(360/sides + 1)
        t.width(x*sides/200)


![alt text](images/01_ColorSpiralHexagonal.png)
