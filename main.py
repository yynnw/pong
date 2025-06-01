import turtle
from player import Player
from ball import Ball
from scoreboard import Scoreboard



screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.bgcolor('black')
turtle.tracer(0)

r_player = Player('right')
r_scoreboard = Scoreboard('r_player')
l_player = Player('left')
l_scoreboard = Scoreboard('l_player')

ball = Ball()

screen.listen()

screen.onkeypress(r_player.move_up, 'Up')
screen.onkeypress(r_player.move_down, 'Down')

screen.onkeypress(l_player.move_up, 'w')
screen.onkeypress(l_player.move_down, 's')

y_speed = 1
x_speed = 1

r_score = 0
l_score = 0
while True:
	r_scoreboard.update_score(r_score)
	l_scoreboard.update_score(l_score)
	if ball.ycor() > 230 or ball.ycor() < -230:
		y_speed *= -1
	if ball.xcor() > 338 and ball.distance(r_player) < 50.0 \
	or ball.xcor() < -338 and ball.distance(l_player) < 50.0:
		x_speed *= -1
		ball.move_ball(y_speed, x_speed * 10)
	if ball.xcor() > 400:
		l_score += 1
		l_scoreboard.update_score(l_score)
		ball.goto(0, 0 )
	if ball.xcor() < -400:
		r_score += 1
		r_scoreboard.update_score(r_score)
		ball.goto(0, 0 )


	ball.move_ball(y_speed, x_speed)
	
	turtle.update()

turtle.done()
	