import random
import sys
import numpy as np


class LU_decomposition:
    def __init__(self, n, precision):
        self.precision = 10 ** ((-1)*precision)
        self.n = n
        sys = self.system_creator(n)
        self.A = [[1.5, 3, 3], [2, 6.5, 14], [1, 3, 8]]
        self.Acopy = [[float(self.A[j][i]) for i in range(n)] for j in range(n)]
        self.B = sys[1]

    def get_precision(self):
        return self.precision

    def system_creator(self, n):
        A = [[random.randint(5, 11) for x in range(n)] for e in range(n)]
        B = [random.randint(5, 11) for x in range(n)]
        return (A, B)

    def nonzero(self, v):
        if np.abs(v) > self.get_precision():
            return True
        else:
            print("This would be a division by 0!")
            sys.exit()

    def is_singular(self):
        det = np.linalg.det(self.A)
        if det != 0:
            return False
        else:
            return True

    def is_tridiagonal(self):
        det = np.linalg.det(self.A)
        if det != 0:
            return False
        else:
            return True

    def do_LU_decomposition(self):
        for p in range(0, self.n):
            for i in range(0, p+1):
                a = sum(self.A[k][i] * self.A[p][k] for k in range(0, i))
                s = sum(self.A[k][p] * self.A[i][k] for k in range(0, i))

                self.A[p][i] = self.A[p][i] - a

                if (i < p):
                    if self.nonzero(self.A[i][i]) is True:
                        self.A[i][p] = (self.Acopy[i][p] - s)/self.A[i][i]
                    else:
                        print("BREAK HERE")


lu_instance = LU_decomposition(3, 15)
print(lu_instance.A)
lu_instance.do_LU_decomposition()
print(lu_instance.A)


