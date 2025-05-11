S = []
print("Введите действительные числа")
while True:
    s = input()
    if s == "":
        break
    try:
        x = float(s)
        S.append(x)
    except ValueError:
        print(f"'{s}' это не число")
        exit()
print(f"Список действительных чисел: {S}")
S = [x for x in S if x % 2 != 0]
print(f"Список действительных чисел с удаленными четными числами: {S}")
p = 1
for x in S:
    if x != 0:
        p *= x
if len(S) > 0:
    print(f"Произведение ненулевых нечетных чисел: {p}")
else:
    print("Ненулевых нечетных чисел нет")