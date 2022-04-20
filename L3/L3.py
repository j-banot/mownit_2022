import math
import numpy as np
import numpy.polynomial.chebyshev as c
import matplotlib.pyplot as plt


def exp_func(x):
    return math.exp(x**2)


def abs_func(x):
    return math.fabs(x)


def sign_func(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    else:
        return -1


def zad1_1():
    x = np.arange(-1, 1, 0.1)
    y = [exp_func(i) for i in np.arange(-1, 1, 0.1)]
    # results = c.chebfit(x, y, 19)
    print(len(x))
    plt.plot(x, y)
    plt.show()


def main():
    zad1_1()


if __name__ == "__main__":
    main()
