import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def getM1(x):
    return sum(x) / len(x)


def getM2(x):
    sum = 0
    for el in x:
        sum += el * el
    return sum / len(x)


def getM12(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]
    return sum / len(x)


def getRQ(x, y):
    x1 = x.copy()
    x1.sort()
    medx = x1[9]
    y1 = y.copy()
    y1.sort()
    medy = y1[9]
    sum = 0
    for i in range(len(x)):
        sum += np.sign(x[i] - medx) * np.sign(y[i] - medy)
    return sum / len(x)


x = np.arange(-1.8, 2.1, 0.2)
e = norm.rvs(size=20)
y = 2 + 2 * x + e
### MNK ###
x_ = getM1(x)
y_ = getM1(y)
xy_ = getM12(x, y)
x2_ = getM2(x)
y2_ = getM2(y)
b1 = (xy_ - x_ * y_) / (x2_ - x_ ** 2)
b0 = y_ - x_ * b1

y_n = y.copy()
y_n[0] += 10
y_n[19] += -10

y_ = getM1(y_n)
xy_ = getM12(x, y_n)
b11 = (xy_ - x_ * y_) / (x2_ - x_ ** 2)
b01 = y_ - x_ * b11

x_nice = np.linspace(-1.8, 2, 1000)
y_nice1m = x_nice * b1 + b0
y_nice2m = x_nice * b11 + b01
y_true = x_nice * 2 + 2

### Robust ###
x1 = x.copy()
x1.sort()
medx = x1[9]
y1 = y.copy()
y1.sort()
medy = y1[9]
r_Q = getRQ(x, y)
b1r = r_Q * (y1[14] - y1[4]) / (x1[14] - x1[4])
b0r = medy - b1r * medx
y_nice1r = x_nice * b1r + b0r

x1 = x.copy()
x1.sort()
medx = x1[9]
y1 = y_n.copy()
y1.sort()
medy = y1[9]
r_Q = getRQ(x, y1)
b1r_ = r_Q * (y1[14] - y1[4]) / (x[14] - x[4])
b0r_ = medy - b1r_ * medx
y_nice2r = x_nice * b1r_ + b0r_

print(b0, b1)
print(b0r, b1r)
print(b01, b11)
print(b0r_, b1r_)

plt.scatter(x, y, label='Выборка')
plt.plot(x_nice, y_nice1m, color='red', label='МНК')
plt.plot(x_nice, y_nice1r, color='black', label='МНМ')
plt.plot(x_nice, y_true, color='green', label='Модель')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower center')

plt.figure()
plt.scatter(x, y_n, label='Выборка')
plt.plot(x_nice, y_nice2m, color='red', label='МНК')
plt.plot(x_nice, y_nice2r, color='black', label='МНМ')
plt.plot(x_nice, y_true, color='green', label='Модель')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower center')
plt.show()
