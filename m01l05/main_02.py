# my_dict = {
#     'name': 'Alice',
#     'age': 25,
#     # 'age1': 25,
#     'dict2': {
#         'age2': 22,
#     },
# }
#
# # print(my_dict['age1'])
# # print(my_dict.get('age1', 18))
#
# my_dict.update(
#     {
#         'last_name': "Alice last name",
#         'age': 26,
#     }
# )
# # print(my_dict)
#
# # for key, value in my_dict.items():
# #     print(key, value)
#
#
# # for value in my_dict.values():
# #     print(value)
#
# # for key in my_dict.keys():
# #     print(key)
#
#
# # a = [1, 2, 2, 5]
# # a = list(set(a))
# # print(a)
#
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# #
# # union_set = set1 | set2
# # intersection_set = set1 & set2
# # difference_set = set1 - set2
# #
# # print(union_set)
# # print(intersection_set)
# # print(difference_set)
#
#
# test_json = [
#     {
#         "Name": "<NAME>"
#     },
#     {
#         "Name": "<NAME>",
#         "bool_1": True,
#         "x": None,
#         'y': None,
#     },
# ]
#
# api_json = """
# [
#     {
#         "Name": "<NAME>"
#     },
#     {
#         "Name": "<NAME>",
#         "bool_1": true,
#         "x": null,
#         "y": null
#     }
# ]
# """
#
# print(test_json[1])
# print(api_json[1])
#

# import json
#
# data = [{'name': 'Alice', 'age': [1, 2], 'city': None, 'city1': True,}]
# json_str = json.dumps(data, indent=4)
# print(type(json_str))  # str
# print(json_str)  # str
#
# data = json.loads(json_str)
# print(type(data))  # JSON
# print(data)  # JSON

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
even_numbers = [
    elem
    for row in matrix
    for elem in row
    if (
            elem % 2 == 0
    )
    if elem // 3 == 0
]
