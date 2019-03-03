import random
import math
import time
import json


def ex1():
    i = -1
    done = False
    while not done:
        number = 10 ** i
        if 1 + number == 1:
            done = True
        i = i - 1
    return number * 10


print("Numarul u: {}\n".format(ex1()))


def ex2():
    x = 1.0
    u = ex1()
    y = u
    z = u
    left_hand = (x + y) + z
    right_hand = x + (y + z)
    print("Adunarea asociativa: {}".format(left_hand == right_hand))

    left_hand = (x * y) * z
    right_hand = x * (y * z)
    while left_hand == right_hand:
        x = random.random()
        left_hand = (x * y) * z
        right_hand = x * (y * z)
        print("Inmultirea asociativa: {} pentru x={}".format(left_hand == right_hand, x))


ex2()
print("\n")


def calculate_constants():
    c1 = 1 / math.factorial(3)
    c2 = 1 / math.factorial(5)
    c3 = 1 / math.factorial(7)
    c4 = 1 / math.factorial(9)
    c5 = 1 / math.factorial(11)
    c6 = 1 / math.factorial(13)
    return c1, c2, c3, c4, c5, c6


def polynomial_1(x, y, c):
    return x * (1 + y * (-c[0] + c[1] * y))


def polynomial_2(x, y, c):
    return x * (1 + y * (-c[0] + y * (c[1] - c[2] * y)))


def polynomial_3(x, y, c):
    return x * (1 + y * (-c[0] + y * (c[1] + y * (- c[2] + c[3] * y))))


def polynomial_4(x, y, c):
    return x * (1 + y * (-0.166 + y * (0.00833 + y * (- c[2] + c[3] * y))))


def polynomial_5(x, y, c):
    return x * (1 + y * (-c[0] + y * (c[1] + y * (- c[2] + y * (c[3] - c[4] * y)))))


def polynomial_6(x, y, c):
    return x * (1 + y * (-c[0] + y * (c[1] + y * (- c[2] + y * (c[3] + y * (- c[4] + c[5] * y))))))


def ex3():
    c = calculate_constants()
    functions = [polynomial_1, polynomial_2, polynomial_3, polynomial_4, polynomial_5, polynomial_6]
    times = dict()
    errors = dict()
    best_polynomials = dict()
    for i in range(0, 100000):
        x = random.uniform(-(math.pi / 2), math.pi / 2)
        y = x * x
        local_errors = dict()
        for index, function in enumerate(functions):
            startTime = time.time()
            approximation = function(x, y, c)
            runningTime = time.time() - startTime
            times[index + 1] = times.get(index + 1, 0) + runningTime
            result = math.sin(x)
            error = math.fabs(result - approximation)
            local_errors[index + 1] = error
            errors[index + 1] = errors.get(index + 1, 0) + error

        sorted_list = sorted(local_errors.items(), key=lambda x: x[1])
        best_polynomials[x] = sorted_list[0:3]
    for key in range(1, 7):
        errors[key] = errors[key] / 100000
        times[key] = times[key] / 100000
    sorted_list_accuracy = sorted(errors.items(), key=lambda x: x[1])
    sorted_list_time = sorted(times.items(), key=lambda x: x[1])

    best = dict.fromkeys([1, 2, 3, 4, 5, 6], 0)
    for three_polynomials in best_polynomials.values():
        for (value, error) in three_polynomials:
            best[value] = best.get(value, 0) + 1
    sorted_list_apparitions = sorted(best.items(), key=lambda x: x[1], reverse=True)

    print("Polinoamele sortate dupa aparitii in top 3: ")
    for index, (polynomial, apparitions) in enumerate(sorted_list_apparitions):
        print("{}.Polinomul P{} Aparitii: {}".format(index + 1, polynomial, apparitions))

    print("\nPolinoamele sortate dupa eroarea medie: ")
    for index, (polynomial, averageError) in enumerate(sorted_list_accuracy):
        print("{}.Polinomul P{} Eroare: {}".format(index + 1, polynomial, averageError))

    print("\nPolinoamele sortate dupa timp: ")
    for index, (polynomial, averageTime) in enumerate(sorted_list_time):
        print("{}.Polinomul P{} Timp: {}".format(index + 1, polynomial, averageTime))

    file = open("results.json", "w")
    json.dump(best_polynomials, file)
    file.close()


ex3()
