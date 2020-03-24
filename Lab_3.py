from scipy.stats import *
import numpy
import matplotlib.pyplot as plt
import math



#x = numpy.linspace(-1000, 1000, 10000)
print("norm:")
Q_1 = norm.ppf(0.25)
Q_3 = norm.ppf(0.75)
X_1 = Q_1 - 3 / 2 * (Q_3 - Q_1)
X_2 = Q_3 + 3 / 2 * (Q_3 - Q_1)
P_o = 1 + norm.cdf(X_1) - norm.cdf(X_2)
print("Q_1 = " + str(Q_1))
print("Q_3 = " + str(Q_1))
print("X_1 = " + str(X_1))
print("X_2 = " + str(X_2))
print("P_o = " + str(P_o))

print("cauchy:")
Q_1 = cauchy.ppf(0.25)
Q_3 = cauchy.ppf(0.75)
X_1 = Q_1 - 3 / 2 * (Q_3 - Q_1)
X_2 = Q_3 + 3 / 2 * (Q_3 - Q_1)
P_o = 1 + cauchy.cdf(X_1) - cauchy.cdf(X_2)
print("Q_1 = " + str(Q_1))
print("Q_3 = " + str(Q_1))
print("X_1 = " + str(X_1))
print("X_2 = " + str(X_2))
print("P_o = " + str(P_o))

print("laplace:")
Q_1 = laplace.ppf(0.25, scale=1/math.sqrt(2))
Q_3 = laplace.ppf(0.75, scale=1/math.sqrt(2))
X_1 = Q_1 - 3 / 2 * (Q_3 - Q_1)
X_2 = Q_3 + 3 / 2 * (Q_3 - Q_1)
P_o = 1 + laplace.cdf(X_1, scale=1/math.sqrt(2)) - laplace.cdf(X_2, scale=1/math.sqrt(2))
print("Q_1 = " + str(Q_1))
print("Q_3 = " + str(Q_1))
print("X_1 = " + str(X_1))
print("X_2 = " + str(X_2))
print("P_o = " + str(P_o))

print("poisson:")
Q_1 = poisson.ppf(0.25, mu=10)
Q_3 = poisson.ppf(0.75, mu=10)
X_1 = Q_1 - 3 / 2 * (Q_3 - Q_1)
X_2 = Q_3 + 3 / 2 * (Q_3 - Q_1)
P_o = 1 + poisson.cdf(X_1, mu=10) - poisson.cdf(X_2, mu=10)
print("Q_1 = " + str(Q_1))
print("Q_3 = " + str(Q_1))
print("X_1 = " + str(X_1))
print("X_2 = " + str(X_2))
print("P_o = " + str(P_o))

print("uniform:")
Q_1 = uniform.ppf(0.25, loc=-math.sqrt(3), scale=2*math.sqrt(3))
Q_3 = uniform.ppf(0.75, loc=-math.sqrt(3), scale=2*math.sqrt(3))
X_1 = Q_1 - 3 / 2 * (Q_3 - Q_1)
X_2 = Q_3 + 3 / 2 * (Q_3 - Q_1)
P_o = 1 + uniform.cdf(X_1, loc=-math.sqrt(3), scale=2*math.sqrt(3)) - uniform.cdf(X_2, loc=-math.sqrt(3), scale=2*math.sqrt(3))
print("Q_1 = " + str(Q_1))
print("Q_3 = " + str(Q_1))
print("X_1 = " + str(X_1))
print("X_2 = " + str(X_2))
print("P_o = " + str(P_o))


n_s = [20, 100]

data = list()
for i in range(len(n_s)):
    r = norm.rvs(size=n_s[i])
    data.append(r)
fig1, ax1 = plt.subplots()
ax1.set_title('Normal')
ax1.set_xlabel('x')
ax1.set_ylabel('n')
ax1.boxplot(data, vert=False, labels=n_s)
plt.show()

data = list()
for i in range(len(n_s)):
    r = cauchy.rvs(size=n_s[i])
    data.append(r)
fig1, ax1 = plt.subplots()
ax1.set_title('Cauchy')
ax1.set_xlabel('x')
ax1.set_ylabel('n')
ax1.boxplot(data, vert=False, labels=n_s)
plt.show()

data = list()
for i in range(len(n_s)):
    r = laplace.rvs(scale=1/math.sqrt(2), size=n_s[i])
    data.append(r)
fig1, ax1 = plt.subplots()
ax1.set_title('Laplace')
ax1.set_xlabel('x')
ax1.set_ylabel('n')
ax1.boxplot(data, vert=False, labels=n_s)
plt.show()


data = list()
for i in range(len(n_s)):
    r = poisson.rvs(10, size=n_s[i])
    data.append(r)
fig1, ax1 = plt.subplots()
ax1.set_title('Poisson')
ax1.set_xlabel('x')
ax1.set_ylabel('n')
ax1.boxplot(data, vert=False, labels=n_s)
plt.show()

data = list()
for i in range(len(n_s)):
    r = uniform.rvs(loc=-math.sqrt(3), scale=2 * math.sqrt(3), size=n_s[i])
    data.append(r)
fig1, ax1 = plt.subplots()
ax1.set_title('Unif')
ax1.set_xlabel('x')
ax1.set_ylabel('n')
ax1.boxplot(data, vert=False, labels=n_s)
plt.show()

