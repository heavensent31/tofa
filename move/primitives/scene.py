from sharedfunc import *
from moon import *
from sun import *
from starsky import *

Result = list()
Result.append('<svg width="800" height="600" viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" version="1.1">')
Result.append(DrawLittleStar(MakePoint(200, 200), 10, 'F'))
# Result.append(DrawSun(MakePoint(200, 200), 20, 50, 200))
# Result.append(DrawMoon(MakePoint(400, 200), 0, 50, 200, 0.5)) 
Result.append('</svg>')

with open('test.svg', 'wt') as f: f.write(''.join(Result))
