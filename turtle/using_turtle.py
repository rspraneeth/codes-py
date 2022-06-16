from random import choice, randint, random
from turtle import Turtle, Screen
from random import randint

t = Turtle()
sc = Screen()

# drawing a square
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# drawing a dashed line
# for i in range(5):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# drawing different polygon shapes one after another with random color for each shape
# n = int(input("How many sides for the final polygon: "))
# sides = 3
# for i in range(n-2):
#     sc.colormode(255)
#     t.pencolor(randint(1, 256), randint(1, 256), randint(1, 256))
#     for j in range(sides):
#         t.forward(100)
#         t.right(360/sides)
#     sides += 1

# random walk
sc.screensize(700, 500)
def rand_color():
    sc.colormode(255)
    t.pencolor(randint(1, 256), randint(1, 256), randint(1, 256))

loop = True
t.pensize(5)
q = 0
while loop:
    a = randint(1,4)
    if a == 1:
        rand_color()
        t.forward(20)
    elif a == 2:
        rand_color()
        t.left(90)
    elif a== 3:
        rand_color()
        t.forward(20)
    else:
        rand_color()
        t.back(20)
    q += 1
    if q == 1000:
        loop = False




sc.exitonclick()