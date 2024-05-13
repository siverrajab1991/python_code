import math 

pi = math.pi 

def kreis(radius,hoehe):
	radius = input("Gebe eine Zahl für den Radius ein: ")
	hoehe = input("Nun gebe eine Zahl für die Höhe ein: ")
	v = pi*(radius**2)*hoehe 
	return f"das Volumen beträgt {v}"
