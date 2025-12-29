'''
4. Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
'''

import time, random

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Затраченое время: {end - start:.6f} сек")
        return result
    return wrapper

@timer

def matrix_creator(a, b, n, m):
    return [[random.randint(a, b) for _ in range(m)] for _ in range(n)]

a = 0
b = 10
n = int(input("Укажите высоту матрицы: "))
m = int(input("Укажите ширину матрицы: "))

matrix = matrix_creator(a, b, n, m)

for row in matrix:
    print(row)