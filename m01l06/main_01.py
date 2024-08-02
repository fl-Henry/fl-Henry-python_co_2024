# # # # # def greet():
# # # # #     print("Hello, world!")
# # # # #
# # # # #
# # # # # for i in range(9):
# # # # #     greet()
# # # #
# # # #
# # # # # def greet(name, age: int):
# # # # #     age += 1
# # # # #     print(f"Hello, {name}, {age}!")
# # # # #
# # # # #
# # # # # greet('My_name', 25)
# # # # # greet(
# # # # #     age=25,
# # # # #     name="My_name"
# # # # # )
# # # # # # print(age)  # Ошибка
# # # #
# # # # #
# # # # # def add(a, b):
# # # # #     if a > b:
# # # # #         return a - b
# # # # #     else:
# # # # #         return a + b
# # # # #
# # # # #
# # # # # result = add(7, 3)
# # # # # print("result", result)
# # # #
# # # #
# # # # # def greet(name):
# # # # #     print(f"Hello, {name}!")
# # # # #
# # # # #
# # # # # result = greet('name')
# # # # # print("result", result)
# # # #
# # # #
# # # # # def greet(name="Andrey"):
# # # # #     print(f"Hello, {name}!")
# # # # #
# # # # #
# # # # # greet('name')
# # # # # greet()
# # # #
# # # #
# # # # def example(a, b):
# # # #     return a + b
# # # #
# # # #
# # # # x = example(1, b=8)
# # # # print(x)
# # #
# # #
# # def print_numbers(a, b, *args):
# #     print(args)
# #     print(type(args))
# #     for number in args:
# #         print(number, number, number, number, number, number, number)
# #
# #
# # print_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # # print_numbers(1, 2, 3, 4, 5, 6)
# #
# #
# # # key word args
# # # def print_info(b=4, **kwargs):
# # #     print(b, kwargs)
# # #     kwargs.update({'name_2': '<NAME>'})
# # #     for key, value in kwargs.items():
# # #         print(f"{key}: {value}")
# # #
# # #
# # # print_info(b=6, name="Alice", age=30, city="New York")
#
# x = 5
# c = 666
#
#
# def local_example():
#     x = 10  # Локальная переменная
#
#     print("local c =", c)
#     # global c
#     # c = 123
#     # print("local c =", c)
#
#     print("local x =", x)
#
#     return x
#
#
# # local_example()
# print("global x =", x)
# c = local_example()
# print("global c =", c)


# def print_numbers(args: list):
#     print(args)
#     print(type(args))
#     for number in args:
#         print(number, number, number, number, number, number, number)
#
#
# print_numbers((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# # print_numbers(1, 2, 3, 4, 5, 6)


def local_example():

    def inner_func():
        c = 3
        d = 4
        print("a =", a)

    a = 1
    b = 2
    inner_func()
    # print(c)


local_example()

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

result = best_student(students)
print(result)

result = best_student(students)
print(result)

result = best_student(students)
print(result)
