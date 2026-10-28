n = int(input("Введите количество чисел "))
a = list(map(float, input("Введите числа: ").split()))

ok = True

for i in range(n):
    if a[i] > 0:
        for j in range(i + 1, n):
            if a[i] < 0 and a[i] > abs(a[j]):
                ok = False
print(ok)
