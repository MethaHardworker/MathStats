from scipy.stats import *
import numpy
import matplotlib.pyplot as plt
import math

n_s = [10, 50, 1000]

plt.figure()
for i in range(len(n_s)):
    k = int(10 + 3.31 * math.log10(n_s[i]))
    plt.subplot(1, len(n_s), i + 1)
    plt.title("n = " + str(n_s[i]))
    plt.ylabel("Плотность распределения")
    r = norm.rvs(size=n_s[i])
    x = numpy.linspace(min(r), max(r), 3000)
    plt.plot(x, norm.pdf(x), color='red')
    plt.hist(r, k, density=True, histtype='stepfilled', alpha=0.5, color='green')
plt.savefig('norm.png')
plt.show()

plt.figure()
for i in range(len(n_s)):
    k = int(10 + 3.31 * math.log10(n_s[i]))
    plt.subplot(1, len(n_s), i + 1)
    plt.title("n = " + str(n_s[i]))
    plt.ylabel("Плотность распределения")
    r = cauchy.rvs(size=n_s[i])
    x = numpy.linspace(min(r), max(r), 3000)
    plt.plot(x, cauchy.pdf(x), color='red')
    plt.hist(r, k, density=True, histtype='stepfilled', alpha=0.5, color='green')
plt.savefig('cauchy.png')
plt.show()


plt.figure()
for i in range(len(n_s)):
    k = int(10 + 3.31 * math.log10(n_s[i]))
    plt.subplot(1, len(n_s), i + 1)
    plt.title("n = " + str(n_s[i]))
    plt.ylabel("Плотность распределения")
    r = laplace.rvs(scale=1/math.sqrt(2), size=n_s[i])
    x = numpy.linspace(min(r), max(r), 3000)
    plt.plot(x, laplace.pdf(x), color='red')
    plt.hist(r, k, density=True, histtype='stepfilled', alpha=0.5, color='green')
plt.savefig('laplace.png')
plt.show()


fig = plt.figure()
for i in range(len(n_s)):
    mu = 10
    k = int(10 + 3.31 * math.log10(n_s[i]))
    plt.subplot(1, len(n_s), i + 1)
    plt.title("n = " + str(n_s[i]))
    plt.ylabel("Плотность распределения")
    r = poisson.rvs(10, size=n_s[i])
    x = numpy.linspace(0, max(r), max(r) + 1)
    plt.plot(x, poisson.pmf(x, mu), color='red')
    plt.hist(r, k, density=True, histtype='stepfilled', alpha=0.5, color='green')
plt.savefig('poisson.png')
plt.show()


plt.figure()
for i in range(len(n_s)):
    plt.subplot(1, len(n_s), i + 1)
    plt.title("n = " + str(n_s[i]))
    plt.ylabel("Плотность распределения")
    r = uniform.rvs(loc=-math.sqrt(3), scale=2*math.sqrt(3), size=n_s[i])
    x = numpy.linspace(-math.sqrt(3), math.sqrt(3))
    plt.plot(x, uniform.pdf(x, loc=-math.sqrt(3), scale=2*math.sqrt(3)), color='red')
    plt.hist(r, density=True, histtype='stepfilled', alpha=0.5, color='green')
plt.savefig('uni.png')
plt.show()

