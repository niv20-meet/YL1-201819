import random 
from turtle import *
class Square (Turtle):
	def __init__ (self,size ):
		self.size = size 
		self.shape ("square")
		self.random_color = random_color
	def random_color(self):
		r=random.randint(0,256)
		g=random.randint(0,256)
		b=random.randint(0,256)
		self.color(r, g, b)
