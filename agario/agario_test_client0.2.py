import turtle 
import time 
import random
import math
import socket
from ball import Ball
import struct

s = socket.socket()
host ="192.168.252.172"
port = int(turtle.textinput(" ","enter Game Pin"))

window = turtle.Screen()
window.setup(1280,800)

#USE THIS FOR FULLSCREEN:
window.screensize()
window.setup(width = 1.0, height = 1.0)

#window.addshape("duck.gif")
turtle.bgpic("blue-graph.gif")
turtle.colormode(1)
turtle.tracer(0)
turtle.ht()
running=True 
screen_width = turtle.getcanvas().winfo_width()//2
screen_height = turtle.getcanvas().winfo_height()//2


pen = turtle.Turtle()
pen.pu()
pen.ht()
pen.speed(0)

my_ball_name = turtle.Turtle()
my_ball_name.speed(0)
my_ball_name.pu()
my_ball_name.ht()
my_ball_name.color("white")

def Write(text,size,x,y):
        pen.goto(x,y)
        pen.write(text, move=False, align="center", font=("arial", size, "bold"))

Write("Quick, Enter Full Screen\nBefore The Countdown Is Over",20,0,0)
Write("5",30,0,-40)
my_ball=Ball(100,300,6,6,"blue",30)
player_2=Ball(100,300,6,6,"red",30)




def Distance(x1,y1,x2,y2):
        d=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        return d




def move_all_balls():
	global X
	global Y
	global R
	global ball_xyr
	global inpt
	X=[]
	Y=[]
	R=[]
	ball_xyr = []
	#print("max range:",len(int_list)//3)
	for bit in range(1,len(int_list)//3):
		X.append(int(int_list[bit*3]))
		Y.append(int(int_list[bit*3+1]))
		R.append(int(int_list[bit*3+2])/10)
	#print(len(BALLS))
	#print(len(X),X)
	for ball in range(len(BALLS)):
		BALLS[ball].goto(X[ball],Y[ball])
		BALLS[ball].shapesize(R[ball])
	#print(ball_xyr)
	


def movearound():
	X_coordinate=turtle.getcanvas().winfo_pointerx() - screen_width
	Y_coordinate=screen_height - turtle.getcanvas().winfo_pointery()
	#my_ball.goto(X_coordinate,Y_coordinate+my_ball.r)
	send_r = int(list(my_ball.shapesize())[0])*10
	global message
	my_cor = [int(X_coordinate),int(Y_coordinate)]
	message = struct.pack(">{}l".format(2), *my_cor)

print("waiting to connect")
s.connect((host, port))
talk = True
ball_xyr = []
time.sleep(1)
pen.clear()
Write("Quick, Enter Full Screen\nBefore The Countdown Is Over",20,0,0)
Write("4",30,0,-40)
time.sleep(1)
pen.clear()
Write("Quick, Enter Full Screen\nBefore The Countdown Is Over",20,0,0)
Write("3",30,0,-40)
time.sleep(1)
pen.clear()
Write("Quick, Enter Full Screen\nBefore The Countdown Is Over",20,0,0)
Write("2",30,0,-40)
time.sleep(1)
pen.clear()
Write("Quick, Enter Full Screen\nBefore The Countdown Is Over",20,0,0)
Write("1",30,0,-40)
time.sleep(1)
pen.clear()
turtle.pu()
turtle.goto(-screen_width*2 + 130,screen_height*2 - 20)
turtle.write(arg="size:",move=True,align="center",font=("Arial",36,"normal"))
turtle.goto(0,0)
global message, BALLS
global in_x
global in_y
BALLS = None
temp = ""
all_info = []
X=[]
Y=[]
R=[]

def create_balls(number_of_balls):
        global BALLS
        minimum_ball_radius=10
        maximum_ball_radius=80
        minimum_ball_dx=-3
        maximum_ball_dx=3
        minimum_ball_dy=-3
        maximum_ball_dy=3
        BALLS=[]

        for ball in range(number_of_balls):
                x=random.randint(-screen_width*2+maximum_ball_radius,screen_width*2-maximum_ball_radius)
                y=random.randint(-screen_height*2+maximum_ball_radius,screen_height*2-maximum_ball_radius)
                dx=random.randint(minimum_ball_dx,maximum_ball_dx)
                dy=random.randint(minimum_ball_dy,maximum_ball_dy)             

                r=random.randint(minimum_ball_radius,maximum_ball_radius)
                color = (random.random(), random.random(), random.random())

                ball1=Ball(x,y,dx,dy,color,r)
                BALLS.append(ball1) 

while running == True:
        
        message = s.recv(1024)
        num_digits = int(message[0:1].decode())
        if num_digits == 0:
                write("game over",30,0,0)
                running=False
                break
        list_length = int(message[1:1+num_digits].decode())
        int_list = struct.unpack(">{}l".format(list_length), message[1+num_digits:])

        if BALLS == None:
                create_balls((list_length-3)//3)
        in_x,in_y,in_r,my_x,my_y,my_r = int_list[0:6]
        #print(int_list[0:6])
        
        movearound()
        player_2.goto(int(in_x),int(in_y))
        player_2.shapesize(int(in_r)/10)
        move_all_balls()
        s.sendall(message)
        pen.clear()
        my_size= my_r
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
        Write(str(int(my_size)),36,-screen_width + 150,screen_height - 67)	
        turtle.update()
        time.sleep(.01)

turtle.pencolor("blue")
turtle.write(arg="game over",move=False,align="center",font=("Arial",42,"bold"))


turtle.mainloop()


