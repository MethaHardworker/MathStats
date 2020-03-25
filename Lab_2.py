from scipy.stats import *
import math


def trimmed_sum(iterable, start, end):
    s = 0
    for i in range(start, end):
        s += iterable[i]
    return s


def chooseDistribution(name, n):
    if name == 'norm':
        return norm.rvs(size=n)
    elif name == 'cauchy':
        return cauchy.rvs(size=n)
    elif name == 'laplace':
        return laplace.rvs(scale=1/math.sqrt(2), size=n)
    elif name == 'poisson':
        return poisson.rvs(10, size=n)
    elif name == 'uniform':
        return uniform.rvs(loc=-math.sqrt(3), scale=2*math.sqrt(3), size=n)
    else:
        return


n_s = [10, 100, 1000]
titles = ["norm", "cauchy", "laplace", "poisson", "uniform"]

# norm
for title in titles:
    print(title)
    for n in n_s:
        E_e = 0
        D_e = 0
        E_med = 0
        D_med = 0
        E_r = 0
        D_r = 0
        E_q = 0
        D_q = 0
        E_tr = 0
        D_tr = 0
        for i in range(1000):
            x = chooseDistribution(title, n)
            x.sort()
            x_e = sum(x) / n
            E_e += x_e
            D_e += x_e * x_e
            half = int(n / 2)
            x_med = (x[half] + x[half + 1]) / 2
            E_med += x_med
            D_med += x_med * x_med
            x_r = (x[0] + x[n - 1]) / 2
            E_r += x_r
            D_r += x_r * x_r
            r = int(n / 4)
            x_q = (x[r] + x[3 * r]) / 2
            E_q += x_q
            D_q += x_q * x_q
            x_tr = trimmed_sum(x, r + 1, n - r)
            x_tr /= n - 2 * r
            E_tr += x_tr
            D_tr += x_tr * x_tr
        E_e /= 1000
        D_e = D_e / 1000 - E_e * E_e
        E_med /= 1000
        D_med = D_med / 1000 - E_med * E_med
        E_q /= 1000
        D_q = D_q / 1000 - E_q * E_q
        E_r /= 1000
        D_r = D_r / 1000 - E_r * E_r
        E_tr /= 1000
        D_tr = D_tr / 1000 - E_tr * E_tr
        print(str(n) + ":")
        print("E_e = " + str(E_e))
        print("D_e = " + str(D_e))
        print("E_med = " + str(E_med))
        print("D_med = " + str(D_med))
        print("E_q = " + str(E_q))
        print("D_q = " + str(D_q))
        print("E_r = " + str(E_r))
        print("D_r = " + str(D_r))
        print("E_tr = " + str(E_tr))
        print("D_tr = " + str(D_tr))
