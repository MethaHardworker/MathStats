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


def pCounts(bounds):
    F = [0] * (len(bounds) + 1)
    F[0] = sc.norm.cdf(bounds[0])
    F[len(bounds)] = 1 - sc.norm.cdf(bounds[len(bounds) - 1])
    for i in range(1, len(bounds)):
        F[i] = sc.norm.cdf(bounds[i]) - sc.norm.cdf(bounds[i - 1])
    return F


n = 100
a_s = [-1.5, -0.5, 0, 0.5, 1.5]
data = sc.norm.rvs(size=n, scale=1, loc=0)
print(sc.norm.fit(data))
n_s = binCount(data, a_s)
p_s = pCounts(a_s)

print('ps:', p_s)


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
