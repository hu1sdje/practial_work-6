import turtle
import turtle
r1, x1, y1 = map(int, input().split())
turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)
r2, x2, y2 = map(int, input().split())
turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r1)
if ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 > r2 + r1:
    turtle.write('Окружности лежат одна вне другой, не касаясь')
elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 == r2 + r1:
    turtle.write('Окружности имеют общее касание')
elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 < r2 + r1 and (x2 - x1) ** 2 + (y2 - y1) ** 2 < abs(r2 - r1):
    turtle.write('Окружности пересекаются')
elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 == abs(r2 - r1):
    turtle.write('Окружности имеют внутреннее касание')
elif ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 > abs(r2 - r1):
    turtle.write('Одна окружность лежит внутри другой, не касаясь')
turtle.done()