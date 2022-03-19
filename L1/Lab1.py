from numpy import double, single, finfo
import matplotlib.pyplot as plt


def calculate_series_float(n: int):
    if n == 0:
        return single(0.01)
    previous_n = calculate_series_float(n - 1)
    a = single(1.0 - previous_n)
    b = single(previous_n * a)
    c = single(3.0 * b)

    return single(previous_n + c)


def calculate_series_double(n: int):
    if n == 0:
        return double(0.01)
    previous_n = calculate_series_double(n - 1)
    a = double(1.0 - previous_n)
    b = double(previous_n * a)
    c = double(3.0 * b)

    return double(previous_n + c)


def calculate_series_float_v2(n: int):
    if n == 0:
        return single(0.01)
    previous_n = calculate_series_float_v2(n - 1)
    a = single(3.0 * previous_n * previous_n)
    b = single(4.0 * previous_n)

    return single(b - a)


def calculate_series_double_v2(n: int):
    if n == 0:
        return double(0.01)
    previous_n = calculate_series_double_v2(n - 1)
    a = double(3.0 * previous_n * previous_n)
    b = double(4.0 * previous_n)

    return double(b - a)


def calculate_results(n: int, precision: str):
    if precision == 'float':
        return [calculate_series_float(i) for i in range(n + 1)]
    if precision == 'double':
        return [calculate_series_double(i) for i in range(n + 1)]
    if precision == 'float_v2':
        return [calculate_series_float_v2(i) for i in range(n + 1)]
    if precision == 'double_v2':
        return [calculate_series_double_v2(i) for i in range(n + 1)]
    else:
        return "Wrong precision setting"


def print_chart(n: int):
    float_result = calculate_results(n, 'float')
    double_result = calculate_results(n, 'double')
    float_v2_result = calculate_results(n, 'float_v2')
    double_v2_result = calculate_results(n, 'double_v2')
    x_axis = [i for i in range(n + 1)]
    x_ticks = [i for i in range(0, n + 1, 5)]
    plt.figure(figsize=(9, 5))
    # plt.plot(x_axis, float_result, label="float")
    plt.plot(x_axis, double_result, label="double")
    # plt.plot(x_axis, float_v2_result, label="float_v2")
    plt.plot(x_axis, double_v2_result, label="double_v2")
    plt.title('Kolejne wartości wyrazów ciągu: x{n+1} = 4.0 * x{n} - 3.0 * x{n} * x{n}')
    # plt.title('Kolejne wartości wyrazów ciągu: x{n+1}= x{n} + 3.0 * x{n} * (1 - x{n})')
    plt.xlabel('n')
    plt.xticks(x_ticks)
    plt.legend()
    plt.show()


def find_epsilon():
    epsilon = double(1.0)
    while (epsilon * 0.5) + 1.0 > 1.0:
        epsilon *= 0.5
    print(f"Maszynowe epsilon: {epsilon}")


if __name__ == '__main__':
    # print_chart(100)
    find_epsilon()
