import time
import math

size = 0
epsilon = 10 ** -15


def get_matrix(filename, vector):
    global size
    f = open(filename)
    content = f.read()
    f.close()
    lines = content.split("\n")
    del lines[1]
    size = int(lines[0])
    # matrix = dict.fromkeys(list(range(0,size)),{})
    matrix = {}
    for i in range(0, size):
        matrix[i] = {}
    i = 0
    row = lines[i]
    while row != '':
        i = i + 1
        row = lines[i]
        if row != '':
            val, line, col = row.split(",")
            val = float(val)
            line = int(line)
            col = int(col)
            matrix[line][col] = matrix[line].get(col, 0) + val

    if vector is True:
        b = []
        no_of_lines = i
        for i in range(no_of_lines + 1, no_of_lines + size + 1):
            b.append(float(lines[i]))
        return matrix, b
    return matrix


def add_matrixes(A, B):
    result = {}
    for i in range(0, size):
        result[i] = {}
    for i in range(0, size):
        for j in range(0, size):
            if j in A[i].keys():
                if j in B[i].keys():
                    result[i][j] = A[i][j] + B[i][j]
                else:
                    result[i][j] = A[i][j]
            elif j in B[i].keys():
                result[i][j] = B[i][j]
    return result


def normal_matrix_multiply(A, B):
    result = {}
    for i in range(0, size):
        result[i] = {}
    for i in range(0, size):
        for j in range(0, size):
            for k in range(0, size):
                if k in A[i].keys():
                    if j in B[k].keys():
                        result[i][j] = result[i].get(j, 0) + A[i][k] * B[k][j]

    return result


def sparse_matrix_multiply(A, B):
    result = {}
    for i in range(0, size):
        result[i] = {}
    for index, row in enumerate(A.values()):
        for k in range(0, size):
            number = sum([v * B[i].get(k, 0) for (i, v) in row.items()])
            if number != 0:
                result[index][k] = number

    return result


def verify_matrix_equality(A, B):
    for i in range(0, size):
        for j in range(0, size):
            if j in A[i].keys():
                if j in B[i].keys():
                    if math.fabs(A[i][j] - B[i][j]) > epsilon:
                        return False
                else:
                    return False
            elif j in B[i].keys():
                return False
    return True


def mult_matrix_vector(A, x):
    result = []
    for index, row in enumerate(A.values()):
        result.append(sum([v * x[i] for (i, v) in row.items()]))

    return result


def verify_vectors(x, y):
    for i in range(0, size):
        if math.fabs(x[i] - y[i]) > epsilon:
            return False
    return True


def adunare(A, B, AplusB):
    t = time.time()
    add_result = add_matrixes(A, B)
    print("Adding the matrixes: {}".format(time.time() - t))
    print("Adunarea  este egal cu aplusb: {}\n".format(verify_matrix_equality(add_result, AplusB)))


def inmultire(A, B, AoriB):
    t = time.time()
    dot_result = sparse_matrix_multiply(A, B)
    print("Multiplying the matrixes: {}".format(time.time() - t))
    print("Inmultirea este egal cu aorib: {}\n".format(verify_matrix_equality(dot_result, AoriB)))


def vector(A, b, x, name):
    t = time.time()
    bcalc = mult_matrix_vector(A, x)
    print("{} * x : {}".format(name, time.time() - t))
    print(
        "Vectorul calculat este egal cu b-ul din fisier-ul {}.txt: {}\n".format(name.lower(), verify_vectors(b, bcalc)))


t = time.time()
A, bA = get_matrix("a.txt", True)
ok = True
for line in A.values():
    if len(line.keys())>12:
        ok = False
if ok is False:
    print("A nu este sparse: mai mult de 12 elemente nenule pe line")
B, bB = get_matrix("b.txt", True)
ok = True
for line in B.values():
    if len(line.keys())>12:
        ok = False
if ok is False:
    print("B nu este sparse: mai mult de 12 elemente nenule pe line")
AplusB = get_matrix("aplusb.txt", False)
AoriB = get_matrix("aorib.txt", False)
x = list(range(2019, -1, -1))

print("Loading the matrixes: {}\n".format(time.time() - t))

adunare(A, B, AplusB)
inmultire(A, B, AoriB)
vector(A, bA, x, "A")
vector(B, bB, x, "B")

