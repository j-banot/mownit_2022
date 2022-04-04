import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import barycentric_interpolate, CubicSpline, Akima1DInterpolator


def fun(x: float):
    return x + np.cos(x * x)


def main():
    a = 1.0
    b = 10.0
    steps = 10
    x_observed = [None] * 10
    y_observed = [None] * 10

    dx = (b-a) / steps

    for i in range(0, steps):
        x_observed[i] = a + i * dx + 0.5 * np.sin(i * dx)
        y_observed[i] = fun(x_observed[i])

    x = np.linspace(min(x_observed), max(x_observed), num=100)
    x_cubic = np.arange(0, 10)
    y_barycentric = barycentric_interpolate(x_observed, y_observed, x)
    y_cubic = CubicSpline(x_observed, y_observed)
    y_akima = Akima1DInterpolator(x_observed, y_observed)
    print(y_cubic)
    plt.plot(x_observed, y_observed, 'ro', label="Values")
    plt.plot(x, y_barycentric, label="Barycentric Interpolation")
    plt.plot(x_cubic, y_cubic(x_cubic), label="Cubic Interpolation")
    plt.plot(x, y_akima(x), label="Akima Interpolation")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
