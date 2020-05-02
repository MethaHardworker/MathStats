import scipy.stats as sc
import numpy as np


def getM(x, p):
    if p == 1:
        ev = 0
    else:
        ev = getM(x, 1)
    sum = 0
    for el in x:
        sum += pow(el - ev, p)
    return sum / len(x)


n_s = [20, 100]
alpha = 0.05
for n in n_s:
    r = sc.norm.rvs(size=n, scale=1, loc=0)
    o_x = getM(r, 1) # np.mean(r)
    s = np.sqrt(getM(r, 2)) #np.std(r)
    d = s * sc.t.ppf(1 - alpha / 2, n - 1) / np.sqrt(n - 1)
    print('T & Chi:')
    print('$', o_x - d, '< m <', o_x + d, '$')
    print('$', s * np.sqrt(n) / np.sqrt(sc.chi2.ppf(1 - alpha / 2, n - 1)), '< \\sigma <',
          s * np.sqrt(n) / np.sqrt(sc.chi2.ppf(alpha / 2, n - 1)), '$')
    print('Assimpt:')
    d = s * sc.norm.ppf(1 - alpha / 2) / np.sqrt(n)
    U = sc.norm.ppf(1 - alpha / 2) * np.sqrt((getM(r, 4) / pow(s, 4) - 1) / n)
    print('$', o_x - d, '< m <', o_x + d, '$')
    print('$', s * pow((1 + U), -0.5), '< \\sigma <', s * pow(1 - U, -0.5), '$')
