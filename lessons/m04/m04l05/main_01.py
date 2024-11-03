import pandas as pd
import json


# Создаем два DataFrame с пропусками
df = pd.DataFrame({'A': [1, '2s', None], 'B': [None, 5, 6], 'C': [4, None, 22]})

print(df)

# df.to_json('data.json', orient='records')

# "split", "records", "index", "table", "columns", "values"

data_json = df.to_json()
print("orient=''")
print(json.dumps(json.loads(data_json), indent=4))
print()

data_json = df.to_json(orient='split')
print("orient='split'")
print(json.dumps(json.loads(data_json), indent=4))
print()

data_json = df.to_json(orient='records')
print("orient='records'")
print(json.dumps(json.loads(data_json), indent=4))
print()

data_json = df.to_json(orient='index')
print("orient='index'")
print(json.dumps(json.loads(data_json), indent=4))
print()

data_json = df.to_json(orient='table')
print("orient='table'")
print(json.dumps(json.loads(data_json), indent=4))
print()

data_json = df.to_json(orient='columns')
print("orient='columns'")
print(json.dumps(json.loads(data_json), indent=4))
print()

data_json = df.to_json(orient='values')
print("orient='values'")
print(json.dumps(json.loads(data_json), indent=4))
print()