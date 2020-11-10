
import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")


u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")
