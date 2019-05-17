import random
import numpy as np


def compute_Aitken(x, y, n):
    divided_differences = y
    for k in range(1, n + 1):
        for i in range(n, k - 1, -1):
            divided_differences[i] = (divided_differences[i] - divided_differences[i - 1]) / (x[i] - x[i - k])
    return divided_differences


def compute_Ln(x, y, n, x_bar):
    divided_differences = compute_Aitken(x, y, n)
    print("Diferente divizate =", divided_differences)
    y_bar = y[0]
    prod = 1
    for i in range(1, n + 1):
        prod *= x_bar - x[i - 1]
        y_bar += divided_differences[i] * prod
    return y_bar


def compute_spline(x, y, n, x_bar, a, b, da, db):
    h = [0 for j in range(0, n)]
    for i in range(n ):
        h[i] = x[i + 1] - x[i]
    H = []
    for i in range(0, n):
        H.append([0 for j in range(0, n)])
    print("h=",h)

    H[0][0] = 2 * h[0]
    H[0][1] = h[0]

    for i in range(1, n - 1):
        H[i][i] = 2 * (h[i - 1] + h[i])
        H[i][i - 1] = h[i - 1]
        H[i][i + 1] = h[i]

    H[n - 1][n - 1] = 2 * h[n - 1]
    H[n - 1][n - 2] = h[n - 1]

    f = [0 for j in range(0, n)]
    f[0] = 6 * ((y[1] - y[0]) / h[0] - da)
    print("aaa",y[1]-y[0],h[0],da)
    for i in range(1, n - 1):
        f[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
    f[n - 1] = 6 * (db - (y[n] - y[n-1]) / h[n-1])

    H = np.array(H)
    f = np.array(f)
    print(H)
    print(f)
    A = np.linalg.solve(H, f)

    for i in range(n - 1):
        if x_bar >= x[i] and x_bar <= x[i + 1]:
            b = (y[i + 1] - y[i]) / h[i] - h[i] * (A[i + 1] - A[i]) / 6
            c = (x[i + 1] * y[i] - x[i] * y[i + 1]) / h[i] - (h[i] * (x[i + 1] * A[i] - x[i] * A[i + 1])) / 6
            return (x_bar - x[i]) ** 3 * A[i + 1] / (6 * h[i]) + (
                    (x[i + 1] - x_bar) ** 3 * A[i] / (6 * h[i])) + b * x_bar + c


def read_input1():
    with open("input1.txt", "r") as f:
        x = [int(i) for i in f.readline().split()]
        y = [int(i) for i in f.readline().split()]
        x_bar = float(f.readline())
        result = float(f.readline())
        da = float(f.readline())
        db = float(f.readline())
    return x, y, x_bar, result, da, db


def func_input2(x):
    return x * x * x + 3 * x * x - 5 * x + 12


# input 1
print("Exemplu 1")
x, y, x_bar, f_bar, da, db = read_input1()
y1 = y.copy()
n = len(x) - 1
Ln = compute_Ln(x, y, len(x) - 1, x_bar)
print("Ln(x_bar) = ", Ln)
print("|Ln(x_bar) - f(x_bar)| = ", abs(Ln - f_bar))
Sf = compute_spline(x, y1, n, x_bar, x[0], x[n - 1], da, db)
print("Sf(x_bar = ", Sf)
print("|Sf(x_bar) - f(x_bar)| = ", abs(Sf - f_bar))

print("\n")
# input 2
print("Exemplu 2")
n = 5
x = []
y = []
for i in range(n):
    x += [random.uniform(1, 5)]
    y += [func_input2(x[i])]
x[0]=1
x[4]=5
x_bar = random.uniform(1, 5)
y1 = y.copy()
while x_bar in x:
    x_bar = random.uniform(1, 5)
f_bar = func_input2(x_bar)
print("x_bar = ", x_bar)
Ln = compute_Ln(x, y, len(x) - 1, x_bar)
print("Ln(x_bar) = ", Ln)
print("|Ln(x_bar) - f(x_bar)| = ", abs(Ln - f_bar))
da = 4
db = 100
Sf = compute_spline(x, y1, n-1, x_bar, x[0], x[n - 1], da, db)
print("Sf(x_bar) = ", Sf)
print("|Sf(x_bar) - f(x_bar)| = ", abs(Sf - f_bar))