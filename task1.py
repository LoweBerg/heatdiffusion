import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import matplotlib.animation as animation

fig, ax = plt.subplots()

def u(x, t):
    return (1/2)*(special.erf((1/2 - x)/(np.sqrt(4*t))) - special.erf((-1/2 - x)/(np.sqrt(4*t))))

T = np.linspace(0.001, 1, 100)
X = np.linspace(-3, 3, 300)
Y = u(X, 0.001)


line2 = ax.plot(X, Y)[0]

def update(frame):
    #update the line plot:
    Y_ = u(X, T[frame])
    line2.set_ydata(Y_)
    ax.set_title(f"Temperature at time t={T[frame]:.3f} unit time")
    return line2

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(T), interval=0.035)
plt.show()

