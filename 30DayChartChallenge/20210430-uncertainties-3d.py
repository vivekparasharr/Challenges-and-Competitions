
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
#!/usr/bin/env python3
from re import X
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Taubin
def Taubin_heart_3d(x,y,z):
   return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3
# Kuska
def Kuska_heart_3d(x,y,z):
   return ((2*(x**2) + y**2 + z**2 - 1)**3 - ((x**2)*(z**3))/10 - ((y**2)*(z**3)))
# Nordstrand
def Nordstrand_heart_3d(x,y,z):
   return ( (32/9)*(x**2) + 2*(y**2) + z**2 - 1 )**3 - (8/45)*(x**2)*(z**3) - (y**2)*(z**3) 


def plot_implicit(fn, fig, sub_plot, color, resolution, slices, elevation, azimuth, bbox=(-1.5, 1.5)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    #fig = plt.figure()
    ax = fig.add_subplot(sub_plot, projection='3d')
    A = np.linspace(xmin, xmax, resolution) # resolution of the contour
    B = np.linspace(xmin, xmax, slices) # number of slices
    A1, A2 = np.meshgrid(A, A) # grid on which the contour is plotted

    for z in B: # plot contours in the XY plane
        X, Y = A1, A2
        Z = fn(X, Y, z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z', colors=(color,))
        # [z] defines the only level to plot
        # for this contour for this value of z

    for y in B:  # plot contours in the XZ plane
        X, Z = A1, A2
        Y = fn(X, y, Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y', colors=(color,))

    for x in B: # plot contours in the YZ plane
        Y, Z = A1, A2
        X = fn(x, Y, Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors=(color,))

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
    # elevation of 60 degrees (that is, 60 degrees above the x-y plane) and an 
    # azimuth of 35 degrees (that is, rotated 35 degrees counter-clockwise about the z-axis)
    ax.view_init(elevation, azimuth) 
    #plt.show()

fig = plt.figure(figsize=[12.8, 9.6])
#fig, ax = plt.subplots(2,2)
fig.suptitle('Plotting Heart Surface on a 3-Dimentional Axes', fontsize=26, color='dimgray')
fig.text(0.35, 0.05, '#30DayChartChallenge - 2021/04/30 | uncertainties | 3-dimensional', style = 'italic', fontsize = 10, color = "dimgray") 
fig.text(0.35, 0.03, 'Plotting 3 variable implicit equations', style = 'italic', fontsize = 10, color = "dimgray") 
fig.text(0.35, 0.01, 'twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com', style = 'italic', fontsize = 10, color = "dimgray") 

fig.text(0.15, 0.87, "Taubin's heart surface equation (filled)", style = 'normal', fontsize = 16, color = "dimgray") 
fig.text(0.15, 0.84, "(x^2+(9/4)*y^2+z^2-1)^3-x^2*z^3-(9/80)*y^2*z^3", style = 'normal', fontsize = 12, color = "slategray") 
plot_implicit(Taubin_heart_3d, fig, 221, 'crimson', 100, 40, 20, 70) # Taubin
fig.text(0.55, 0.87, "Taubin's heart surface equation (mesh)", style = 'normal', fontsize = 16, color = "dimgray") 
fig.text(0.55, 0.84, "(x^2+(9/4)*y^2+z^2-1)^3-x^2*z^3-(9/80)*y^2*z^3", style = 'normal', fontsize = 12, color = "slategray") 
plot_implicit(Taubin_heart_3d, fig, 222, 'red', 50, 20, 20, 70)
fig.text(0.15, 0.47, "Kuska's heart surface equation", style = 'normal', fontsize = 16, color = "dimgray") 
fig.text(0.15, 0.44, "((2*(x^2)+y^2+z^2-1)^3-((x^2)*(z^3))/10-((y^2)*(z^3)))", style = 'normal', fontsize = 12, color = "slategray") 
plot_implicit(Kuska_heart_3d, fig, 223, 'darkorchid', 50, 20, 20, 20)
fig.text(0.55, 0.47, "Nordstrand's heart surface equation", style = 'normal', fontsize = 16, color = "dimgray") 
fig.text(0.55, 0.44, "((32/9)*(x^2)+2*(y^2)+z^2-1)^3-(8/45)*(x^2)*(z^3)-(y^2)*(z^3)", style = 'normal', fontsize = 12, color = "slategray") 
plot_implicit(Nordstrand_heart_3d, fig, 224, 'fuchsia', 50, 20, 20, 15)
plt.savefig('Charts/2021-04-30.png', dpi=300, facecolor='w')
plt.show()


