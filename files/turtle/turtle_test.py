import turtle
from time import sleep

t = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen','red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen', 'red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink', 'orange', 'blue', 'yellow', 'lightgreen']:
    t.color(c)
    t.forward(75)
    t.left(50)
t.penup()
t.forward(85)
t.pendown()
for d in ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink']:
	t.color(d)
	t.forward(85)
	t.right(60)
t.penup()
t.downwards(85)
t.pendown()
for d in ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'purple', 'pink']:
	t.color(d)
	t.forward(85)
	t.right(90)
sleep (5)