L1 = []
print("Введите действительные числа для первой очереди L1")
while True:
    s = input()
    if s == "":
        break
    try:
        x = float(s)
        L1.append(x)
    except ValueError:
        print(f"'{s}' это не число")
        exit()

L2 = []
print("Введите действительные числа для второй очереди L2")
while True:
    s = input()
    if s == "":
        break
    try:
        x = float(s)
        L2.append(x)
    except ValueError:
        print(f"'{s}' это не число")
        exit()

S = []
while L1:
    x = L1.pop()
    if x > 0:
        S.append(x)
while L2:
    x = L2.pop()
    if x > 0:
        S.append(x)

print(f"Стек положительных элементов: {S}")
if S:
    print(f"Количество элементов в стеке: {len(S)}")
else:
    print("Положительных элементов нет")
