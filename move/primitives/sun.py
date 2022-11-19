from sharedfunc import *
	
def DrawSunSquare(Center, Angle, Radius, Style):
	PointList = list()
	for Point in range(4): 
		VectorAngle = (pi2 * (Point + 0.5)) + Angle
		PointList.append(MovePolar(Center, VectorAngle, Radius))
	DString = MakePath(PointList)
	return f'<path style="{Style}" d="{DString}" />'

def DefineSunGrad(Center, Number, Angle, Radius):
	Vector1 = MovePolar(Center, (Number * pi4) + Angle, Radius)
	Vector2 = MovePolar(Center, ((Number + 1) * pi4) + Angle, Radius)
	Median = FindCenter(Vector1, Vector2)
	return f'<linearGradient id="SunHaloPart{Number + 1}" xlink:href="#SunHaloBase" x1="{Center["X"]}" y1="{Center["Y"]}" x2="{Median["X"]}" y2="{Median["Y"]}" gradientUnits="userSpaceOnUse" />'

def DrawSunLip(Center, Number, Angle, Radius):
	Point1 = MovePolar(Center, (Number * pi4) + Angle, Radius)
	Point2 = MovePolar(Center, ((Number + 1) * pi4) + Angle, Radius)
	DString = MakePath([Center, Point1, Point2])
	return f'<path style="fill:url(#SunHaloPart{Number + 1})" d="{DString}" />'

def DrawSun(Center, Angle, SunRadius, HaloRadius):
	Result = list()
	Result.append('<g id="SunObject">')
	Result.append('<defs id="SunDefs">')
	Result.append('<linearGradient id="SunHaloBase"><stop style="stop-color:#ffffff;stop-opacity:1;" offset="0" /><stop style="stop-color:#ffffff;stop-opacity:0;" offset="1" /></linearGradient>')
	for Point in range(8): Result.append(DefineSunGrad(Center, Point, Angle, HaloRadius))
	Result.append('</defs>')
	for Point in range(8): Result.append(DrawSunLip(Center, Point, Angle, HaloRadius))
	Result.append(DrawSunSquare(Center, Angle, SunRadius, "fill:#ffffff"))
	Result.append(DrawSunSquare(Center, Angle + pi4, SunRadius, "fill:#ffffff"))
	Result.append('</g>')
	return ''.join(Result)
