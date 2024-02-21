def upper(num):
    for i in range(1, num + 1):
        print(f'{" " * (num - i)}{"* " * i}')


def lower(num):
    for row in range(num - 1, 0, -1):
        print(f"{' ' * (num - row)}{'* ' * row}")


def print_rhombus(num):
    upper(num)
    lower(num)


n = int(input())

print_rhombus(n)
