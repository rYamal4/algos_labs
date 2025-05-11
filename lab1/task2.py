def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

n = int(input("Введите n: "))
if is_prime(n):
    print("Число простое")
else:
    print("Число составное")