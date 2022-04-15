
# https://www.kdnuggets.com/2019/05/animations-with-matplotlib.html

# Animations using Celluloid Module
from matplotlib import pyplot as plt
from celluloid import Camera
fig = plt.figure()
camera = Camera(fig)
for i in range(10):
    plt.plot([i] * 10)
    camera.snap()
animation = camera.animate()
animation.save('celluloid_minimal.gif', writer = 'imagemagick')


########################################################################


# Subplots
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera
fig, axes = plt.subplots(2)
camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 128, endpoint=False)
for i in t:
    axes[0].plot(t, np.sin(t + i), color='blue')
    axes[1].plot(t, np.sin(t - i), color='blue')
    camera.snap()
animation = camera.animate()  
animation.save('celluloid_subplots.gif', writer = 'imagemagick')


########################################################################


# Legends
import matplotlib
from matplotlib import pyplot as plt
from celluloid import Camera
fig = plt.figure()
camera = Camera(fig)
for i in range(20):
    t = plt.plot(range(i, i + 5))
    plt.legend(t, [f'line {i}'])
    camera.snap()
animation = camera.animate()
animation.save('celluloid_legends.gif', writer = 'imagemagick')


########################################################################


# Basic Animation: Moving Sine Wave 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')
fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)
def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,
anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
anim.save('sine_wave.gif', writer='imagemagick')


########################################################################


# A Growing Coil
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 
plt.style.use('dark_background')
fig = plt.figure() 
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50)) 
line, = ax.plot([], [], lw=2) 
# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 
# lists to store x and y axis points 
xdata, ydata = [], [] 
# animation function 
def animate(i): 
	# t is a parameter 
	t = 0.1*i 
	# x, y values to be plotted 
	x = t*np.sin(t) 
	y = t*np.cos(t) 
	# appending new points to x, y axes points list 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 
	return line, 
# setting a title for the plot 
plt.title('Creating a growing coil with matplotlib!') 
# hiding the axis details 
plt.axis('off') 
# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=500, interval=20, blit=True) 
# save the animation as mp4 video file 
anim.save('coil.gif',writer='imagemagick')


########################################################################


# Live Updating Graphs
#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)
def animate(i):
    data = open('stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    for line in lines:
        x, y = line.split(',') # Delimiter is comma    
        xs.append(float(x))
        ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib')	
ani = animation.FuncAnimation(fig, animate, interval=1000) 
plt.show()


