import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 11, 12, 13, 14]
})

# Построение интерактивной тепловой карты
fig = px.scatter(df, x='X', y='Y', title='Диаграмма рассеяния', hover_data={'X': False})

fig.show()