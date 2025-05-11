k = int(input("Введите количество тактов: "))

red = 1
green = 0

for _ in range(k):
    new_green = red
    red = green
    green += new_green

print(red + green)