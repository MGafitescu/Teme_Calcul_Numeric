import random
import math

epsilon = 10 ** -10
h = 10 ** -5


def steffensen(f):
    x = random.randrange(-4, 4)
    k = 0
    kmax = 100
    delta_x = 1
    while epsilon <= delta_x <= 10 ** 8 and k <= kmax:
        if math.fabs(g(f, x)) <= epsilon:
            return x
        s_x = (g(f, x + g(f, x)) - g(f, x)) / g(f, x)
        delta_x = g(f, x) / s_x
        x = x - delta_x
        k = k + 1
    if math.fabs(delta_x) < epsilon:
        return x
    else:
        return None


def g(f, x):
    g1 = (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)
    # g2 = (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)
    return g1


def second_derivative(f, x):
    s_d = -f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)
    s_d = s_d / (12 * (h ** 2))
    return s_d


def punct_minim(f):
    punct_critic = steffensen(f)
    k = 0
    while punct_critic is None and k < 1000:
        punct_critic = steffensen(f)
        k = k + 1

    print("Punct critic: {}".format(punct_critic))
    if punct_critic is not None:
        if second_derivative(f, punct_critic) > 0:
            print("Punctul critic este si punct de minim")
        else:
            print("Nu este punct de minim")
    print()


f1 = lambda x: x ** 2 - 4 * x + 3
f2 = lambda x: x ** 2 + math.e ** x
f3 = lambda x: x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4

punct_minim(f1)
punct_minim(f2)
punct_minim(f3)
