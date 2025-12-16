import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import matplotlib.animation as animation

fig, ax = plt.subplots()

#parameters
r_0x = 17.5
r_0y = 37.5
r_lim = 3
u_0 = 100
alfa = 2

def u(x, y, t):
    r = np.sqrt((x - r_0x) ** (2) + (y - r_0y) ** 2)
    return (1/2)*u_0*(special.erf((r_lim - r)/(np.sqrt(4*alfa*t))) - special.erf((-r_lim - r)/(np.sqrt(4*alfa*t))))

grid = np.meshgrid(np.linspace(0, 50, 200), np.linspace(0, 50, 200))
data = u(grid[0], grid[1], 0)
T = np.linspace(0.001, 5, 100)

im = ax.imshow(data, cmap = "jet", origin = "lower")
def update(frame):
    data_ = u(grid[0], grid[1], T[frame])
    im.set_data(data_)
    ax.set_title(f"Temperature at time t={T[frame]:.3f} unit time")
    return im

ax.set_xlabel("x")
ax.set_ylabel("y")
fig.colorbar(im, ax=ax)


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(T), interval=10)
plt.show()