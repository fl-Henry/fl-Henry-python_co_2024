import numpy as np
# #
# # # random_array = np.random.rand(2, 3)  # 2 строки, 3 столбца
# # # print(random_array)
# # # print()
# # #
# # # random_normal_array = np.random.randn(2, 3)
# # # print(random_normal_array)
# # # print()
# #
# # array = np.random.randint(20, 40, (4, 4))  # 2 строки, 3 столбца
# # print(array)
# # print()
# # # slice_array = array[1:, 1]  # Извлечение элементов с 1 по 3
# # # print(slice_array)  # Вывод: [20 30 40]
# #
# # # print(array[array > 30])  # Вывод: [40 50]
# # aa = array[[0, 1, 2, -1]]
# # print(aa)
# # print()
# # print(aa[:, [0, -1]])
# #
# # A = np.array()
# # B = np.array()
# #
# # np.matmul()
#
# # array = np.array([1, 2, 5, 4, 3, 1, 3])
# # median_value = np.median(array)
# # print(median_value)
# #
# # range_value = np.ptp(array)
# # print(range_value)
# #
# # unique_elements, counts = np.unique(array, return_counts=True)
# # print(unique_elements)
# # print(counts)
#
# # array_to_tile = np.array([[1, 2], [3, 4]])
# # print(array_to_tile)
# # print()
# # tiled_array = np.tile(array_to_tile, (2, 3))  # Повторить 2 раза по строкам и 3 раза по столбцам
# # print(tiled_array)
# #
# # array1 = np.array([[1], [2], [3]])
# # array2 = np.array([[4], [5], [6]])
# # combined_array = np.concatenate((array1, array2))
# # print(combined_array)  # Вывод: [1 2 3 4 5 6]
# # # Вывод:
# # # [[1 4]
# # #  [2 5]
# # #  [3 6]]
# #
# # array1 = np.array([[1], [2], [3]])
# # array2 = np.array([[4], [5], [6]])
# # horizontal_stacked_array = np.hstack((array1, array2))
# # print(horizontal_stacked_array)
# # # Вывод:
# # # [[1 4]
# # #  [2 5]
# # #  [3 6]]
#
# array1 = np.array(['a', 'b', 'c'])
# array2 = np.array([1, 2, 3])
# print(np.strings.multiply(array1, 2))
# print(array2.sum())
# # print([1, 2, 3].sum())

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