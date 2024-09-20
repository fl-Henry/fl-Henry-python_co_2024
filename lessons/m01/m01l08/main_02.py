# # string = "Hello, World!\nWorld\nWorld"
# # print(string)
# #
# # uppercase_string = string.upper()
# # print(uppercase_string)
# #
# # lowercase_string = string.lower()
# # print(lowercase_string)
#
#
# # str_ = 'Command_1'
# #
# # if str_.lower() == 'command_1'.lower():
# #     print('command_1')
# # elif str_ == 'command_2':
# #     ...
# # elif str_ == 'command_3':
# #     pass
# # else:
# #     print('Invalid')
#
#
# # # new_string = string.replace("World", "Python")
# # new_string = string.replace("\n", " ")
# # print(new_string)
# #
# # ";" "x089;"
#
#
# # string = "Hello; World 1!\nHello; World 2!"
# # print(string)
# #
# # words = string.split("\n")
# # print(words)
# # # CSV
# #
# # words = ['Hello', 'Python', 'World']
# # joined_string = " ; ".join(words)
# # print(joined_string)
#
#
# # str_ = "  \n  Hello, World!   "
# # stripped_string = str_.strip()
# # print(str_)
# # print(stripped_string)
#
# name = "Alice"
# formatted_string = "Hello, {}!".format(name)
# print(formatted_string)
#
# # formatted_string = "Hello, {0}! You have {1} new messages.".format(name, 5)
# # formatted_string = "Hello, {1}! You have {0} new messages.".format(name, 5)
# formatted_string = "Hello, {hello_name}! You have {} new messages.".format(5, hello_name=name)
# print(formatted_string)

# name = "Alice"
# age = 30
# formatted_string = f"Hello, {name}! You are {age} years old."



# raw_string = "\n"
# raw_string = "C:\\Users\\Name\\Docu\nments\\File.txt"
# raw_string = r"C:\Users\Name\Docu\nments\File.txt"
# print(raw_string)


# file = open('main_01.txt', 'r', encoding='utf-8')
#
# # content = file.read()
# # print(content)
#
# # lines = file.readlines()
# # lines = [x.strip() for x in lines]
# # print(lines)
#
#
# line = file.readline()
# print(line)
#
# line = file.readline()
# print(line)
#
# line = file.readline()
# print(line)
# file.close()


# file = open('main_02.txt', 'w', encoding='utf-8')
#
# file.write("\nHello, World!")
#
# file.close()


with open('main_02.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
