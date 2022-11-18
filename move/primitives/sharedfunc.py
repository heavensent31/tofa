import math

pi2 = math.pi / 2
pi4 = math.pi / 4
pi3 = math.pi / 3

def MakePath(List):
	MarkersList = list()
	Start = True
	for Point in List:
		MarkersList.append('M' if Start else 'L')
		MarkersList.append(str(Point['X']))
		MarkersList.append(str(Point['Y']))
		Start = False
	MarkersList.append('Z')
	return ' '.join(MarkersList)

def MakePoint(X, Y):
	return {'X': float(X), 'Y': float(Y)}

def MovePolar(Center, Angle, Radius):
	X = Center['X'] + (math.sin(Angle) * Radius)
	Y = Center['Y'] + (math.cos(Angle) * Radius)
	return MakePoint(X, Y)

def FindCenter(Point1, Point2):
	X = Point1['X'] + ((Point2['X'] - Point1['X']) / 2)
	Y = Point1['Y'] + ((Point2['Y'] - Point1['Y']) / 2)
	return MakePoint(X, Y) 
