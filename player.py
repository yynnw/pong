import turtle

class Player(turtle.Turtle):
	"""initialize the player by specifying 'right' or 'left'"""
	def __init__(self, side):
		super().__init__() 
		if side == 'right':
			self.start_side = 360
		elif side == 'left':
			self.start_side = -360
		self.penup()
		self.shape('square')
		self.color('white')
		self.shapesize(stretch_wid=4, stretch_len=1)
		self.goto(self.start_side,0)


	def move_up(self):
		if self.ycor() < 205:
			self.sety(self.ycor() + 10)

	def move_down(self):
		if self.ycor() > -195:
			self.sety(self.ycor() - 10)