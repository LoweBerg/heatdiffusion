import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

#parameters
r_0x = 4230e3  #position in x
r_0y = 4230e3  #position in y
r_lim = 3e3  #size of comet
u_0 = 1000000  #starting temp
#alfa = 2
width = 200
secs = 31557600
years = 700e6

a = 5e-18   #decaying parameter


x_earth = np.linspace(0, 8000e3, width)
y_earth = np.linspace(0, 8000e3, width)
grid = np.meshgrid(x_earth, y_earth)
R = np.sqrt(grid[0]**2 + grid[1]**2)

Layer = np.array([0, 1000e3, 2000e3, 5000e3, 6000e3, 6200e3])   #creating layers of the earth
alpha_ = np.array([11e-5, 23e-7, 4e-6, 1e-5, 1e-4])
Temp_ = np.array([6000, 3800, 3000, 2000, 0])

alpha = np.zeros((width, width))
Temp = np.zeros((width, width))

for i in range(len(Layer)-1):
    alpha[(R >= Layer[i]) & (R < Layer[i+1])] = alpha_[i]
    Temp[(R >= Layer[i]) & (R < Layer[i+1])] = Temp_[i]

def small_r(x, y):
    r_ = np.sqrt((x-r_0x)**2 + (y-r_0y)**2)
    return r_

def u(r_1, t):  #heatdiffusion equation
    return (1/2)*u_0*(special.erf((r_lim - r_1)/(np.sqrt(4*alpha*t))) - special.erf((-r_lim - r_1)/(np.sqrt(4*alpha*t)))) * np.exp(-a*t)


r = small_r(grid[0], grid[1])
data = u(r, 0)
time = np.linspace(0.01, secs*years, 200)

data = Temp + data

im = ax.imshow(data, cmap = "jet", origin = "lower", interpolation = "hamming", extent=(0, 8e6, 0, 8e6), vmax=10000)
def update(frame):
    data_ = Temp + u(r, time[frame])
    im.set_data(data_)
    ax.set_title(f"Temperature at time t={time[frame]/secs/1e6:.3f} million years")
    return im

ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
fig.colorbar(im, ax=ax)


anim = FuncAnimation(fig=fig, func=update, frames=len(time), interval=0.001)
plt.show()
#anim.save("earth_comet_good_decay.gif", fps = 30, dpi=200)