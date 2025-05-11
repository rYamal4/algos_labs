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
S = [x for x in S if x % 2 != 0]
p = 1
for x in S:
    if x != 0:
        p *= x
print(f"Список действительных чисел: {S}")
if len(S) > 0:
    print(f"Произведение ненулевых нечетных чисел: {p}")
else:
    print("Ненулевых нечетных чисел нет")