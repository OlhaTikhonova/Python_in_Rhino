import rhinoscriptsyntax as rs
import random
import math

def blipCurve(z,radius):
	listOfPoints=[]
	pi = math.pi
	theta  = 0
	while theta<=2*pi:
		r = radius * (1 - math.sin(theta)) #BLIP in circle that forms heart 
		x = 5*math.cos(z/5) + (r)*math.cos(theta)
		y = 5*math.cos(z/5)+(r)*math.sin(theta)
		listOfPoints.append((x,y,z))
		theta+=0.01
	return rs.AddInterpCurve(listOfPoints,3)

z=0
radius = 100
while z<200:
	if z==50: # Huge Blip
		aCurve = blipCurve(z,radius+20)
	else:
		aCurve = blipCurve(z,radius)
	z+=1
	radius-=0.4
