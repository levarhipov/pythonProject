import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides = 5
colors = ("red", "blue", "green", "salmon", "lemon chiffon")
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

input()