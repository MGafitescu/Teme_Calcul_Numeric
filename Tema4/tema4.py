import time
import math

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


def solve_system(matrix, size, vector, omega):
    xc = []
    delta = 1
    kmax = 10000
    for i in range(0, size):
        xc.append(0)

    k = 0
    while epsilon <= delta <= 10 ** 8 and k <= kmax:
        delta = 0
        for i in range(0, size):
            s1 = 0
            s2 = 0
            xp = xc[i]
            for column, value in matrix[i].items():
                if column < i:
                    s1 += matrix[i][column] * xc[column]
                else:
                    s2 += matrix[i][column] * xc[column]
            xc[i] = xc[i] + omega / matrix[i][i] * (vector[i] - s1 - s2)
            delta += (xc[i] - xp) ** 2
        k = k + 1
        delta = math.sqrt(delta)
    print(k)
    if delta > epsilon:
        print("Divergenta")
        return None
    else:
        return xc


def mult_matrix_vector(A, x):
    result = []
    for index, row in enumerate(A.values()):
        result.append(sum([v * x[i] for (i, v) in row.items()]))

    return result


def calculate_norm(v1, v2, size):
    vect = []
    for i in range(size):
        vect.append(math.fabs(v1[i] - v2[i]))
    return max(vect)


def calculate_for_omega(matrix, vector, size, omega):
    t = time.time()
    sol = solve_system(matrix, size, vector, omega)
    print("Rezolvare cu omega={}: {}".format(omega, time.time() - t))
    # print(sol)
    matrix_x = mult_matrix_vector(matrix, sol)
    norma = calculate_norm(matrix_x, vector, size)
    print("Norma A*x_calculat - b: {}\n".format(norma))


def calculate_solution(file):
    print("Calculul pentru {}".format(file))
    matrix, vector, size = get_matrix(file, True)
    diagonala_nenula = verify_diagonal(matrix, size)
    print("Elementele de pe diagonale sunt nenule: {}".format(diagonala_nenula))

    if diagonala_nenula:
        calculate_for_omega(matrix, vector, size, 0.8)
        calculate_for_omega(matrix, vector, size, 1.0)
        calculate_for_omega(matrix, vector, size, 1.2)
    else:
        print("Nu se poate rezolva -> Divergenta")


calculate_solution("m_rar_2019_1.txt")
calculate_solution("m_rar_2019_2.txt")
calculate_solution("m_rar_2019_3.txt")
calculate_solution("m_rar_2019_4.txt")
calculate_solution("m_rar_2019_5.txt")
