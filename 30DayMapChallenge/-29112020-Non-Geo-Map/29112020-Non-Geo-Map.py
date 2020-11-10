	
# http://www.mit.edu/~iancross/python/maps.html
import maps
nlat, nlon = 60, 30
phi, theta = maps.makegrid(nlat, nlon)
# Make a small spot centered near, but not at, the equator:
equator_spot = maps.makespot(0, 0, 0.4, phi, theta)
# Make a larger spot centered near, but not at, the pole:
pole_spot = maps.makespot(1.2, 0, 0.7, phi, theta)

