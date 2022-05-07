import numpy as np
import matplotlib.pyplot as plt


def draw_plots(function, title):
    x_min = -1
    x_max = 1
    x_grid = np.linspace(x_min, x_max, 100)
    plt.figure()
    plt.plot(x_grid, function(x_grid), label="org")

    Tf_2 = Chebyshev.approximation(x_min, x_max, 2, function)
    Tf_3 = Chebyshev.approximation(x_min, x_max, 3, function)
    Tf_4 = Chebyshev.approximation(x_min, x_max, 4, function)
    Tf_8 = Chebyshev.approximation(x_min, x_max, 8, function)

    plt.plot(x_grid, Tf_2, label="2")
    plt.plot(x_grid, Tf_3, label="3")
    plt.plot(x_grid, Tf_4, label="4")
    plt.plot(x_grid, Tf_8, label="8")

    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
    plt.close()


class Chebyshev:
    """
    Source: https://www.semanticscholar.org/paper/Multi-Core-Parallel-Programming-in-Go-Tang/7679bd13f5987da282b0662a0c41a4d6dd6f2165
    """
    def scale_up(z, x_min, x_max):
        return x_min + (z + 1) * (x_max - x_min) / 2

    def scale_down(x, x_min, x_max):
        return (2 * (x - x_min) / (x_max - x_min)) - 1

    def approximation(x_min, x_max, n, function):
        x_grid = np.linspace(x_min, x_max, 100)
        m = n + 1
        r_k = -np.cos((2 * np.arange(1, m + 1) - 1) * np.pi / (2 * m))

        T = np.zeros((m, n + 1))

        T[:, 0] = np.ones((m, 1)).T

        T[:, 1] = r_k.T

        for i in range(1, n):
            T[:, i + 1] = 2 * r_k * T[:, i] - T[:, i - 1]

        x_k = Chebyshev.scale_up(r_k, x_min, x_max)
        y_k = function(x_k)
        alpha = np.linalg.inv(T.T @ T) @ T.T @ y_k

        T = np.zeros((len(x_grid), n + 1))

        T[:, 0] = np.ones((len(x_grid), 1)).T

        z_grid = Chebyshev.scale_down(x_grid, x_min, x_max)

        T[:, 1] = z_grid.T

        for i in range(1, n):
            T[:, i + 1] = 2 * z_grid * T[:, i] - T[:, i - 1]

        return T @ alpha

