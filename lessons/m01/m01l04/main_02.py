import random

# var1 = 1
# var2 = 2
#
# if False:
#     # действия
#     var1 = 12
#     var2 = 13
#
# print(var1, var2)


# var1 = "Hello"
# var1 = "World"
# var1 = "Hello World"
#
# var1 = input("Enter a word: ")
#
# # var1 = int(var1)
# # var1 = float(var1)
# # print(type(var1))
#
# if var1 == "World":
#     print('var1 == "World"')
#
# if var1 == "Hello":
#     print('var1 == "Hello"')
#
# else:
#     print('var1 != "Hello" and var1 != "World"')
#     print('var1', var1)



# for i in [1, 2, 'String', 4, 5]:
#     print("i = ", i)


# var2 = range(start, stop, step)
# var2 = range(0, 9, 2)
# print(list(var2))

# var2 = range(20)
# print(list(var2))


# for i in range(5):
#     print("i = ", i)

# var3 = random.randint(нижняя_граница, верхняя_граница)
# var3 = random.randint(4, 8)
# print(var3)

# for i in range(random.randint(3, 6)):
#     print("i = ", i)


# while True:
#     # действия
#     print("while")

# while True:
#     # действия
#     print("while")
#     for i in range(random.randint(3, 6)):
#         print("i = ", i)
#         break
#     break

possible_chars = 'abcdefghijklmnopqrstuvwxyz'

index = random.randint(0, len(possible_chars) - 1)
print(possible_chars[index])