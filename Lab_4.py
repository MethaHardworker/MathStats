from scipy.stats import *
import seaborn as sns
import numpy
import matplotlib.pyplot as plt
from math import *

n_s = [20, 60, 100]
################## NORM ##########################
for size in n_s:
    plt.subplot(1, len(n_s), n_s.index(size) + 1)
    plt.title('n = ' + str(size))
    plt.xlabel('x')
    plt.ylabel('y')
    x = numpy.linspace(-4, 4, 1000)
    plt.plot(x, norm.cdf(x), color='red')
    x_a = norm.rvs(size=size)
    x_a = x_a[x_a <= 4]
    x_a = x_a[x_a >= -4]
    x_a.sort()
    size = x_a.size
    y_a = numpy.linspace(0, 1, size)
    x2 = [0] * size * 2
    x2[0] = -4
    y2 = [0] * size * 2
    y2[0] = 0
    for i in range(size - 1):
        x2[2 * i + 1] = x_a[i]
        x2[2 * i + 2] = x_a[i + 1]
        y2[2 * i + 1] = y_a[i]
        y2[2 * i + 2] = y_a[i]
    x2[2 * size - 1] = 4
    y2[2 * size - 1] = 1
    x2[2 * size - 2] = x_a[size - 1]
    y2[2 * size - 2] = 1
    plt.plot(x2, y2)

for size in n_s:
    fig, ax = plt.subplots(1, 3)
    x = numpy.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)
    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)
    x = norm.rvs(size=size)
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()

    gauss = gaussian_kde(x, bw_method='silverman')
    h_n = gauss.factor
    sns.kdeplot(x, ax=ax[0], bw=h_n / 2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=2 * h_n)
    ax[0].set_title(r'$h = h_n/2$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = 2h_n$')

plt.show()

############## LAPLACE ####################

for size in n_s:
    plt.subplot(1, len(n_s), n_s.index(size) + 1)
    plt.title('n = ' + str(size))
    plt.xlabel('x')
    plt.ylabel('y')
    x = numpy.linspace(-4, 4, 1000)
    plt.plot(x, laplace.cdf(x, scale=1/sqrt(2)), color='red')
    x_a = laplace.rvs(size=size, scale=1/sqrt(2))
    x_a = x_a[x_a <= 4]
    x_a = x_a[x_a >= -4]
    x_a.sort()
    size = x_a.size
    y_a = numpy.linspace(0, 1, size)
    x2 = [0] * size * 2
    x2[0] = -4
    y2 = [0] * size * 2
    y2[0] = 0
    for i in range(size - 1):
        x2[2 * i + 1] = x_a[i]
        x2[2 * i + 2] = x_a[i + 1]
        y2[2 * i + 1] = y_a[i]
        y2[2 * i + 2] = y_a[i]
    x2[2 * size - 1] = 4
    y2[2 * size - 1] = 1
    x2[2 * size - 2] = x_a[size - 1]
    y2[2 * size - 2] = 1
    plt.plot(x2, y2)

for size in n_s:
    fig, ax = plt.subplots(1, 3)
    x = numpy.linspace(-4, 4, 1000)
    y = laplace.pdf(x, scale=1/sqrt(2))
    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)
    x = laplace.rvs(size=size, scale=1/sqrt(2))
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()

    gauss = gaussian_kde(x, bw_method='silverman')
    h_n = gauss.factor
    sns.kdeplot(x, ax=ax[0], bw=h_n / 2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=2 * h_n)
    ax[0].set_title(r'$h = h_n/2$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = 2h_n$')

plt.show()

############### CAUCHY ###############

for size in n_s:
    plt.subplot(1, len(n_s), n_s.index(size) + 1)
    plt.title('n = ' + str(size))
    plt.xlabel('x')
    plt.ylabel('y')
    x = numpy.linspace(-4, 4, 1000)
    plt.plot(x, cauchy.cdf(x), color='red')

    x_a = cauchy.rvs(size=size)
    x_a = x_a[x_a <= 4]
    x_a = x_a[x_a >= -4]
    x_a.sort()
    size = x_a.size
    y_a = numpy.linspace(0, 1, size)
    x2 = [0] * size * 2
    x2[0] = -4
    y2 = [0] * size * 2
    y2[0] = 0
    for i in range(size - 1):
        x2[2 * i + 1] = x_a[i]
        x2[2 * i + 2] = x_a[i + 1]
        y2[2 * i + 1] = y_a[i]
        y2[2 * i + 2] = y_a[i]
    x2[2 * size - 1] = 4
    y2[2 * size - 1] = 1
    x2[2 * size - 2] = x_a[size - 1]
    y2[2 * size - 2] = 1
    plt.plot(x2, y2)

