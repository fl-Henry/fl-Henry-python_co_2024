# # import csv
# #
# # with open('output.csv', mode='r', newline='', encoding='utf-8') as file:
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
#     ['Bob1', 25, 'Data Scientist'],
#     ['Charlie', 35, 'Teacher']
# ]
#
# # Открытие файла для записи
# with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
#     # Создание объекта writer
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#     #
#     # # Запись данных построчно
#     # writer.writerows(data)
#
#
#     # Запись заголовка
#     writer.writerow(['Name', 'Age', 'Occupation'])
#
#     # Запись данных
#     writer.writerow(['Alice', 30, 'Engineer'])
#     writer.writerow(['Bob2', 25, 'Data Scientist'])
#     writer.writerow(['Charlie', 35, 'Teacher'])
#
# with open('output.csv', mode='a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#     #
#     # # Запись данных построчно
#     # writer.writerows(data)
#
#     # Запись заголовка
#     writer.writerow(['Name', 'Age', 'Occupation'])
#
#     # Запись данных
#     writer.writerow(['Alice', 30, 'Engineer'])
#     writer.writerow(['Bob2', 25, 'Data Scientist'])
#     writer.writerow(['Charlie', 35, 'Teacher'])
import json

#
import pandas as pd
#
# # pd.set_option('display.max_rows', None)
#
# # Загрузка CSV файла в DataFrame
# df = pd.read_csv('output.csv')
#
# # Просмотр DataFrame
# print(df)


# Создание DataFrame из JSON объекта
# df = pd.DataFrame(
#     {
#         'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [30, 25, 35],
#         'Occupation': ['Engineer', 'Data Scientist', 'Teacher']
#     }
# )

df_data = [
    {
        'Name': 'Alice',
        'Age': 30,
        'Occupation': 'Engineer',
        'Occupation1': 'Engineer',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },
    {
        'Name': 'Bob',
        'Age': 25,
        'Occupation': 'Data Scientist',
    },

]

df = pd.DataFrame(df_data)

new_row = {
    'Name': 'Bob2',
    'Age': 252,
    'Occupation': 'Data Scientist2',
}

df = pd.concat([df, pd.DataFrame([new_row], index=[3])], ignore_index=True)
# print(df)


# print(df.head())
# print()
# print(df.head(10))  # Показать первые 10 строк
#
# print(df.tail())
# print()
# print(df.tail(10))  # Показать последние 10 строк

# print(df.info())

# import pandas as pd
#
# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob'],
#     'Age': [30, 25]
# })
#
# # Запись DataFrame в CSV файл
# df.to_csv('output.csv', index=False)


import pandas as pd
#
# # pd.set_option('display.max_rows', None)
#
# Загрузка CSV файла в DataFrame
df = pd.read_csv('output.csv')

# Просмотр DataFrame
import json
json_data = json.loads(df.to_json(orient="records"))

for x in json_data:
    print(x)
    print(x.get('Name'))