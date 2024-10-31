import numpy as np
#
# # Массив 1 (размер: (2, 3))
# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
#
# # Массив 2 (размер: (3,))
# b = np.array([10, 20, 30])
#
# # Broadcasting
# result = a + b
# print(result)

# # Массив 1 (размер: (2, 3))
# c = np.array([[1, 2, 3],
#               [4, 5, 6]])
#
# # Массив 2 (размер: (2, 2))
# d = np.array([[10],
#               [30]])
#
# # Попытка сложения
# try:
#     result = c + d
#     print(result)
# except ValueError as e:
#     print("Ошибка:", e)


# # Массив 1 (размер: (3,))
# e = np.array([1, 2, 3, 4, 5])
#
# # Массив 2 (размер: (2, 1))
# f = np.array([['1'],
#               ['2'],
#               ['3'],
#               ['4'],
#               ['5']])
#
# # Сложение
# # result = e + f
# result = np.strings.multiply(f, e)
# print(result)

# import numpy as np
#
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])
# A_T = A.T
# print(A_T)
#
# print(np.transpose(A, axes=[]))

# A = np.array([
#     [1, 2],
#     [3, 4]
# ])
# B = np.array([
#     [2, 3],
#     [4, 5]
# ])
#
# result = np.multiply(A, B)
# print(result)
# """
# [[ 2  6]
#  [12 20]]
# """
#
# C = A @ B
# print(C)

# 
# A = np.array([[1, 2, 3],
#               [4, 5, 6]])  # Размер: (2, 3)
# 
# B = np.array([[7, 8],
#               [9, 10],
#               [11, 12]])  # Размер: (3, 2)
# 
# C = A @ B  # или np.dot(A, B)
# print(C)

import time

# Создание большой матрицы
A = np.random.rand(1000, 1000)

# Векторизация
start_time = time.time()
result_vectorized = np.square(A)
end_time = time.time()
print("Векторизация время:", end_time - start_time)

# Цикл Python
result_loop = np.empty_like(A)
start_time = time.time()
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        result_loop[i, j] = A[i, j] ** 2
end_time = time.time()
print("Цикл Python время:", end_time - start_time)