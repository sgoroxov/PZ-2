import math


def f_linear(x):
    return x


def f_square(x):
    return x * x


def f_cube(x):
    return x ** 3


def f_sin(x):
    return math.sin(x)


def f_exp(x):
    return math.exp(x)


def f_log(x):
    return math.log1p(x)   # log(1+x)


functions = {
    "линейная": f_linear,
    "квадратичная": f_square,
    "кубическая": f_cube,
    "тригонометрическая": f_sin,
    "экспоненциальная": f_exp,
    "логарифмическая": f_log,
}
