import numpy as np
import matplotlib.pyplot as plt

class fourier_plot():

    def __init__(self):

        pass
    def f(t):
        return 2*np.sin(t)
    def f2(t):
        return np.sin(t*5) #* np.sin(2*np.pi*t)

    def cart2pol(x, y):
        theta = np.arctan2(y, x)
        rho = np.hypot(x, y)
        return theta, rho

    def pol2cart(theta, rho):
        x = rho * np.cos(theta)
        y = rho * np.sin(theta)
        return x, y

    t1 = np.arange(0.0, 10.0, 0.01)
    t2 = np.arange(0.0, 10.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t2, f(t2), 'k')

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r

    circle_freq=1

    r, theta=cart2pol(t1,f(t1))
    ax = plt.subplot(212, projection='polar')
    ax.plot(theta*(3), r)
    # ax.set_rmax(2)
    ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
    ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
    ax.grid(True)


    plt.show()

if __name__ == __main__:
    p1=fourier_plot()

