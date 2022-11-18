from sharedfunc import *

def DrawHexagon(Center, Angle, Radius, Style):
	PointList = list()
	for Point in range(6): 
		VectorAngle = (pi3 * Point) + Angle
		PointList.append(MovePolar(Center, VectorAngle, Radius))
	DString = MakePath(PointList)
	return f'<path style="{Style}" d="{DString}" />'

def DrawCrater(Center, Number, Angle, Radius, CraterRadius, Opacity):
	PointList = list()
	NewRadius = Radius * (math.sqrt(3) / 3)
	NewCenter = MovePolar(Center, ((Number + 0.5) * pi3) + Angle, NewRadius)
	for Point in range(3): 
		VectorAngle = (pi3 * (Point + (0.25 if Number % 2 == 1 else -0.25)) * 2) + Angle
		PointList.append(MovePolar(NewCenter, VectorAngle, CraterRadius * NewRadius))
		DString = MakePath(PointList)
	return f'<path style="fill:#76766d;opacity:{Opacity}" d="{DString}" />'

def DrawMoonShadow(Center, Angle, Radius, Phase):
	PhaseAngle = 0
	PointList = list()
	Radii = [0] * 6
	Radii[1] = 1 if Phase < 0.5 else math.cos(math.pi * Phase * 2)
	Radii[2] = 1 if Phase < 0.5 else math.cos(math.pi * Phase * 2)
	Radii[3] = 1 if abs(Phase - 0.5) < 0.4 else 1 - (0.5 - abs(Phase - 0.5))
	Radii[4] = math.cos(math.pi * Phase * 2) if Phase < 0.5 else 1
	Radii[5] = math.cos(math.pi * Phase * 2) if Phase < 0.5 else 1
	Radii[0] = 1 if abs(Phase - 0.5) < 0.4 else 1 - (0.5 - abs(Phase - 0.5))
	for Point in range(6): 
		VectorAngle = (pi3 * Point) + Angle
		PointList.append(MovePolar(Center, VectorAngle, Radius * Radii[Point]))
	if Radii[1] < 0:
		Temp = PointList[1]
		PointList[1] = PointList[2]
		PointList[2] = Temp
	if Radii[4] < 0:
		Temp = PointList[4]
		PointList[4] = PointList[5]
		PointList[5] = Temp
	DString = MakePath(PointList)
	return f'<path style="fill:#000000;opacity:0.99" d="{DString}" />'

def DrawMoonLip(Center, Number, Angle, Radius):
	Point1 = MovePolar(Center, (Number * pi3) + Angle, Radius)
	Point2 = MovePolar(Center, ((Number + 1) * pi3) + Angle, Radius)
	DString = MakePath([Center, Point1, Point2])
	return f'<path style="fill:url(#MoonHaloPart{Number + 1})" d="{DString}" />'

def DefineMoonGrad(Center, Number, Angle, Radius):
	Vector1 = MovePolar(Center, (Number * pi3) + Angle, Radius)
	Vector2 = MovePolar(Center, ((Number + 1) * pi3) + Angle, Radius)
	Median = FindCenter(Vector1, Vector2)
	return f'<linearGradient id="MoonHaloPart{Number + 1}" xlink:href="#MoonHaloBase" x1="{Center["X"]}" y1="{Center["Y"]}" x2="{Median["X"]}" y2="{Median["Y"]}" gradientUnits="userSpaceOnUse" />'

def DrawMoon(Center, Angle, MoonRadius, HaloRadius, Phase):
	Result = list()
	Result.append('<svg width="4cm" height="4cm" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" version="1.1">')
	Result.append('<g id="MoonObject">')
	Result.append('<defs id="MoonDefs">')
	Result.append(f'<linearGradient id="MoonHaloBase"><stop style="stop-color:#ffffff;stop-opacity:{0.5 - abs(Phase - 0.5)};" offset="0" /><stop style="stop-color:#e7e7e5;stop-opacity:0;" offset="1" /></linearGradient>')
	for Point in range(6): Result.append(DefineMoonGrad(Center, Point, Angle, HaloRadius))
	Result.append('</defs>')
	Result.append(DrawHexagon(Center, Angle, MoonRadius, "fill:#e7e7e5"))
	Result.append(DrawCrater(Center, 0, Angle, MoonRadius, 0.5, 0.7))
	Result.append(DrawCrater(Center, 2, Angle, MoonRadius, 0.25, 0.6))
	Result.append(DrawCrater(Center, 3, Angle, MoonRadius, 1, 0.6))
	Result.append(DrawCrater(Center, 5, Angle, MoonRadius, 1, 0.6))
	Result.append(DrawMoonShadow(Center, Angle, MoonRadius * 1.01, Phase))
	for Point in range(6): Result.append(DrawMoonLip(Center, Point, Angle, HaloRadius))
	Result.append('</g>')
	Result.append('</svg>')
	return ''.join(Result)

with open('test.svg', 'wt') as f: f.write(DrawMoon(MakePoint(200, 200), 0, 50, 200, 0.5))
