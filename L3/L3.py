import math
import numpy as np
import chebyshev as c


def exp_func(x):
    return math.e**(x**2)


def abs_func(x):
    return abs(x+x**3)


def sign_func(x):
    return np.sign(x)


def zad1():
    c.draw_plots(exp_func, "y = exp((x**2), <-1,1>")
    # c.draw_plots(abs_func, "y = abs(x+x**3), <-1,1>")
    # c.draw_plots(sign_func, "y = sign(x), <-1,1>")


def main():
    zad1()


if __name__ == "__main__":
    main()
