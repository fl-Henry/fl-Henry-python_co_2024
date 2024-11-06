import pandas as pd
df1 = pd.DataFrame({'A': [1, 2]}, index=['a', 'b'])
df2 = pd.DataFrame({'B': [3, 4]}, index=['b', 'c'])

# Выравнивание по индексу
df1_aligned, df2_aligned = df1.align(df2, fill_value=0)

print(df1_aligned)
print(df2_aligned)
