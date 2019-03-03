import math
import numpy as np

size = 0
precision = 0
A = []


def read_input():
    f = open("input.txt", "r")
    content = f.readlines()
    f.close()
    return content


def parse_input(content):
    global size
    global precision
    size = int(content[0])
    t = int(content[1])
    precision = 10 ** (-t)
    A = []
    del content[0]
    del content[0]
    b = content[-1].split(" ")
    b = [float(x) for x in b]
    del content[-1]
    for line in content:
        matrix_line = []
        columns = line.split(" ")
        for number in columns:
            matrix_line.append(float(number))
        A.append(matrix_line)
    return A, b


def matrix_print(matrix):
    for line in matrix:
        for number in line:
            print(number, end="\t")
        print("")
    print("")


def format_matrix(matrix):
    s = ""
    for line in matrix:
        for number in line:
            s = s + str(number) + "\t"
        s = s + "\n"
    return s


def compute_LU(matrix):
    A = list(matrix)
    Ainit = list(A)
    for p in range(0, size):
        for i in range(0, p + 1):
            sumU = 0
            sumL = 0
            for k in range(0, i):
                sumL = sumL + A[p][k] * A[k][i]
                sumU = sumU + A[i][k] * A[k][p]
            A[p][i] = A[p][i] - sumL
            if i < p:
                if math.fabs(A[i][i]) > precision:
                    A[i][p] = (Ainit[i][p] - sumU) / A[i][i]
                else:
                    print("Nu se poate realiza descompunerea")
    return A


def compute_determinant(A):
    detU = 1.0
    detL = 1.0
    for i in range(0, size):
        detL = detL * A[i][i]
    detA = detL * detU
    return detA


def compute_xLU(A, b):
    x = []
    y = []
    for i in range(0, size):
        x.append(0)
        y.append(0)
    # rezolvam ecuatia Ly = b
    for i in range(0, size):
        if math.fabs(A[i][i]) > precision:
            s = 0;
            for j in range(0, i):
                s = s + A[i][j] * y[j]
            y[i] = (b[i] - s) / A[i][i]
    # rezolvam ecuatia Ux = y
    for i in range(size - 1, -1, -1):
        s = 0
        for j in range(i + 1, size):
            s = s + A[i][j] * x[j]
        x[i] = y[i] - s
    return x


def verify_solution(A, x, b):
    Ax = []
    rez = []
    norma = 0
    for i in range(0, size):
        Ax.append(0)
        rez.append(0)
    for i in range(0, size):
        for j in range(0, size):
            Ax[i] = Ax[i] + A[i][j] * x[j]
    for i in range(0, size):
        rez[i] = Ax[i] - b[i]
    for i in range(0, size):
        norma = norma + rez[i] * rez[i]
    return math.sqrt(norma)


def solve_with_numpy(A, b):
    A = np.array(A)
    b = np.array(b)
    return np.linalg.solve(A, b)


def inverse_with_numpy(A):
    return np.linalg.inv(A)


def norma_1(xLU, xlib):
    rez = []
    for i in range(0, size):
        rez.append(0)
    norma = 0
    for i in range(0, size):
        rez[i] = xLU[i] - xlib[i]
    for i in range(0, size):
        norma = norma + rez[i] * rez[i]
    return math.sqrt(norma)


def norma_2(xLU, A_inverse, b):
    A_inverse_b = []
    rez = []
    norma = 0
    for i in range(0, size):
        A_inverse_b.append(0)
        rez.append(0)
    for i in range(0, size):
        for j in range(0, size):
            A_inverse_b[i] = A_inverse_b[i] + A_inverse[i][j] * b[j]
    for i in range(0, size):
        rez[i] = xLU[i] - A_inverse_b[i]
    for i in range(0, size):
        norma = norma + rez[i] * rez[i]
    return math.sqrt(norma)


def solve():
    content = read_input()
    A, b = parse_input(content)
    print("Matricea: ")
    matrix_print(A)
    print("Termenii liberi: ")
    for term in b:
        print(term, end="\t")
    print("\n")
    A = compute_LU(A)
    print("Descompunerea LU")
    matrix_print(A)
    print("Determinantul  matricii A: {}".format(compute_determinant(A)))
    print("\nSolutia obtinuta prin calcul: ")
    x = compute_xLU(A, b)
    for index, term in enumerate(x):
        print("x{}: {}".format(index, term))
    Ainit, b = parse_input(read_input())
    print("\nNorma AxLU - b: {}".format(verify_solution(Ainit, x, b)))
    print("\nSolutia obtinuta cu numpy: ")
    x_np = solve_with_numpy(Ainit, b)
    for index, term in enumerate(x_np):
        print("x{}: {}".format(index, term))
    print("\nInversa obtinuta cu numpy: ")
    A_inverse = inverse_with_numpy(Ainit)
    matrix_print(A_inverse)
    print("Norma xLU - xlib: {}".format(norma_1(x, x_np)))
    print("\nNorma xLU - A-1*b: {}".format(norma_2(x, A_inverse, b)))


if __name__ == "__main__":
    solve()
