import turtle

class Scoreboard(turtle.Turtle):
	def __init__(self, player):
		super().__init__()
		self.player = player
		self.penup()
		self.color('white')

	def update_score(self, score):
		if self.player == 'r_player':
			self.goto(300, 200)
		if self.player == 'l_player':
			self.goto(-300, 200)
		self.hideturtle()
		self.clear()
		self.write(f"Points: {score}", align='center', font=('Arial', 18, 'bold'))
