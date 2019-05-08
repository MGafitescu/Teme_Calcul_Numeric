import numpy as np
import math
import random

epsilon = 10 ** -10


def get_matrix(filename, vector):
    f = open(filename)
    content = f.read()
    f.close()
    lines = content.split("\n")
    del lines[1]
    size = int(lines[0])
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
        return matrix, b, size
    return matrix, size


def verify_diagonal(matrix, size):
    for i in range(0, size):
        if matrix[i].get(i, 0) < epsilon:
            return False
    return True


def mult_matrix_vector(A, x):
    result = []
    for index, row in enumerate(A.values()):
        result.append(sum([v * x[i] for (i, v) in row.items()]))

    return result


def calculate_norm(v):
    norm = 0
    for el in v:
        norm = norm + el * el
    norm = math.sqrt(norm)
    return norm


def calculate_scalar_product(v1, v2):
    result = 0
    for i in range(0, len(v1)):
        result = result + v1[i] * v2[i]
    return result


def generate_vector(size):
    vect = []
    vect_normalized = []
    for i in range(0, size):
        vect.append(random.randint(1, 100))
    norm = calculate_norm(vect)
    for el in vect:
        vect_normalized.append(el / norm)
    return vect_normalized


def calculate_required_norm(w, lambd, v):
    v_multiplied = []
    difference = []
    for el in v:
        v_multiplied.append(lambd * el)
    for i in range(0, len(w)):
        difference.append(w[i] - v_multiplied[i])
    return calculate_norm(difference)


def metoda_puterii(matrix, size):
    vect = generate_vector(size)
    w = mult_matrix_vector(matrix, vect)
    lambd = calculate_scalar_product(w, vect)
    k = 0
    kmax = 500
    while calculate_required_norm(w, lambd, vect) > size * epsilon and k <= kmax:
        vect = []
        for el in w:
            vect.append(el / calculate_norm(w))
        w = mult_matrix_vector(matrix, vect)
        lambd = calculate_scalar_product(w, vect)
        k = k + 1
    return lambd, vect


def verify_simmetry(matrix):
    for line in matrix.keys():
        for column in matrix.keys():
            if (matrix[line].get(column, 0) - matrix[column].get(line, 0)) > epsilon:
                print(line, column)
                return False
    return True


def generate_matrix(size):
    f = open("matrix.txt", "w")
    f.write(str(size))
    f.write("\n")
    f.write("\n")

    for line in range(0, size - 1):
        for j in range(0, random.randint(0, 5)):
            column = random.randint(0, int(size - 1 / 2))
            number = random.randint(1, 1000)
            f.write(str(number))
            f.write(", ")
            f.write(str(line))
            f.write(", ")
            f.write(str(column))
            f.write("\n")
            f.write(str(number))
            f.write(", ")
            f.write(str(column))
            f.write(", ")
            f.write(str(line))
            f.write("\n")
    f.close()


def transform_matrix(matrix, size):
    normal_matrix = []
    for i in range(0, size):
        line = []
        for j in range(0, size):
            line.append(0)
        normal_matrix.append(line)
    for line, value in matrix.items():
        for column, element in value.items():
            normal_matrix[line][column] = element
    return normal_matrix


filenames = ["matrix.txt", "m_rar_sim_2019_500.txt", "m_rar_sim_2019_1000.txt",
             "m_rar_sim_2019_1500.txt", "m_rar_sim_2019_2019.txt"]


def execute(filenames):
    for f in filenames:
        print("Matricea: {}".format(f))
        matrix, size = get_matrix(f, False)
        print("Este simetrica: {}".format(verify_simmetry(matrix)))
        lambd, vect = metoda_puterii(matrix, size)
        print("Valoarea proprie maxima:{}\nVectorul propriu asociat:{}\n".format(lambd, vect))


def librarie(filename):
    matrix, size = get_matrix(filename, False)
    m = transform_matrix(matrix, size)
    m_np = np.array(m)
    u, s, vh = np.linalg.svd(m_np)
    print("Valorile singulare ale matricii: ")
    for el in s:
        print(el)
    print("Rangul matricii: ")

    rank = len([el for el in set(s) if el > 0])
    print(rank)
    print("Numarul de conditionare a matricii: ")
    conditioning_number = max(s) / min([el for el in set(s) if el > 0])
    print(conditioning_number)
    print("Pseudoinversa Moore-Penrose")
    ps_moore_penrose = np.linalg.pinv(m_np)
    print(ps_moore_penrose)
    b = []
    for i in range(0, size):
        b.append(random.randint(0, 100))
    difference = []
    x = np.dot(ps_moore_penrose, b)
    pmp_x = np.dot(m_np, x)
    for i in range(0, size):
        difference.append(b[i] - pmp_x[i])
    norm = calculate_norm(difference)
    print("Norma b-Ax: ")
    print(norm)


generate_matrix(600)
execute(filenames)
librarie("m_rar_sim_2019_500.txt")