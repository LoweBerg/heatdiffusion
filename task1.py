import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import matplotlib.animation as animation

fig, ax = plt.subplots()

ylim = 0.5
alfa = 1

def u(x, t):
    return 0.5*(erf((ylim-x)/np.sqrt(4*alfa*t))-erf((-ylim-x)/np.sqrt(4*alfa*t)))


time = np.linspace(0.001,1,100)
X = np.linspace(-4, 4, 1000)
Y = u(X, 0.001)

line2 = ax.plot(X, Y)[0]

def update(frame):
    Y_ = u(X, time[frame])
    line2.set_ydata(Y_)
    ax.set_title(f"Temperature at t = {time[frame]:.4f} unit time")
    return line2

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(time), interval=1)
ax.set_xlabel("x")
ax.set_ylabel("u(x)")
plt.show()
