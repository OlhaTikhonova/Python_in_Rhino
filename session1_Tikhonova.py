import rhinoscriptsyntax as rs
import random
import math

z=-100
radius = 30
pi = math.pi

while z<=-95:
	theta  = 0
	while theta<2*pi:
		x = radius*math.cos(theta)
		y = radius*math.sin(theta)
		rs.AddPoint ((x,y,z))
		theta+=.1
	z+=.01

count = 0
theta  = 0
a = 3*pi/2 - z/15
while z>-95 and z<=100:
	if count % 4 ==0:
		x = 3*math.cos(z/15 + a) + (radius+20)*math.cos(theta)
		y = 3*math.cos(z/15 + a)+(radius+20)*math.sin(theta)
	else:	
		x = 3*math.cos(z/15 + a) + radius*math.cos(theta)
		y = 3*math.cos(z/15 + a)+radius*math.sin(theta)
	rs.AddPoint ((x,y,z))
	radius -= .00154
	theta+=1
	z+=.01
	count+=1
