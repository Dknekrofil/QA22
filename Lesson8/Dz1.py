import random

def matrix_creator(a, b, n, m):
    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(a, b))
        matrix.append(row)

    return matrix

def find_min_max(matrix):
    min_value = matrix[0][0]
    max_value = matrix[0][0]

    min_pos = (1, 1)
    max_pos = (1, 1)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_pos = (i + 1, j + 1)

            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_pos = (i + 1, j + 1)

    return min_value, min_pos, max_value, max_pos

def summa(matrix):
    summa_matrix = 0

    for i in matrix:
        for j in i:
            summa_matrix += j

    stolbec = len(matrix[0])

    stolbec_summa = [0] * stolbec

    for j in range(stolbec):
        for i in range(len(matrix)):
            stolbec_summa[j] += matrix[i][j]

    return summa_matrix, stolbec_summa

def stolbec_s_H(matrix, H):
    stolbec = len(matrix[0])

    s_H = []
    bez_H = []

    for j in range(stolbec):
        found = False

        for i in range(len(matrix)):
            if matrix[i][j] == H:
                found = True
                break

        if found:
            s_H.append(j + 1)
        else:
            bez_H.append(j + 1)

    return s_H, bez_H

def diagonal_summa(matrix):
    skolko_stroc = len(matrix)
    skolko_stolbcov = len(matrix[0])

    firs_diag_summa = 0
    secondary_diag_summa = 0

    for i in range(min(skolko_stroc, skolko_stolbcov)):
        firs_diag_summa += matrix[i][i]
        secondary_diag_summa += matrix[i][skolko_stolbcov - 1 - i]

    return firs_diag_summa, secondary_diag_summa

a = int(input("Укажите 1й диапазон рандомных чисел: "))
b = int(input("Укажите 2й диапазон рандомных чисел: "))
n = int(input("Укажите высоту матрицы: "))
m = int(input("Укажите ширину матрицы: "))
H = int(input("Введите число H: "))


if a > b:
    a, b = b, a

matrix = matrix_creator(a, b, n, m)

for row in matrix:
    print(row)

min_value, min_pos, max_value, max_pos = find_min_max(matrix)

print("Минимальное значение:", min_value)
print("Индекс минимума (строка, столбец):", min_pos)
print("Максимальное значение:", max_value)
print("Индекс максимума (строка, столбец):", max_pos)

summa_matrix, stolbec_summa = summa(matrix)

print("Общая сумма элементов:", summa_matrix)

for j in range(len(stolbec_summa)):
    procent = (stolbec_summa[j] / summa_matrix) * 100
    print(f"Столбец {j + 1}: сумма = {stolbec_summa[j]}, доля = {procent:.2f}%")

s_H, bez_H = stolbec_s_H(matrix, H)

print("Столбцы, содержащие число H:", s_H)
print("Столбцы, не содержащие число H:", bez_H)

firs_diag_sum, secondary_diag_sum = diagonal_summa(matrix)

print("Сумма главной диагонали:", firs_diag_sum)
print("Сумма побочной диагонали:", secondary_diag_sum)