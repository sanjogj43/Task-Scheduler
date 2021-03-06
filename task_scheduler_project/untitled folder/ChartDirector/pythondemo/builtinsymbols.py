#!/usr/bin/python
from pychartdir import *

# Some ChartDirector built-in symbols
symbols = [CircleShape, GlassSphereShape, GlassSphere2Shape, SolidSphereShape,
    SquareShape, DiamondShape, TriangleShape, RightTriangleShape, LeftTriangleShape,
    InvertedTriangleShape, StarShape(3), StarShape(4), StarShape(5), StarShape(6),
    StarShape(7), StarShape(8), StarShape(9), StarShape(10), PolygonShape(5),
    Polygon2Shape(5), PolygonShape(6), Polygon2Shape(6), CrossShape(0.1), CrossShape(
    0.2), CrossShape(0.3), CrossShape(0.4), CrossShape(0.5), CrossShape(0.6),
    CrossShape(0.7), Cross2Shape(0.1), Cross2Shape(0.2), Cross2Shape(0.3),
    Cross2Shape(0.4), Cross2Shape(0.5), Cross2Shape(0.6), Cross2Shape(0.7)]

# Create a XYChart object of size 450 x 400 pixels
c = XYChart(450, 400)

# Set the plotarea at (55, 40) and of size 350 x 300 pixels, with a light grey border
# (0xc0c0c0). Turn on both horizontal and vertical grid lines with light grey color
# (0xc0c0c0)
c.setPlotArea(55, 40, 350, 300, -1, -1, 0xc0c0c0, 0xc0c0c0, -1)

# Add a title to the chart using 18 pts Times Bold Itatic font.
c.addTitle("Built-in Symbols", "timesbi.ttf", 18)

# Set the axes line width to 3 pixels
c.xAxis().setWidth(3)
c.yAxis().setWidth(3)

# Ensure the ticks are at least 1 unit part (integer ticks)
c.xAxis().setMinTickInc(1)
c.yAxis().setMinTickInc(1)

# Add each symbol as a separate scatter layer.
for i in range(0, len(symbols)) :
    c.addScatterLayer([i % 6 + 1], [int(i / 6 + 1)], "", symbols[i], 15)

# Output the chart
c.makeChart("builtinsymbols.png")

