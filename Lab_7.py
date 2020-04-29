import scipy.stats as sc


def binCount(arr, bounds):
    res = [0] * (len(bounds) + 1)
    for x in arr:
        if x < bounds[0]:
            res[0] += 1
        elif x > bounds[len(bounds) - 1]:
            res[len(bounds)] += 1
        else:
            for i in range(len(bounds)):
                if bounds[i] < x < bounds[i + 1]:
                    res[i + 1] += 1
    return res


def binCountU(arr, bounds):
    res = [0] * (len(bounds) - 1)
    for x in arr:
        for i in range(len(bounds) - 1):
            if bounds[i] < x < bounds[i + 1]:
                res[i] += 1
                break
    return res

def pCounts(bounds):
    F = [0] * (len(bounds) + 1)
    F[0] = sc.norm.cdf(bounds[0])
    F[len(bounds)] = 1 - sc.norm.cdf(bounds[len(bounds) - 1])
    for i in range(1, len(bounds)):
        F[i] = sc.norm.cdf(bounds[i]) - sc.norm.cdf(bounds[i - 1])
    return F


def pCountsU(bounds):
    F = [0] * (len(bounds) - 1)
    for i in range(1, len(bounds)):
        F[i - 1] = sc.norm.cdf(bounds[i]) - sc.norm.cdf(bounds[i - 1])
    return F


n = 100
n1 = 25
a_s = [-1.5, -0.5, 0, 0.5, 1.5]
a_s1 = [-2, -1, 0, 1, 2]
data = sc.norm.rvs(size=n, scale=1, loc=0)
data1 = sc.uniform.rvs(size=n1, scale=4, loc=-2)
print(sc.norm.fit(data))
n_s = binCount(data, a_s)
n_s1 = binCountU(data1, a_s1)
p_s1 = pCountsU(a_s1)
p_s = pCounts(a_s)


print('ps1: ', p_s1)

for i in range(len(p_s)):
    print(i + 1, end=' & ')
    if i == 0:
        print('[ -\\inf,', a_s[0], ']', end=' & ')
    elif i == len(a_s):
        print('[', a_s[i - 1], '+\\inf ]', end=' & ')
    else:
        print('[', a_s[i - 1], a_s[i], ']', end=' & ')
    print(n_s[i], end=' & ')
    print(p_s[i], end=' & ')
    print(n * p_s[i], end=' & ')
    print(n_s[i] - n * p_s[i], end=' & ')
    print(((n_s[i] - n * p_s[i]) ** 2) / (n * p_s[i]), end=' \\\\ \\hline\n')

for i in range(len(p_s1)):
    print(i + 1, end=' & ')
    print('$[', a_s1[i], a_s1[i + 1], ']$', end=' & ')
    print(n_s1[i], end=' & ')
    print(p_s1[i], end=' & ')
    print(n1 * p_s1[i], end=' & ')
    print(n_s1[i] - n1 * p_s1[i], end=' & ')
    print(((n_s1[i] - n1 * p_s1[i]) ** 2) / (n1 * p_s1[i]), end=' \\\\ \\hline\n')

