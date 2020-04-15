import scipy.stats as sc
import numpy as np
import matplotlib.pyplot as plt
import math


def getR(string, arr):
    def rCounting(ar1, ar2):
        n_s = [0, 0, 0, 0]
        for j in range(len(ar1)):
            if ar1[j] * ar2[j] > 0:
                if ar1[j] > 0:
                    n_s[0] += 1
                else:
                    n_s[2] += 1
            else:
                if ar1[j] > 0:
                    n_s[3] += 1
                else:
                    n_s[1] += 1
        return ((n_s[0] + n_s[2]) - (n_s[1] + n_s[3])) / len(ar1)

    arr = arr.transpose()
    if string == 'r_Q':
        return rCounting(arr[0], arr[1])
    elif string == 'r_s':
        r_val, p_v = sc.spearmanr(arr[0], arr[1])
        return r_val
    elif string == 'r':
        r_val, p_v = sc.pearsonr(arr[0], arr[1])
        return r_val


rhoS = [0.0, 0.5, 0.9]
n_s = [20, 60, 100]
for n in n_s:
    print(str(n) + '\n')
    for rho in rhoS:
        all_r = {'r_Q': [0, 0, 0], 'r_s': [0, 0, 0], 'r': [0, 0, 0]}  # E_x = 0, E_x2 = 0, D_x = 0
        cor_matrix = np.array([[1, float(rho)], [float(rho), 1]])
        for it in range(1000):
            x = sc.multivariate_normal.rvs(np.zeros(2), cov=cor_matrix, size=n)
            for r in all_r:
                cov = getR(r, x)
                all_r.get(r)[0] += cov
                all_r.get(r)[1] += cov ** 2
        print('rho = ' + str(rho) + ' & E(z) & E(z^2) & D(z) \\\\')
        for r in all_r:
            all_r.get(r)[0] /= 1000
            all_r.get(r)[1] /= 1000
            all_r.get(r)[2] = all_r.get(r)[1] - all_r.get(r)[0] ** 2
            print(r, end=' &')
            for i in range(3):
                print(all_r.get(r)[i], end=' ')
                if i != 2:
                    print('&', end=' ')
            print('\\\\')
        print()
    print('MIX: ')
    all_r = {'r_Q': [0, 0, 0], 'r_s': [0, 0, 0], 'r': [0, 0, 0]}  # E_x = 0, E_x2 = 0, D_x = 0
    cor_matrix1 = np.array([[1, 0.9], [0.9, 1]])
    #cor_matrix2 = np.array([[100, -90], [-90, 100]])
    cor_matrix2 = 100 * np.array([[1, -0.9], [-0.9, 1]])
    for it in range(1000):
        x1 = sc.multivariate_normal.rvs(np.zeros(2), cov=cor_matrix1, size=n)
        x2 = sc.multivariate_normal.rvs(np.zeros(2), cov=cor_matrix2, size=n)
        x = 0.9 * x1 + 0.1 * x2
        for r in all_r:
            cov = getR(r, x)
            all_r.get(r)[0] += cov
            all_r.get(r)[1] += cov ** 2
    for r in all_r:
        all_r.get(r)[0] /= 1000
        all_r.get(r)[1] /= 1000
        all_r.get(r)[2] = all_r.get(r)[1] - all_r.get(r)[0] ** 2
        print(r, end=' &')
        for i in range(3):
            print(all_r.get(r)[i], end=' ')
            if i != 2:
                print('&', end=' ')
        print('\\\\')
    print()
for n in n_s:
    step = 0.05
    x = np.arange(-5, 5, step)
    y = np.arange(-5, 5, step)
    fig, ax = plt.subplots(1, 3, figsize=(9, 3))
    #fig.suptitle('Normal distribution n = ' + str(n))
    for i in range(len(rhoS)):
        cor_matrix = np.array([[1, float(rhoS[i])], [float(rhoS[i]), 1]])
        X, Y = np.meshgrid(x, y)
        Z = X ** 2 - 2 * rhoS[i] * X * Y + Y ** 2
        x_norm = np.transpose(sc.multivariate_normal.rvs(np.zeros(2), cov=cor_matrix, size=n))
        ax[i].set_xlim([-4, 4])
        ax[i].set_ylim([-4, 4])
        ax[i].scatter(x_norm[0], x_norm[1], color='k', marker='o', s=4)
        ax[i].contour(X, Y, Z, [4 * math.sqrt(1 - rhoS[i]**2)])
        ax[i].set_title(r'$\rho$ = ' + str(rhoS[i]))
        ax[i].set_xlabel('x')
        ax[i].set_ylabel('y')
    cor_matrix1 = np.array([[1, 0.9], [0.9, 1]])
    cor_matrix2 = 100 * np.array([[1, -0.9], [-0.9, 1]])
    x1 = sc.multivariate_normal.rvs(np.zeros(2), cov=cor_matrix1, size=n)
    x2 = sc.multivariate_normal.rvs(np.zeros(2), cov=cor_matrix2, size=n)
    x = 0.9 * x1 + 0.1 * x2
    x = np.transpose(x)
    fig1, ax = plt.subplots(1, 1)
    ax.scatter(x[0], x[1], color='b', marker='o', s=4)
plt.show()
