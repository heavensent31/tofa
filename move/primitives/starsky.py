from sharedfunc import *

StellarClasses = {
	"O": "91b5ff",
	"B": "a7c3ff",
	"A": "cfdcff",
	"F": "f1f1fd",
	"G": "fdeee6",
	"K": "ffdab5",
	"M": "ffb566",
	"L": "ff7e07",
	"T": "ff3b00"
}

def DrawLittleStar(Center, Radius, Class):
	PointList = list()
	for Point in range(4): 
		VectorAngle = pi2 * Point
		PointList.append(MovePolar(Center, VectorAngle, Radius))
	DString = MakePath(PointList)
	return f'<path style="fill:#{StellarClasses[Class]}" d="{DString}" />'
