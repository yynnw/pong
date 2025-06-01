import turtle
import time

class Ball(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.shape('circle')
		self.color('white')

	def move_ball(self, y_speed, x_speed):
		time.sleep(.007)
		self.setx(self.xcor() + x_speed)
		self.sety(self.ycor() + y_speed)