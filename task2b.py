import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import matplotlib.animation as animation

fig, ax = plt.subplots()

r0x = 4340
r0y = 4340
rlim = 150
u0 = 10000
spery = 31536000
tend = 500e6

def gen_r(x, y):
    return np.sqrt((x-r0x)**2 + (y-r0y)**2)



def u(r_, t, alfa_):
    return 0.5*u0*(erf((rlim - r_) / np.sqrt(4 * alfa_ * t)) - erf((-rlim - r_) / np.sqrt(4 * alfa_ * t)))


# initialize system
res = 200
interval = np.linspace(0, 8000, res)
Grid = np.meshgrid(interval, interval)
R = np.sqrt(Grid[0]**2 + Grid[1]**2)
alfa = np.zeros((res, res))
Temp = np.zeros((res, res))
layers = [6300, 6178, 3478, 1278]
alfa_l = [1e-11, 3e-12, 23e-12, 1e-11]
temp_l = [293, 3000, 4000, 6000]

for i in range(len(layers)):
    alfa[R <= layers[i]] = alfa_l[i]
    Temp[R <= layers[i]] = temp_l[i]

r = gen_r(Grid[0], Grid[1])
Data = Temp + u(r, 0, alfa)
time = np.linspace(0.001, tend*spery,100)

# create initial image
im = ax.imshow(Data, cmap="jet", origin="lower", interpolation="spline16")

ax.set_xlabel("x")
ax.set_ylabel("y")
fig.colorbar(im, ax=ax)

def update(frame):
    Data_ = Temp + u(r, time[frame], alfa)
    im.set_data(Data_)
    ax.set_title(f"Temperature at time t={time[frame]/spery/1e6:.3f} million years")
    return im


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(time), interval=1e-3)
plt.show()
