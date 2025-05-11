A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

if A + B == C + D or A + C == B + D or A + D == B + C:
    print("Да")
else:
    print("Нет")