import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
tim.speed('fastest')
t.colormode(255)
tim.penup()
tim.hideturtle()


color_list = [(236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132),
              (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66),
              (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162),
              (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),
              (179, 17, 8), (233, 66, 34)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()

horizontal_length = t.numinput("Number of Rows", "Enter number of rows (min 5, max 20): ", 10, 5, 20)
vertical_length = t.numinput("Number of Columns", "Enter number of columns (min 5, max 20): ", 10, 5, 20)

for i in range(int(vertical_length)):
    for _ in range(int(horizontal_length)):
        tim.pendown()
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50*int(horizontal_length))
    tim.setheading(0)

t.exitonclick()