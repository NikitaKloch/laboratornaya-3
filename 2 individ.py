x = int(input("Введите 1 число: "))
y = int(input("Введите 2 число: "))
z = int(input("Введите 3 число: "))

if x < 0 or y < 0 or z < 0:
    print("Числа не должны быть отрицательными")
    exit(1)
elif x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("Все числа четные")
elif x % 2 == 0 and y % 2 == 0:
    print("Числа 1 и 2 - четные")
elif y % 2 == 0 and z % 2 == 0:
    print("Числа 2 и 3 - четные")
elif x % 2 == 0 and z % 2 == 0:
    print("Числа 1 и 3 - четные")
elif x % 2 ==0:
    print("Число 1 - четное")
elif y % 2 ==0:
    print("Число 2 - четное")
elif z % 2 ==0:
    print("Число 3 - четное")