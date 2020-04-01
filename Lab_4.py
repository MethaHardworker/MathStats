from scipy.stats import *
import numpy
import matplotlib.pyplot as plt

n_s = [20, 60, 100]

for size in n_s:
    x = numpy.linspace(-4, 4, 1000)
    y = norm.cdf(x)
    plt.subplot(1, len(n_s), n_s.index(size) + 1)

    x = norm.rvs(scale=1)
    x.sort()
    y = numpy.linspace(0, 1, size)
    plt.plot(x, y)

