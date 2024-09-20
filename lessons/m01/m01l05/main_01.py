# # # my_dict = {
# # #     'name': 'Alice1',
# # #     'age': 25
# # # }
# # #
# # # # for key, value in my_dict.keys():
# # # #     print(key, value)
# # #
# # # # print(my_dict['name1'])
# # #
# # # my_dict.update(
# # #     {
# # #         'name': 'Alice2',
# # #         'phone_number': 123456
# # #     }
# # # )
# # #
# # # print(my_dict)
# #
# #
# # json_1 = [
# #     {
# #         "Name": "<NAME>"
# #     },
# #     {
# #         "Name": "<NAME>",
# #         "bool_1": True,
# #         "x": None,
# #         'y': None,
# #     },
# # ]
# #
# # web_data = """
# # [
# #     {
# #         "Name": "<NAME>"
# #     },
# #     {
# #         "Name": "<NAME>",
# #         "bool_1": True,
# #         "x": None,
# #         'y': None,
# #     },
# # ]"""
# #
# # print(web_data[1])
# # print(json_1[1])
# #
# # json_2 = {
# #     "Name": [
# #         '1', '2'
# #     ]
# # }
#
#
# import json
#
# # data = [{'name': 'Alice', 'age': [30, 31, 32], 'city': 'New York'}]
# # json_str = json.dumps(data, indent=4)
# # print(json_str)
#
# json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
# data = json.loads(json_str)
# print(json_str)
# print(data)
# print(data['name'])


# even_squares = [x**2 for x in range(10) if x % 2 == 0]
#
# print(list(range(10)))
# print(even_squares)
# # Результат: [0, 4, 16, 36, 64]



# words = ['hello', 'world', 'python', 'is', 'fun']
# long_words = [word for word in words if len(word) > 3]
# print(long_words)
# # 'hello', 'world', 'python'

#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filtered = [x for x in numbers if x % 2 == 0 if x > 5]
# print(filtered)
#
# # [6, 8]
# # [6, 8] (and)
# # [2, 4, 6, 7, 8, 9] (or)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    elem
    for row in matrix
    for elem in row
]