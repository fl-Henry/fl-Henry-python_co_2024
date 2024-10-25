import numpy as np
# print(np.__version__)

# my_list = [1, 2, 3, 4, 5]
# my_array = np.array(my_list)
# print(my_array)
# print(my_array.dtype)
# print(my_list)


# array_2d = [[1, 2, 3], [4, 5, 6]]
# my_2d_array = np.array(array_2d)
# print(my_2d_array)
# print(array_2d)

# zeros_array = np.ones((3, 4))  # 3 строки, 4 столбца
# print(zeros_array)
# print(zeros_array.dtype)


# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# sum_array = array1 + array2
# print(sum_array)
#
# print(np.mean(array1))  # Среднее значение
# print(np.sum(array1))   # Сумма всех элементов


# array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(array1[::3])
# print(array1[::-1])


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# print(matrix[0, 1])  # Элемент в первой строке и втором столбце
# print(matrix[2, 2])  # Элемент в третьей строке и третьем столбце

sub_matrix = matrix[1:, 1:]  # Все строки, начиная со второй, и все столбцы, начиная со второго
print(sub_matrix)