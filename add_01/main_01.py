# import random
#
#
# # age = int(input("Введите ваш возраст: "))
# # if age > 18:
# #     print("Вы совершеннолетний.")
# # elif age == 18:
# #     print("Вы только что стали совершеннолетним.")
# # else:
# #     print("Вы несовершеннолетний.")
#
#
# # arr = list(range(0, 10, 2))
# # print("последовательность", arr)
# #
# # for i in arr:
# #
# #     print("Элемент", i**2)
#
# # #
#
#
# # single_tuple = 1,
# # # single_tuple = (1)
# # print(single_tuple)
#
# # my_dict = {
# #     'name': 'Alice',
# #     'name1': ['s', 2],
# #     'age': 25,
# # }
#
# # print(my_dict.get('name', 'Bob'))
# # print(my_dict.get('name'))
# # print(my_dict['name'])
# #
# # dict2 = {
# #     'foo': 'bar',
# #     'foo2': 'bar2'
# # }
# # # my_dict['name'] = 'bob1'
# # # print(my_dict['name'])
# #
# # print(my_dict)
# # my_dict.update(dict2)
# # print(my_dict)
#
# # for key, value in my_dict.items():
# #     print("key:", key, "value:", value)
# #     if value == "Alice":
# #         print("Match")
#
#
# # for key in my_dict.keys():
# #     print("key:", key)
# # print()
# #
# # for value in my_dict.values():
# #     print("value:", value)
#
#
# lll = [1, 2, 3, 4, 4]
#
# print(lll)
# my_set = set(lll)
# print(my_set)

#
# import json
#
# data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# json_str = json.dumps(data, indent=4)
# # print(repr(data))
# print(data['name'])
# print(repr(json_str))
# # print(json_str)
# print(json_str[0])
#
# data2 = json.loads(json_str)
# print(data2)
# print(data2['name'])


def greet():
    return "Hello, world!"


def add(a, b):
    return a + b


def func1(a, b, operation='add'):
    x = 22
    print("2: x", x)
    if operation == "add":
        return a + b

    # print(1)

    if operation == "subtract":
        return a - b

#     print(2)


def print_numbers(*args):
    for number in args:
        print(number)


# result = greet()
# result = add(11, 22)
# result = func1(11, 22, 'subtract')
# result = func1(a=11, b=22, operation='subtract')
# print(result)


# print_numbers(1, 2, 3)       # Output: 1 2 3
# print()
# print_numbers(10, 20, 30, 40) # Output: 10 20 30 40


# a = 55
# print("1: a", a)
# result = func1(11, 22, 'subtract')
# print("3: a", a)
# # print(result)


# x = 55
# print("1: x", x)
# result = func1(11, 22, 'subtract')
# print("3: x", x)
# # print(result)


