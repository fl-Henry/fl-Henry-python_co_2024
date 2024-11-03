import pandas as pd

# Создаем два DataFrame с пропусками
df1 = pd.DataFrame({'A': [1, 2, None], 'B': [None, 5, 6]})
df2 = pd.DataFrame({'A': [22, None, 3, 44], 'B': [4, None, None, 55]})

# Объединение с заполнением пропусков
df = df1.combine_first(df2)

print(df1)
print()
print(df2)
print()


print(df)
