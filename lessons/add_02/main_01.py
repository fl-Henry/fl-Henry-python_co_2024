# string1 = "Hello, World!"
# if True:
#     string2 = """Str1
#     str2
#     """
# string3 = "Str1 \n str2"
#
# print("string1", string1)
# print("string2", string2)
# print("string3", string3)
import json

# string1 = "Hello, World!!!!\nWorld"

# print(string1)
# print(string1.upper())
# print(string1.lower())

# print(string1.replace("!", ""))
# print(string1.replace("World", ""))
# print(string1.replace("!", "?"))
# print(string1.replace("\n", " "))
# string1 = "Hello, World; World"
# print(string1.split('; '))

# strings = ['Hello, World', 'World', 'Hello']
# print('; '.join(strings))

# stripped_string = "   \nHello,      World!   ".strip()
# print(stripped_string)

# name = "Alice1"
# formatted_string = "Hello, {1:05d}, {greeting_name}!".format(0, 25, greeting_name=name)  # 'Hello, Alice!'
# print(formatted_string)

# raw_string = r"C:\Users\Name\Documents\File.txt\n"
# raw_string = r"File.txt\nd"
# print(raw_string)  # 'C:\\Users\\Name\\Documents\\File.txt'


# import csv
#
# # Открытие файла для чтения
# with open('test.csv', mode='r') as file:
#     # Создание объекта reader
#     reader = csv.reader(file)
#
#     # Чтение данных построчно
#     for row in reader:
#         # print(row)
#         print(row[1])

# import csv
#
# # Данные для записи
# data = [
#     ['Name', 'Age', 'Occupation'],
#     ['Alice', 30, 'Engineer'],
#     ['Bob', 25, 'Data, Scientist'],
#     ['Charlie', 35, 'Teacher']
# ]
#
# # Открытие файла для записи
# with open('test.csv', mode='w', newline='') as file:
#     # Создание объекта writer
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#
#     # Запись данных построчно
#     writer.writerows(data)

import pandas as pd
#
# # Загрузка CSV файла в DataFrame
# df = pd.read_csv('test.csv')
#
# # Просмотр DataFrame
# # print(json.loads(df.to_json(orient='records'))[0]['Name'])

# json_data = [{'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'}, {'Name': 'Bob', 'Age': 25, 'Occupation': 'Data, Scientist'}, {'Name': 'Charlie', 'Age': 35, 'Occupation': 'Teacher'}]
#
#
# df = pd.DataFrame(json_data)
#
# # Запись DataFrame в CSV файл
# df.to_csv('test.csv', index=False)
#
#
# def greet(name):
#     return f"Hello, {name}!"
#
#
# def greet2(name):
#     return f"Hi, {name}!"
#
#
# def call_function(func, value):
#     return func(value)
#
#
# print(call_function(greet, "Alice"))
# print(call_function(greet2, "Alice"))


#
# from functools import reduce
#
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * 2 * y, numbers)
# print(product)  # Вывод: 24

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__param = [width, height]

    def __call__(self, *args, **kwargs):
        pass

    def area(self):
        # print(self.__param)
        return self.width * self.height

    def __str__(self):
        return f"{self.width}x{self.height}, area = "


rect1 = Rectangle(2, 5)
# rect2 = Rectangle(5, 7)
# rect3 = Rectangle(3, 11)
# print(f"Прямоугольник {rect1.height}x{rect1.width} имеет площадь {rect1.area()}")
# print(f"Прямоугольник {rect2.height}x{rect2.width} имеет площадь {rect2.area()}")
# print(f"Прямоугольник {rect3.height}x{rect3.width} имеет площадь {rect3.area()}")

print(rect1)
rect1 = Rectangle(4, 5)
print(rect1)
# print(rect1.area())
# print(rect1.__param)