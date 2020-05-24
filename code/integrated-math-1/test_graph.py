from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)
    
for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)
    
x = np.arange(-10, 10)
ax.plot(x, 2 - x, '-g')
ax.plot(x, 4*x - 8, '-c')
ax.plot(2, 0, 'om')

plt.legend(['x + y = 2', '4x - y = 8'])
plt.xlim(-9, 9)
plt.ylim(-9, 9)
plt.grid(True)

plt.show()