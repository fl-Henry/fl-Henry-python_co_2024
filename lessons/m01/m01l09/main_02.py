# # import csv
# #
# # # Открытие файла для чтения
# # with open('output.csv', mode='r', newline='', encoding="utf-8") as file:
# #     # Создание объекта reader
# #     reader = csv.reader(file)
# #
# #     # Чтение данных построчно
# #     for row in reader:
# #         print(row)
# #
# # import csv
# #
# # with open('output.csv', mode='r', newline='', encoding="utf-8") as file:
# #     reader = csv.reader(file)
# #
# #     # Пропуск заголовка
# #     headers = next(reader)
# #     print("Заголовки:", headers)
# #
# #     for row in reader:
# #         print(row)
#
#
# import csv
#
# # Данные для записи
# data = [
#     ['Name', 'Age', 'Occupation'],
#     ['Alice', 30, 'Engineer'],
#     ['Bob', 25, 'Data Scientist'],
#     ['Charlie', 35, 'Teacher']
# ]
#
# # Открытие файла для записи
# with open('output.csv', mode='a', newline='', encoding="utf-8") as file:
#     # Создание объекта writer
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#
#     # # Запись данных построчно
#     # writer.writerows(data)
#
#     # Запись данных
#     writer.writerow(['Alice1', 32, 'Engineer1'])
import json

# import pandas as pd
# print(pd.__version__)

import pandas as pd

# Загрузка CSV файла в DataFrame
# df = pd.read_csv('output.csv')

# # Просмотр DataFrame
# print(df)

# json_data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [30, 25, 35],
#     'Occupation': ['Engineer', 'Data Scientist', 'Teacher']
# }
#
# json_data = [
#     {
#         "col 1": "a",
#         "col 2": "b"
#     },
#     {
#         "col 1": "c",
#         "col 2": "d"
#     }
# ]
#
# # Создание DataFrame из JSON объекта
# df = pd.DataFrame(json_data, index=[1, 2])
#
# print(df)
#
# # df.to_csv('output.csv', index=False)  # index=False исключает запись индекса в файл




df = pd.read_csv('output.csv')

json_data = df.to_json(orient='records')

print(df)
print()
print(json.dumps(json.loads(json_data), indent=4))