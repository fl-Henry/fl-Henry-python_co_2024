import pandas as pd
#
# # # Создаем DataFrame
# # data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
# #         'Age': [30, 25, 35, 30],
# #         'Age1': [40, 30, 35, 25]
# #         }
# # df = pd.DataFrame(data)
# # print(df)
# #
# # # Сортируем по возрасту
# # df.sort_values(by=['Age', 'Age1'], inplace=True, ascending=False)
# # # print(sorted_df)
# # print()
# # print(df)
# #
# # # print(sorted_df.iloc[-1])
# #
# # # Сортируем по индексу
# # df.sort_index(inplace=True, ascending=False)
# # print()
# # print(df)
#
#
# import pandas as pd
#
# # Создаем DataFrame с нестандартным форматом дат
# data = {'date_string': ['04/11/2023', '05/11/2023', '06/11/2023']}
# df = pd.DataFrame(data)
#
#
# print(df)
# print()
# # df.info()
# # print()
#
#
# # Преобразуем с указанием формата
# df['date'] = pd.to_datetime(df['date_string'], format='%d/%m/%Y', errors='coerce')
# print(df)
# print()
# # df.info()
#
# # # Извлекаем компоненты даты
# # df['year'] = df['date'].dt.year
# # df['month'] = df['date'].dt.month
# # df['day'] = df['date'].dt.day
# #
# # # Извлекаем день недели (0 - понедельник, 6 - воскресенье)
# # df['day_of_week'] = df['date'].dt.dayofweek
# #
# # # Извлекаем номер квартала
# # df['quarter'] = df['date'].dt.quarter
# #
# # # Создаем столбец, который содержит дату в формате 'день.месяц.год'
# # df['formatted_date'] = df['date'].dt.strftime('%Y %m %d')
# #
# # # Создаем новый столбец, который показывает, является ли дата выходным
# # df['is_weekend'] = df['day_of_week'].isin([5, 6])  # 5 - суббота, 6 - воскресенье
#
# # Сложение: добавляем 10 дней
# df['new_date'] = df['date'] + pd.Timedelta(days=10)
#
# # Вычитание: вычитаем 5 дней
# df['previous_date'] = df['date'] - pd.Timedelta(days=5)
#
# print(df)
# print()
# df.info()

# # Создаем DataFrame с датами окончания задач
# data = {'start_date': ['2023-11-01 14:22:30', '2023-11-02 16:22:30'],
#         'end_date': ['2023-11-10', '2023-11-07']}
# df = pd.DataFrame(data)
#
# print(df)
# print()
#
# # Преобразуем строки в даты
# df['start_date'] = pd.to_datetime(df['start_date'])
# df['end_date'] = pd.to_datetime(df['end_date'])
#
# # Вычисляем разницу между датами
# df['duration'] = df['end_date'] - df['start_date']
#
# print(df)
# print()


# Создаем DataFrame с датами и значениями
data = {
    'date': ['2023-11-01', '2023-11-10', '2023-12-01', '2023-11-02'],
    'value': [100, 150, 200, 250]
}
df = pd.DataFrame(data)

# Преобразуем строки в даты
df['date'] = pd.to_datetime(df['date'])
print(df)
print()

# Фильтруем данные по дате
# import datetime
# start_date = datetime.datetime.fromisoformat('2023-11-01')
# end_date = datetime.datetime.fromisoformat('2023-11-30')

# start_date = '2023-11-01'
# end_date = '2023-11-30'
# filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
#
# print(filtered_df)
# print()

df.sort_values(by='date', inplace=True)
print(df)
print()