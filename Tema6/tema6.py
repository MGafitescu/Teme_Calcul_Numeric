import random
import math
epsilon = 10 ** -10

def horner(coefficients,x):
    b = coefficients[0]
    for i in range(1,len(coefficients)):
        b = coefficients[i]+b*x
    return b

def derivate(coefficients):
    new_coefficients = []
    for index,coef in enumerate(coefficients[:-1]):
        new_coefficients.append(coef*(len(coefficients)-index-1))
    return new_coefficients

def halley(coefficients):
    max_coef = max(coefficients)
    r = (coefficients[0]+max_coef)/coefficients[0]
    r = int(r)+1
    k= 1
    kmax = 100000
    x = random.randrange(-r,r)
    delta = 12
    while epsilon<=math.fabs(delta)<=10**8 and k<=kmax:
        first_dev = derivate(coefficients)
        second_dev = derivate(first_dev)
        a = 2*(horner(first_dev,x)**2)-horner(coefficients,x)*horner(second_dev,x)
        if math.fabs(a)<epsilon:
            x = random.randrange(-r,r)
            break;
        delta = horner(coefficients,x)*horner(first_dev,x)/a
        x = x - delta
        k = k+1
    if math.fabs(delta)<epsilon:
        return x
    else:
        print("Divergenta")

def solutions(coefficients):
    print("Polinomul: ",coefficients)

    sol = []
    for i in range(0,1000):
        s = halley(coefficients)
        if s is not None:
            values = [math.fabs(x-s) for x in sol]
            if not any(val< epsilon for val in values):
                sol.append(s)
    print("Radacinile polinomului: ",sol,"\n")
    f = open("file.txt","w")
    for s in sol:
        f.write(str(s))
        f.write("\t")
    f.write("\n")
    f.close()

p1 = [1,-6,11,-6]
p2 = [1,-55/42,-1,49/42,-6/42]
p3 = [1,-38/8,49/8,-22/8,3/8]
solutions(p1)
solutions(p2)
solutions(p3)

