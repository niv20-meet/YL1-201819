import turtle 
import time 
import random
import math
from ball import Ball
from pygame import mixer


mixer.init()
mixer.music.load('bgmusic.mp3')
mixer.music.play()
turtle.bgpic("blue-graph-paper-grid-purple-1920x1080-c2-e6e6fa-5f9ea0-l2-3-93-a-0-f-20.gif")
turtle.colormode(1)
turtle.tracer(0)
turtle.ht()
running=True 
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

my_ball=Ball(100,300,6,6,"blue",30)
my_ball.register_shape(duck.gif)
number_of_balls=8
minimum_ball_radius=10
maximum_ball_radius=80
minimum_ball_dx=-4
maximum_ball_dx=4
minimum_ball_dy=-4
maximum_ball_dy=4
BALLS=[]

for ball in range(number_of_balls):
	x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
	y=random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
	dx=random.randint(minimum_ball_dx,maximum_ball_dx)
	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	while dx == 0 or dy==0 :
		dx=random.randint(minimum_ball_dx,maximum_ball_dx)
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)


	r=random.randint(minimum_ball_radius,maximum_ball_radius)
	color = (random.random(), random.random(), random.random())

	ball1=Ball(x,y,dx,dy,color,r)
	BALLS.append(ball1) 

def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width,screen_height)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False 
	d=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))	
	if d<=ball_a.r+ball_b.r	:
		return True
	else :
		return False
def check_all_balls_collision():
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a	in all_balls:
		for ball_b in all_balls:
			if collide(ball_a,ball_b):
				global running
				x=random.randint(int(-screen_width+maximum_ball_radius),int(screen_width-maximum_ball_radius))
				y=random.randint(int(-screen_height + maximum_ball_radius),int(screen_height - maximum_ball_radius))
				dx=random.randint(minimum_ball_dx,maximum_ball_dx)
				dy=random.randint(minimum_ball_dy,maximum_ball_dy)
				while dx == 0 or dy==0 :
					dx=random.randint(minimum_ball_dx,maximum_ball_dx)
					dy=random.randint(minimum_ball_dy,maximum_ball_dy)
				r=random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.random(), random.random(), random.random())
				if ball_a.r< ball_b.r:
					if ball_a == my_ball:
						running = False	
					ball_a.new_Ball(x,y,dx,dy,color,r)
					ball_b.r+=1
					ball_b.shapesize(ball_b.r/10)
						
				if ball_b.r< ball_a.r:
					if ball_b == my_ball:
						running = False
					ball_b.new_Ball(x,y,dx,dy,color,r)
					ball_a.r+=1
					ball_a.shapesize(ball_a.r/10)
					


def movearound():
	X_coordinate=turtle.getcanvas().winfo_pointerx() - screen_width
	Y_coordinate=screen_height - turtle.getcanvas().winfo_pointery()
	my_ball.goto(X_coordinate,Y_coordinate)

while running == True:
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	movearound()
	move_all_balls()	
	check_all_balls_collision()
	turtle.update()
	time.sleep(.1)

turtle.pencolor("blue")
turtle.write(arg="end game",move=True,align="center",font=("Arial",36,"normal"))


turtle.mainloop()


