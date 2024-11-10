from math import sqrt, fabs, log, cos, sin

# Введення початкових даних
a = 1.0  # Початок інтервалу
b = 10.0  # Кінець інтервалу
h = 0.15  # Крок табулювання

# Функція для обчислення значення f(x)
def f(x):
    if x < 3:
        if x <= 0:
            raise ValueError("x має бути більше 0 для обчислення log(x)")
        return sqrt(x**3 + log(x))
    elif x >= 3 and x < 6:
        return fabs(log(x))**5
    else:
        return (cos(x))**x

# Табулювання функції
x = a
print(f"Табулювання функції на інтервалі [{a}, {b}] з кроком {h}:")
while x <= b:
    try:
        print(f"f({x:.2f}) = {f(x):.5f}")
    except ValueError as e:
        print(f"f({x:.2f}) = неможливо обчислити ({e})")
    x += h 
    x = round(x, 2)
    print(x)


# Друга частина
a = 0.0  # Початок інтервалу
b = 1.0  # Кінець інтервалу
h = 0.05  # Крок табулювання
epsilon = 1e-5  # Похибка

# Функція для обчислення значення f(x)
def f(x):
    sum_result = 0.0
    n = 1
    term = n*x**2 * sin(n*x)
    max_iterations = 1000  # Максимальна кількість ітерацій
    try:
        while abs(term) > epsilon and:  # Поки доданок більший за похибку
            term = n * x**2 * sin(n * x)
            sum_result += term
            n += 1
    except OverflowError as oe:
        print(f"Переповнення на ітерації {n}: {oe}")
    return x + sum_result

# Табулювання функції
x = a
print(f"Табулювання функції на інтервалі [{a}, {b}] з кроком {h}:")
while x <= b:
    try:
        print(f"f({x:.2f}) = {f(x):.5f}")
    except ValueError as e:
        print(f"f({x:.2f}) = неможливо обчислити ({e})")
    x += h
    x = round(x, 2)
    print(x)