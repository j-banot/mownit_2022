import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import barycentric_interpolate


def fun(x: float):
    return x + np.cos(x * x)


def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)


def main():
    a = 1.0
    b = 10.0
    steps = 10
    x_observed = [None] * 10
    y_observed = [None] * 10

    # input = open("wartosci.txt", "w")
    # output = open("inter.txt", "w")

    dx = (b-a) / steps

    for i in range(0, steps):
        x_observed[i] = a + i * dx + 0.5 * np.sin(i * dx)
        y_observed[i] = fun(x_observed[i])
        # fprintf(input, "%g %g\n", x_observed[i], y_observed[i])

    x = np.linspace(min(x_observed), max(x_observed), num=100)
    y = barycentric_interpolate(x_observed, y_observed, x)
    plt.plot(x, y, label="barycentric interpolation")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
