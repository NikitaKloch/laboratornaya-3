import math
EPS = 1e-10

a = 1 / 2
S, n = a, 0
while math.fabs(a) > EPS:
    a *= (-((4 * (math.pi ** 2) * n) + (math.pi ** 2) / (16 * (n ** 2) + (36 * n) + 20)))
    S += a
    n += 1

print("Ei: ", '%.3f' % S)
