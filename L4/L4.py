import math
from scipy import integrate


def f1(x: float) -> float:
    return x * x


def f2(x: float) -> float:
    return 1 / math.sqrt(x)


def calculate_integral(f, a, b, n):
    dx = (b - a) / n
    integral = 0

    for i in range(1, n + 1):
        i = i * dx + a
        integral += dx * f(i)

    # print(f"Result for {n} intervals: {integral} \n")
    return integral


def analyze_integral(f, a, b, expected):
    results = []
    for i in range(3, 7):
        limit = pow(10, (-i))
        inter = 1
        running = True
        while running:
            result = calculate_integral(f, a, b, inter)
            error = abs(result - expected)
            running = error >= limit
            if not running:
                results.append((result, error, limit, inter))
                print(f"Result: {result} error: {error}, expected: {expected}, Limit: {limit} Interwals: {inter} \n")
            inter += 1
    return result


def main():
    # print("x^2:")
    # calculate_integral(f1, 0, 1, 1000)
    #
    # print("1/sqrt(x):")
    # calculate_integral(f2, 0, 1, 1000)
    analyze_integral(f2, 0, 1, 1 / 3.0)


if __name__ == "__main__":
    main()
