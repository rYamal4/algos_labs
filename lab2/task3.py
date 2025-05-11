def create_deque():
    d = []
    print("Введите действительные числа для дека d")
    while True:
        s = input()
        if s == "":
            break
        try:
            x = float(s)
            d.append(x)
        except ValueError:
            print(f"'{s}' это не число")
            exit()
    return d

def print_deque(d):
    print(f"Дек после обработки: {d}")

def main():
    d = create_deque()
    processed = []
    while d:
        x = d.pop(0)
        processed.append(x)
        if x < 0:
            processed.append(abs(x))
    print_deque(processed)

if __name__ == "__main__":
    main()
