import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import FancyArrowPatch
from scipy.interpolate import barycentric_interpolate, CubicSpline, Akima1DInterpolator
from mpl_toolkits.mplot3d import Axes3D, proj3d


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


def read_from_file1(list_x, list_y, file_name):
    with open(file_name) as tmp:
        for line in tmp:
            tmp_list = line.split(";")
            list_x.append(float(tmp_list[0]))
            list_y.append(float(tmp_list[1]))


def zad2():
    list_x = []
    list_y = []
    read_from_file1(list_x, list_y, "dane1.txt")
    plt.xscale("log")
    plt.plot(list_x, list_y, label="dane1.dat")
    plt.legend()
    plt.show()


def read_from_file2(list_x, list_y, list_z, file_name):
    with open(file_name) as tmp:
        for line in tmp:
            tmp_list = line.split(";")
            list_x.append(float(tmp_list[0]))
            list_y.append(float(tmp_list[1]))
            list_z.append(float(tmp_list[2]))


def zad3():
    list_x = []
    list_y = []
    list_z = []
    read_from_file2(list_x, list_y, list_z, "dane2.txt")
    list_x = np.reshape(list_x, (-1, 2))
    list_y = np.reshape(list_y, (-1, 2))
    list_z = np.reshape(list_z, (-1, 2))
    ax = plt.axes(projection='3d')
    ax.contour3D(list_x, list_y, list_z, 1000, cmap=cm.cool)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    a = Arrow3D([2, 3], [2, 5], [0.75, 0.75],
                mutation_scale=30,
                lw=4, arrowstyle="-|>", color="g")
    ax.add_artist(a)
    plt.show()


def zad4():
    list_x = []
    list_y = []
    list_z = []
    read_from_file2(list_x, list_y, list_z, "fun1.txt")
    x = np.arange(-3, 3, 0.1)
    y_fun2 = np.sin(x ** 5)
    y_fun1 = np.cos(x * np.sin(x))
    y_fun3 = 3 * np.sin(x)
    plt.bar(x, y_fun1, align='center', width=0.1, edgecolor="red", color="none",
            label="funkcja 1: 2*cos(x*sin(x))")
    plt.plot(x, y_fun2, label="funkcja 2: sin(x^5)")
    plt.plot(x, y_fun3, color="green", label="funkcja 3: 3*sin(x)")
    plt.plot(list_x, list_y, "g_")
    plt.plot(list_x, list_z, "g_")
    plt.vlines(list_x, list_y, list_z, color="green", label="Dane z pliku fun1.txt")
    plt.title("Wykres Testowy")
    plt.ylabel("Amplituda")
    plt.legend()
    plt.grid()
    plt.show()


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))

        return np.min(zs)


def fun(x: float):
    return x + np.cos(x * x)


def main():
    # zad1()
    # zad2()
    # zad3()
    zad4()


if __name__ == "__main__":
    main()
