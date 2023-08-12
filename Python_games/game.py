import time
import turtle

#WINDOW

window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor('brown')
window.title('PONG')
window.tracer(0)

#Left hand side bat
left_hand_side_bat = turtle.Turtle()
left_hand_side_bat.speed(0)
left_hand_side_bat.shape('square')
left_hand_side_bat.shapesize(stretch_wid=5, stretch_len=1)
left_hand_side_bat.color('white')
left_hand_side_bat.penup()
left_hand_side_bat.goto(-350,0)
#time.sleep(15)
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


