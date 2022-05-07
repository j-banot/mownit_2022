import math


def f1(x: float) -> float:
    return x * x


def f2(x: float) -> float:
    return 1 / math.sqrt(x)


def calculate_integral(f, a, b, n):
    dx = (b - a) / n
    sum1 = 0

    for i in range(1, n+1):
        x = a + 1 * dx
        sum1 += f(x)

    result = dx * sum1
    print(f"Result for {n} intervals: {result} \n")


def main():
    print("x^2:")
    calculate_integral(f1, 0, 1, 501)

    print("1/sqrt(x):")
    calculate_integral(f2, 0, 1, 501)


if __name__ == "__main__":
    main()
