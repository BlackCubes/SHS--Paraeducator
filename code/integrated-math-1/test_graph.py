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

line1, = ax.plot(x, 2 - x, "-g", label="x + y = 2")
ax.plot(2, 0, color="#FFA000", marker="o", markersize=10)
ax.plot(0, 2, color="#FFA000", marker="o", markersize=10)

line2, = ax.plot(x, 4*x - 8, "-c", label="4x - y = 8")
ax.plot(2, 0, color="#EC407A", marker="o", markersize=5)
ax.plot(0, -8, color="#EC407A", marker="o", markersize=5)

line1_legend = plt.legend(handles=[line1], loc="lower right")
ax = plt.gca().add_artist(line1_legend)
plt.legend(handles=[line2], loc="upper right")
plt.annotate("From (21) in Substitution Method section", xy=(2, 0), xytext=(4, 2), arrowprops=dict(facecolor="black", shrink=0.05),)

# plt.legend()
plt.xlim(-9, 9)
plt.ylim(-9, 9)
plt.grid(True)

plt.show()