import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import barycentric_interpolate, CubicSpline, Akima1DInterpolator


def fun(x: float):
    return x + np.cos(x * x)


def zad1():
    a = 1.0
    b = 10.0
    steps = 10
    x_observed = [None] * 10
    y_observed = [None] * 10

    dx = (b - a) / steps

    for i in range(0, steps):
        x_observed[i] = a + i * dx + 0.5 * np.sin(i * dx)
        y_observed[i] = fun(x_observed[i])

    x = np.linspace(min(x_observed), max(x_observed), num=100)
    y_barycentric = barycentric_interpolate(x_observed, y_observed, x)
    x_cubic = np.arange(0, 10)
    y_cubic = CubicSpline(x_observed, y_observed)
    y_akima = Akima1DInterpolator(x_observed, y_observed)
    plt.plot(x_observed, y_observed, 'ro', label="Values")
    plt.plot(x, y_barycentric, label="Barycentric Interpolation")
    plt.plot(x_cubic, y_cubic(x_cubic), label="Cubic Interpolation")
    plt.plot(x, y_akima(x), label="Akima Interpolation")
    plt.grid()
    plt.legend()
    plt.show()


def read_from_file(list_x, list_y, file_name):
    with open(file_name) as tmp:
        for line in tmp:
            list = line.split(";")
            list_x.append(float(list[0]))
            list_y.append(float(list[1]))


def zad2():
    list_x = []
    list_y = []
    read_from_file(list_x, list_y, "dane1.txt")
    plt.xscale("log")
    plt.plot(list_x, list_y, label="dane1.dat")
    plt.legend()
    plt.show()


def main():
    # zad1()
    zad2()


if __name__ == "__main__":
    main()
