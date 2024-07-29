import random
#
# # for i in 'abcdefghij':
# #     print(i)
#
# #
# # print(list(range(1, 4)))
# #
# #
# # counter = range(1, 7, 2)
# # print(list(counter))
# #
# # for i in range(1, 4):
# #     print("loop #", i)
# #
# # print()
# # for i in range(1, 4):
# #     rand_int = random.randint(1, 3)
# #     print("rand_int = ", rand_int)
# #     # random.random()  # [0, 1] float
#
#
# # l1 = [54, 26, 93, 17, 77, 31, 44]
# #
# # l1_1 = l1[1] - l1[0]
# # l1_2 = l1[2] - l1[1]
# # l1_3 = l1[3] - l1[2]
# #
# # l2 = []
# # for i in range(1, len(l1)):
# #     dif = l1[i] - l1[i - 1]
# #     l2.append(dif)
# #     print("Разница в цене", dif)
# #
# #
# # print(l2)
#
#
# j = 0
# i = 0
# while i < 5:  # 10000  == 10_000
#     print(i)
#     # i += 1
#
#     # continue
#
#     # for i in range(1, 4):
#     #     rand_int = random.randint(1, 3)
#     #     print("rand_int = ", rand_int)
#     #     # random.random()  # [0, 1] float
#
#     j += 1
#     if j > 10_000:
#         print("ERROR")
#         break
#
#
# # print(j)


str_ = 'abcdefg'
print(len(str_))
print(len(str_) - 1)
index = random.randint(0, len(str_) - 1)
print(index)
print(str_[index])
