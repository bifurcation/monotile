import svgwrite
import math
import copy

# Settings
scale = 100
line_width = '0.1px'
r = math.sqrt(3)
patch = False

# Construct the monotile
points = [
    (-1, 0), 
    (1, 0), 
    (1.5, 0.5 * r),
    (3, 0),
    (4.5, 0.5 * r),
    (4, r),
    (3, r),
    (3, 2*r),
    (1.5, 2.5*r),
    (1, 2*r),
    (0, 2*r),
    (0, r),
    (-1.5, 0.5 * r),
    (-1, 0),
]

hat = svgwrite.shapes.Polygon()
hat.stroke(color='black', width=line_width, linejoin='round')
hat.fill(color='grey')
hat.points.extend(points)

# Add more hats to make a 1-patch
if patch:
    patch_hat = copy.deepcopy(hat)
    patch_hat.fill(color='lightgrey')
    
    hat2 = copy.deepcopy(patch_hat)
    hat2.translate(-4.5, 1.5 * r)
    hat2.rotate(-60)
    
    hat3 = copy.deepcopy(patch_hat)
    hat3.scale(-1, 1)
    hat3.translate(0, 2*r)
    
    hat4 = copy.deepcopy(patch_hat)
    hat4.translate(-1.5, 4.5 * r)
    hat4.rotate(-60)
    
    hat5 = copy.deepcopy(patch_hat)
    hat5.translate(4.5, 1.5 * r)
    hat5.rotate(60)
    
    hat6 = copy.deepcopy(patch_hat)
    hat6.translate(4.5, 1.5 * r)
    hat6.rotate(-120)
    
    hat7 = copy.deepcopy(patch_hat)
    hat7.translate(4.5, -1.5 * r)
    hat7.rotate(120)
    
    hat8 = copy.deepcopy(patch_hat)
    hat8.rotate(180)

# Construct the SVG, using a group to position the hats properly and flip the Y axis
dwg = svgwrite.Drawing(profile='tiny')
dwg.viewbox(0, 0, 2000, 2000)

g = dwg.g()
g.add(hat)
if patch:
    g.add(hat2)
    g.add(hat3)
    g.add(hat4)
    g.add(hat5)
    g.add(hat6)
    g.add(hat7)
    g.add(hat8)
g.translate(800, 1000)
g.scale(scale, -scale)

dwg.add(g)
dwg.saveas('monotile.svg')
