from numpy import double, single
import matplotlib.pyplot as plt


def calculate_series_float(n: int):
    if n == 0:
        return single(0.01)
    previous_n = single(calculate_series_float(n - 1))
    a = single(1.0 - previous_n)
    b = single(previous_n * a)
    c = single(3.0 * b)

    return previous_n + c


def calculate_series_double(n: int):
    if n == 0:
        return double(0.01)
    previous_n = double(calculate_series_double(n-1))
    a = double(1.0 - previous_n)
    b = double(previous_n * a)
    c = double(3.0 * b)

    return previous_n + c


def calculate_results(n: int, precision: str):
    if precision == 'float':
        return [calculate_series_float(i) for i in range(n + 1)]
    if precision == 'double':
        return [calculate_series_double(i) for i in range(n + 1)]
    else:
        return "Wrong precision setting"


def print_chart(n: int):
    float_result = calculate_results(n, 'float')
    double_result = calculate_results(n, 'double')
    x_axis = [i for i in range(n + 1)]
    x_ticks = [i for i in range(0, n+1, 5)]

    plt.figure(figsize=(9, 5))
    plt.plot(x_axis, float_result, label="float")
    plt.plot(x_axis, double_result, label="double")
    plt.title('Title')
    plt.xlabel('Values')
    plt.xticks(x_ticks)
    plt.ylabel('n')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print_chart(100)
