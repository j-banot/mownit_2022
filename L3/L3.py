import math
import numpy as np
import chebyshev as c
import matplotlib.pyplot as plt


def exp_func(x):
    return math.e**(x**2)


def abs_func(x):
    return abs(x+x**3)


def sign_func(x):
    return np.sign(x)


def zad1():
    c.draw_plots(exp_func, "y = exp((x**2), <-1,1>")
    c.draw_plots(abs_func, "y = abs(x+x**3), <-1,1>")
    c.draw_plots(sign_func, "y = sign(x), <-1,1>")


def zad2_func(x):
    return 0.5**(x**2+2*x)


def zad2_approx(x):
    return 1.01691 - 1.37024*x + 0.0835053*x**2 + 0.441443*x**3


def zad2():
    x_min = -1
    x_max = 1
    x_grid = np.linspace(x_min, x_max, 100)
    plt.figure()
    plt.plot(x_grid, zad2_func(x_grid), label="org")
    plt.plot(x_grid, zad2_approx(x_grid), label="średniokwadratowa")
    Tf_3 = c.Chebyshev.approximation(x_min, x_max, 3, zad2_func)
    plt.plot(x_grid, Tf_3, label="liniowa")
    plt.legend()
    plt.grid()
    plt.show()
    plt.close()


def main():
    #zad1()
    zad2()


if __name__ == "__main__":
    main()
