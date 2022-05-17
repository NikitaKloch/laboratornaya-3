import sys

n = int(input("Введите потраченое электричество: "))
kv = 7
kv1 = 17
kv2 = 20
if n <= 250:
    k = kv * n
    print(k, "руб.")
if 251 <= n <= 300:
    k = kv1 * n
    print(k, "руб.")
if n >= 301:
    k = kv2 * n
    print(k, "руб.")
if n <= 0:
    print("n должно быть больше 1",file=sys.stderr)