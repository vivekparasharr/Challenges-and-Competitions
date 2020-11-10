
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ax.annotate('test', xy=(0.9, 0.9),
             #xycoords='data',
             xytext=(0, 0),
             #textcoords='data',
             arrowprops=dict(arrowstyle= '<|-|>',
                             color='blue',
                             lw=3.5,
                             ls='--')
           )

ax.set_xlim(-0.1,1)
ax.set_ylim(-0.1,1)
fig.show()

