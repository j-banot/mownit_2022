import random

import numpy as np
import matplotlib.pyplot as plt


def hit_and_miss(func, n):
    hits = 0
    misses = 0
    xH = []
    yH = []
    xM = []
    yM = []

    for i in range(n):
        xx = np.random.uniform()
        yy = np.random.uniform()
        if yy <= func(xx):
            hits += 1
            xH = xH + [xx]
            yH = yH + [yy]
        else:
            misses += 1
            xM = xM + [xx]
            yM = yM + [yy]
    intEst = hits / n
    # print('The Hit & Miss estimate of the integral of f(x) on 0 < x < 1 is', intEst)
    diff = 0.33 - intEst
    # print(f"n = {n}, difference = {diff}")
    return diff


def monte_carlo(func, a, b, n):
    random_nums = np.random.uniform(a, b, n)
    integral = 0.0
    for i in range(n):
        integral += func(random_nums[i])
    return (b - a)/float(n) * integral


def main():
    def func1(x):
        return 1 / np.sqrt(x)

    def func2(x):
        return x * x

    print("f(x) = x^2")
    # hit_and_miss(func1, 1000)
    # print("\n")
    # print("f(x) = x^2")

    diff_array = []
    answer = 0
    for i in range(1, 5000):
        answer = monte_carlo(func2, 0, 1, 5000)
        diff_array.append(0.33 - answer)

    print(f"Integral from 0 to 1 of f(x): {answer}")
    print("Number of calls: 5000")

    x = list(range(1, 5000))
    plt.plot(x, diff_array, "ro", label="difference")
    plt.title("f(x) = x^2")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
