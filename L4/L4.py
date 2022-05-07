import math


def f1(x: float) -> float:
    return x * x


def f2(x: float) -> float:
    return 1 / math.sqrt(x)


def calculate_integral(f, a, b, n):
    dx = (b - a) / n
    integral = 0

    for i in range(1, n+1):
        i = i * dx + a
        integral += dx * f(i)

    print(f"Result for {n} intervals: {integral} \n")
    return integral


def main():
    print("x^2:")
    calculate_integral(f1, 0, 1, 1000)

    print("1/sqrt(x):")
    calculate_integral(f2, 0, 1, 1000)


if __name__ == "__main__":
    main()
