import random


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


def read_input1():
    with open("input1.txt", "r") as f:
        x = [int(i) for i in f.readline().split()]
        y = [int(i) for i in f.readline().split()]
        x_bar = float(f.readline())
        result = float(f.readline())
    return x, y, x_bar, result


def func_input2(x):
    return x * x * x + 3 * x * x - 5 * x + 12


# input 1
print("Exemplu 1")
x, y, x_bar, f_bar = read_input1()
Ln = compute_Ln(x, y, len(x) - 1, x_bar)
print("Ln(x_bar) = ", Ln)
print("|Ln(x_bar) - f(x_bar)| = ", abs(Ln - f_bar))

print("\n")
# input 2
print("Exemplu 2")
n = 5
x = []
y = []
for i in range(n):
    x += [random.uniform(1, 5)]
    y += [func_input2(x[i])]
x_bar = random.uniform(1, 5)
while x_bar in x:
    x_bar = random.uniform(1, 5)
f_bar = func_input2(x_bar)
print("x_bar = ", x_bar)
Ln = compute_Ln(x, y, len(x) - 1, x_bar)
print("Ln(x_bar) = ", Ln)
print("|Ln(x_bar) - f(x_bar)| = ", abs(Ln - f_bar))
