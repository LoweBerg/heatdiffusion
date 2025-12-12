import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import matplotlib.animation as animation

fig, ax = plt.subplots()

r0x = 17.5
r0y = 37.5
rlim = 5/2
alfa = 2
u0 = 100

def r(x, y):
    return np.sqrt((x-r0x)**2 + (y-r0y)**2)

def u(r_, t):
    return 0.5*u0*(erf((rlim - r_) / np.sqrt(4 * alfa * t)) - erf((-rlim - r_) / np.sqrt(4 * alfa * t)))


interval = np.linspace(0, 50, 100)

Grid = np.meshgrid(interval, interval)
Data = u(r(Grid[0], Grid[1]), 0)
time = np.linspace(0.001,5,100)

im = ax.imshow(Data, cmap="plasma", origin="lower")

def update(frame):
    Data_ = u(r(Grid[0], Grid[1]), time[frame])
    im.set_data(Data_)
    ax.set_title(f"Temperature at time t={time[frame]:.3f} unit time")
    return im


ax.set_xlabel("x")
ax.set_ylabel("y")
fig.colorbar(im, ax=ax)

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(time), interval=0.001)
plt.show()
