# import pandas as pd
#
# # index = ['a', 'b', 'c', 'd']
# # series = pd.Series(
# #     [10, 20, 30.0, '40'],
# #     index=index
# # )
#
# # data = {'a': 10, 'b': 20, 'c': 30}
# # series = pd.Series(data)
# #
# # print(series)
#
# # series = pd.Series()
# #
# # print(series)
#
# # series = pd.Series(
# #     [10, 10,10,20, 20, 30, 40, 40],
# # )
# # # subset = series[1:3]
# #
# # # Логическая индексация
# # mask = (series > 20 + 10) & (True)
# # print(mask)
# # unique_values = series.unique()
# # print(unique_values)
# # counts = series.value_counts()
# # print(counts)
#
# # filtered_series = series[mask]
# #
# # print(filtered_series)
#
#
# # data = {'a': 10, 'b': 20, 'c': 30}
# # series = pd.Series(data)
# #
# # print(series)
# # print()
# # print(series['b'])
# # print(series.loc['b'])
# # print(series.iloc[1])
#
#
# # data = {5: 10, 6: 20, 7: 30}
# # series = pd.Series(data)
# #
# # print(series)
# # print()
# # print(series[6])
# # print(series.loc[6])
# # print(series.iloc[-1])
#
#
# import pandas as pd
#
# data1 = [10, 20, 30]
# data2 = [1, 2, 3]
# index = ['a', 'b', 'c']
#
# series1 = pd.Series(data1, index=index)
# # series2 = pd.Series(data2, index=index)
# #
# # # # Сложение двух Series
# # # result = series1 + series2
# # # print(result)
# #
# # # Умножение на скаляр
# # # result = series1 + 22
# # # print(result)
# #
# # total = series1.sum()
# # print(total)
#
# def square(x):
#     return x ** 2
#
#
# squared_series = series1.apply(square)
# print(squared_series)


import pandas as pd

# data = {
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [25, 30, 35],
#     'city': ['New York', 'Los Angeles', 'Chicago']
# }
#
# df = pd.DataFrame(data)
# print(df)

data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
    ['Charlie', 35, 'Chicago'],
]

df = pd.DataFrame(data, columns=['name', 'age', 'city'])
print(df)
print()
#
# # df.info()
# print(df.describe())

print(df.head(4))  # Вернет первые 5 строк
print(df.tail(4))

# ages = df['age']  # Вернет Series с возрастами
# print(ages)
#
# subset = df[['city', 'name']]  # Вернет DataFrame с выбранными столбцами
# print(subset)

# df = pd.DataFrame(columns=['name', 'age', 'city'])
# print(df)
# print()
# df = pd.DataFrame()
# print(df)