for size in n_s:
    fig, ax = plt.subplots(1, 3)
    x = numpy.linspace(-4, 4, 1000)
    y = cauchy.pdf(x)
    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)
    x = cauchy.rvs(size=size)
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()
    gauss = gaussian_kde(x, bw_method='silverman')
    h_n = gauss.factor
    sns.kdeplot(x, ax=ax[0], bw=h_n / 2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=2 * h_n)
    ax[0].set_title(r'$h = h_n/2$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = 2h_n$')

plt.show()

############### POISSON ###################
for size in n_s:
    plt.subplot(1, len(n_s), n_s.index(size) + 1)
    plt.title('n = ' + str(size))
    plt.xlabel('x')
    plt.ylabel('y')
    x = numpy.linspace(6, 14, 1000)
    plt.plot(x, poisson.cdf(x, 10), color='red')

    x_a = poisson.rvs(10, size=size)
    x_a = x_a[x_a <= 14]
    x_a = x_a[x_a >= 6]
    x_a.sort()
    size = x_a.size
    y_a = numpy.linspace(0, 1, size)
    x2 = [0] * size * 2
    x2[0] = 6
    y2 = [0] * size * 2
    y2[0] = 0
    for i in range(size - 1):
        x2[2 * i + 1] = x_a[i]
        x2[2 * i + 2] = x_a[i + 1]
        y2[2 * i + 1] = y_a[i]
        y2[2 * i + 2] = y_a[i]
    x2[2 * size - 1] = 14
    y2[2 * size - 1] = 1
    x2[2 * size - 2] = x_a[size - 1]
    y2[2 * size - 2] = 1
    plt.plot(x2, y2)

for size in n_s:
    fig, ax = plt.subplots(1, 3)
    x = numpy.linspace(5, 15, 11)
    y = poisson.pmf(x, 10)
    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)

    x = poisson.rvs(10, size=size)
    x = x[x <= 14]
    x = x[x >= 6]
    x.sort()

    gauss = gaussian_kde(x, bw_method='silverman')
    h_n = gauss.factor
    sns.kdeplot(x, ax=ax[0], bw=h_n / 2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=2 * h_n)
    ax[0].set_title(r'$h = h_n/2$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = 2h_n$')

plt.show()

############ UNIFORM ###################

for size in n_s:
    plt.subplot(1, len(n_s), n_s.index(size) + 1)
    plt.title('n = ' + str(size))
    plt.xlabel('x')
    plt.ylabel('y')
    x = numpy.linspace(-4, 4, 1000)
    plt.plot(x, uniform.cdf(x, -sqrt(3), 2 * sqrt(3)), color='red')

    x_a = uniform.rvs(size=size, loc=-sqrt(3), scale=2* sqrt(3))
    x_a = x_a[x_a <= 4]
    x_a = x_a[x_a >= -4]
    x_a.sort()
    size = x_a.size
    y_a = numpy.linspace(0, 1, size)
    x2 = [0] * size * 2
    x2[0] = -4
    y2 = [0] * size * 2
    y2[0] = 0
    for i in range(size - 1):
        x2[2 * i + 1] = x_a[i]
        x2[2 * i + 2] = x_a[i + 1]
        y2[2 * i + 1] = y_a[i]
        y2[2 * i + 2] = y_a[i]
    x2[2 * size - 1] = 4
    y2[2 * size - 1] = 1
    x2[2 * size - 2] = x_a[size - 1]
    y2[2 * size - 2] = 1
    plt.plot(x2, y2)

for size in n_s:
    fig, ax = plt.subplots(1, 3)
    x = numpy.linspace(-4, 4, 1000)
    y = uniform.pdf(x, -sqrt(3), 2*sqrt(3))
    ax[0].plot(x, y)
    ax[1].plot(x, y)
    ax[2].plot(x, y)

    x = uniform.rvs(size=size, loc=-sqrt(3), scale=2*sqrt(3))
    x = x[x <= 4]
    x = x[x >= -4]
    x.sort()

    gauss = gaussian_kde(x, bw_method='silverman')
    h_n = gauss.factor
    sns.kdeplot(x, ax=ax[0], bw=h_n / 2)
    sns.kdeplot(x, ax=ax[1], bw=h_n)
    sns.kdeplot(x, ax=ax[2], bw=2 * h_n)
    ax[0].set_title(r'$h = h_n/2$')
    ax[1].set_title(r'$h = h_n$')
    ax[2].set_title(r'$h = 2h_n$')

plt.show()

