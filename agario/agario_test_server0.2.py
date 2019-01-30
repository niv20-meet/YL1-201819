import turtle 
import time 
import random
import math
import socket    
from ball import Ball
import struct

#server setup
try:
        s = socket.socket()
        host = '127.0.0.1' #'192.168.252.172' #enter ip address
except:
        pen.clear()
        Write("unable to set up connection",60,0,0)
pen2=turtle.Turtle()
pen2.ht()
pen2.speed(0)
pen2.pensize(3)
pen2.pu()
pen2.goto(0,50)
pen2.pd()
pen2.goto(200,50)
pen2.goto(200,0)
pen2.goto(-200,0)
pen2.goto(-200,50)
pen2.goto(0,50)
pen = turtle.Turtle()
pen.pu()
pen.ht()
pen.speed(0)
pen.color('blue')
def Write(text,size,x,y):
        pen.goto(x,y)
        pen.write(text, move=False, align="center", font=("AR BLANCA", size, "bold"))

port = 1234 #random.randint(10000,65535)           # Reserve a port for your service.
Write(str(" AGARIO  Game Pin: "+str(port)),24,0,0)#gmae port printing 
s.bind((host, port))        # Bind to the port



window = turtle.Screen()   #game screen set up in the begining
window.setup(600,550)

#USE FOR FULLSCREEN
#window.screensize()
#window.setup(width = 1.0, height = 1.0)

turtle.bgpic("blue-graph.gif")
turtle.colormode(1)
turtle.tracer(0)
turtle.ht()
running=True 
screen_width = turtle.getcanvas().winfo_width()//2
screen_height = turtle.getcanvas().winfo_height()//2




my_ball=Ball(100,300,6,6,"blue",20)     #players set up 
player_2=Ball(100,300,6,6,"red",23)

#bots set up 
number_of_balls=3
minimum_ball_radius=10
maximum_ball_radius=80
minimum_ball_dx=-2
maximum_ball_dx=2
minimum_ball_dy=-2
maximum_ball_dy=2
BALLS=[]







def Distance(x1,y1,x2,y2):
        d=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        return d

#Add player_2 ball to BALLS list, so there are now num_balls+1 balls in the list	
BALLS.append(player_2)

for ball in range(number_of_balls):
	x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
	y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
	dx=random.randint(minimum_ball_dx,maximum_ball_dx)
	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	while dx == 0 or dy==0 :
		dx=random.randint(minimum_ball_dx,maximum_ball_dx)
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	while Distance(my_ball.xcor(), my_ball.ycor(), x, y) < 130 :
		new_x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
		new_y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
		x=new_x
		y=new_y
        

	r=random.randint(minimum_ball_radius,maximum_ball_radius)
	color = (random.random(), random.random(), random.random())

	ball1=Ball(x,y,dx,dy,color,r)
	BALLS.append(ball1)



def move_all_balls():
	global ball_xyr
	ball_xyr = []
	for ball in BALLS:
		ball.move(screen_width,screen_height)
		ball_xyr.append(int(ball.xcor()))
		ball_xyr.append(int(ball.ycor()))
		ball_xyr.append(int(list(ball.shapesize())[0]*10))

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
	all_balls.append(player_2)
        #for dots in all_dots:
                #all_balls.append(all_dots)
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
				while Distance(my_ball.xcor(), my_ball.ycor(), x, y) < 130 :
					new_x=random.randint(int(-screen_width+maximum_ball_radius),int(screen_width-maximum_ball_radius))
					new_y=random.randint(int(-screen_height+maximum_ball_radius),int(screen_height-maximum_ball_radius))
					x=new_x
					y=new_y
				r=random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.random(), random.random(), random.random())
				if ball_a.r< ball_b.r:
					if ball_a == my_ball or ball_a == player_2:
						running = False
					if ball_b == player_2:
						color="red"
					ball_a.new_Ball(x,y,dx,dy,color,r)
					ball_b.r+=1
					ball_b.shapesize(ball_b.r/10)
						
				if ball_b.r< ball_a.r:
					if ball_b == my_ball or ball_b == player_2:
						running = False
					if ball_a == player_2:
						color="red"
					ball_b.new_Ball(x,y,dx,dy,color,r)
					ball_a.r+=1
					ball_a.shapesize(ball_a.r/10)
					
print("waiting for client to connect")
s.listen(5)                 # Now wait for client connection.
talk = True
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
pen.clear()
Write("Quick, Enter Full Screen\nBefore The Countdown Is Over",20,0,0)
Write("5",30,0,-40)
ball_xyr=[]
def movearound():
        X_coordinate=turtle.getcanvas().winfo_pointerx() - screen_width
        Y_coordinate=screen_height - turtle.getcanvas().winfo_pointery()
        my_ball.goto(X_coordinate,Y_coordinate) #my_ball.r)
        send_r = int(list(my_ball.shapesize())[0])*10 
        global message
        global all_info
        #print([int(X_coordinate),int(Y_coordinate)])
        my_cor = [int(X_coordinate),int(Y_coordinate),int(send_r)]
        all_info.append(my_cor[0])
        all_info.append(my_cor[1])
        all_info.append(my_cor[2])
        for info in ball_xyr:
                all_info.append(info)

        '''
        message needs to tell the client how many ints to expect, so in addition to the list,
        we will also send the number of elements in the list.
        but in order to decode that number, we need to send the number of digits in that number
        so for a list [123,53,72], we would send:
        1 3 [123,53,72]
        3 is number of ints, and 1 is the number of digits in 3
        '''

        list_length = str(len(all_info)) #number of ints in the list
        num_digits = str(len(list_length)) #number of digits in the length of the list
        message_part_1 = num_digits.encode() 
        message_part_2 = list_length.encode()
        print("all info",all_info)
        message_part_3 = struct.pack(">{}l".format(number_of_balls * 3 + 6), *all_info)
        message = message_part_1 + message_part_2 + message_part_3
        all_info = []

#all_dots=[]
#for dots in range (1000):
    #x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
   # y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
    #dots = Balls(x,y,0,0,'green',2)
    #all_dots.append(dots)
def restart():
        running = True

        
#####NOTE: use a for loop for this:
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
all_info = []

print("PLAYER 2",player_2.shapesize())

while True:
        while running == True:
                print("PLAYER 2",player_2.shapesize(),player_2.pos())
                move_all_balls()
                movearound()
                pen2.clear()
                pen.clear()
                my_size=list(my_ball.shapesize())[0]*10
                Write(str(my_size),36,-screen_width + 150,screen_height - 67)
                screen_width = turtle.getcanvas().winfo_width()/2
                screen_height = turtle.getcanvas().winfo_height()/2	
                check_all_balls_collision()
                turtle.update()
                time.sleep(.01)
                c.sendall(message) #sending data 
                try:  #resiving data 
                        inpt = c.recv(1024)
                        inpt = struct.unpack(">{}l".format(2), inpt)
                        in_x,in_y = inpt
                        player_2.goto(int(in_x),int(in_y))
                except:
                        #pen.clear()
                        #Write("bad connection",60,0,0)
                        print("bad connection")
                #except:
                 #   Write("connection failed, client code unreponsive",24,0,60 )
        #death_message=[10000,1,2,3,2,1,2,3,3,3,3,3,3,3,3,3,4,4,2,1,2,3,4,5,4,3,2,1,2,3]
        message = "0".encode() #struct.pack(">{}l".format(30), *death_message)
        turtle.pencolor("blue")
        turtle.write(arg="game over",move=False,align="center",font=("Arial",36,"normal"))
        turtle.onkeypress(restart,"r")

turtle.mainloop()


