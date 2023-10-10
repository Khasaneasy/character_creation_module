from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления \
квадратного корня из заданного числа'


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверка на отрицательность числа."""
    res = calculate_square_root(your_number)
    if your_number <= 0:
        return f"""Мы вычислили квадратный корень из введенного вами числа. \
Это будет: {0}"""
    else:
        return ((f"""Мы вычислили квадратный корень из введённого вами числа. \
Это будет: {res}"""))


print(message)
print(calc(25.5))
