import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import matplotlib.animation as animation

fig, ax = plt.subplots()

r0x = 4440e3
r0y = 4440e3
rlim = 4000
u0 = 1000000
spery = 31536000
tend = 1000e6

a = 1e-17

def gen_r(x, y):
    return np.sqrt((x-r0x)**2 + (y-r0y)**2)


def u(r_, t, alfa_):
    return 0.5*u0*(erf((rlim - r_) / np.sqrt(4 * alfa_ * t)) - erf((-rlim - r_) / np.sqrt(4 * alfa_ * t))) * np.exp(-a*t)


# initialize system
res = 300
interval = np.linspace(0, 8000e3, res)
Grid = np.meshgrid(interval, interval)
R = np.sqrt(Grid[0]**2 + Grid[1]**2)
alfa = np.zeros((res, res))
Temp = np.zeros((res, res))
layers = [6300e3, 6178e3, 3478e3, 1278e3]
alfa_l = [1e-5, 8e-6, 23e-7, 11e-5]
temp_l = [293, 3000, 4000, 6000]

for i in range(len(layers)):
    alfa[R <= layers[i]] = alfa_l[i]
    Temp[R <= layers[i]] = temp_l[i]

r = gen_r(Grid[0], Grid[1])
Data = Temp + u(r, 0, alfa)
time = np.linspace(0.001, tend*spery,200)


mask_data = np.ma.masked_where(Data <= 0, Data)
cmap = plt.get_cmap('jet')
cmap.set_bad('black', 1)


# create initial image
im = ax.imshow(mask_data, cmap=cmap, origin="lower", interpolation="hamming", extent=(0, 8e6, 0, 8e6), vmax=10000)

ax.set_xlabel(r"$x$ [m]")
ax.set_ylabel(r"$y$ [m]")
fig.colorbar(im, ax=ax)

def update(frame):
    Data_ = Temp + u(r, time[frame], alfa)
    mask_data_ = np.ma.masked_where(Data_ <= 0, Data_)
    im.set_data(mask_data_)
    ax.set_title(fr"Temperature at time t={time[frame]/spery/1e6:.3f} million years")
    return im


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(time), interval=0.0001)

#ani.save("CometFlowey.gif", fps=60)

plt.show()
