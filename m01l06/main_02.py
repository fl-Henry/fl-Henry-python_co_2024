# #
# #
# #
# # #
# # # print(f"Hello, {name}!")
# # name = 'Alice'
# # print("Hello, " + name + "!")
# # print(f"Hello, {name}!")
# # print("Hello, {}!".format(name))
# # print("Hello, Alice!")
#
#
# def add(a: int, b=None):
#     # if b is None:
#     # if b:
#     #     ...
#     # else:
#     #     ...
#
#     return a, b
#
#
# result = add(3, 5)
# print(result)  # Output: 8


# def print_numbers(a, *args):
#     print(args)
#     print(type(args))
#
#     for number in args:
#         print(number)
#
# # print_numbers(1, 2, 3)       # Output: 1 2 3
# print_numbers(10, 20, 30, 40) # Output: 10 20 30 40


# def print_info(name, **kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_info(name="Alice", age=30, city="New York")

# x = 5
# b = 666
#
#
# def local_example():
#     def inner_example():
#         x = 66
#
#     x = 10  # Локальная переменная
#     print(x)
#     b = 555
#     print("b=", b)
#
#
# local_example()
# print(x)

#
# x = 20  # Глобальная переменная
#
# def modify_global(a):
#     # global x
#     x = a + 10
#     return x
#
#
# print(x)
# x = modify_global(x)
# print(x)



students = [
    {"id": 1, "name": "Alice", "age": 20, "grades": [85, 92, 78]},
    {"id": 2, "name": "Bob", "age": 22, "grades": [89, 94, 90]},
    {"id": 3, "name": "Charlie", "age": 21, "grades": [80, 85, 88]},
    {"id": 4, "name": "Diana", "age": 20, "grades": [70, 75, 80]},
    {"id": 5, "name": "Eve", "age": 23, "grades": [95, 88, 91]},
    {"id": 6, "name": "Frank", "age": 22, "grades": [65, 72, 68]},
    {"id": 7, "name": "Grace", "age": 21, "grades": [88, 90, 93]},
    {"id": 8, "name": "Hannah", "age": 20, "grades": [77, 84, 79]},
    {"id": 9, "name": "Ivy", "age": 24, "grades": [82, 89, 87]},
    {"id": 10, "name": "Jack", "age": 22, "grades": [92, 85, 88]}
]

result = best_student(students)
print(result)

result = best_student(students, 22)
print(result)

result = best_student(students)
print(result)

result = best_student(students)
print(result)

