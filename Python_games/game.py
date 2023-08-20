import time
import turtle

#WINDOW

window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor('brown')
window.title('PONG')
window.tracer(0)

#Left hand side bat
left_bat = turtle.Turtle()
left_bat.speed(0)
left_bat.shape('square')
left_bat.shapesize(stretch_wid=5, stretch_len=1)
left_bat.color('white')
left_bat.penup()
left_bat.goto(-350,0)


#Right hand side bat
right_bat = turtle.Turtle()
right_bat.speed(0)
right_bat.shape('square')
right_bat.shapesize(stretch_wid=5, stretch_len=1)
right_bat.color('white')
right_bat.penup()
right_bat.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)

def right_bat_up():
   y = left_bat.ycor()
   y += 30
   left_bat.sety(y)

while True:
   window.update()





# manoturtle = turtle.Turtle()
#
# manoturtle.speed(1)
# manoturtle.shape('square')
# manoturtle.color('green')
# manoturtle.shapesize(stretch_wid=5, stretch_len=1)
# manoturtle.penup()
#
# manoturtle.forward(100)
# manoturtle.right(90)
# manoturtle.forward(100)
# manoturtle.right(90)
# manoturtle.forward(100)
# manoturtle.right(90)
# manoturtle.forward(100)
# manoturtle.right(90)


