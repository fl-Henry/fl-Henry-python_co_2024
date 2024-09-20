# string = "Hello, World!\nWorld"
#
# # print(string)
# # print(string.upper())
# # print(string.lower())
#
# # new_string = string.replace("\n", " ")
# # # new_string = string.replace("World", "Python")
# # print(new_string)
#
#
# # # words = string.split("\n")
# # words = string.split("sdfhgsd")
# # print(words)
#
#
# # words = ['Hello', 'World!', 'sdgfsdg']
# # joined_string = "; ".join(words)
# # print(joined_string)
#
#
# # stripped_string = "   Hello, World!   "
# # print(stripped_string)
# # print(stripped_string.strip())
#
#
# def build_template(var):
#     # formatted_string = "Hello, %s!" % var
#     # formatted_string = "Hello, {} {}!".format(var, 5)
#     # formatted_string = "Hello, {1} {0}!".format(var, 5)
#     # formatted_string = "Hello, {name} {0}!".format(5, name=var)
#     formatted_string = f"Hello, {var}! You are {18+4} years old."
#     return formatted_string
#
# # C:\Users\user_name\PycharmProjects\python_co_2024
# print(build_template("George"))


# file = open('main_01.txt', 'r', encoding='utf-8')
#
# # print(file.read())
# print(file.readlines())
#
# file.close()

# file = open('main_01.txt', 'w', encoding='utf-8')
#
# write_str = 'Метод writelines(): Записывает:последовательность строк в файл. Не добавляет символы новой строки автоматически.'
# # file.write(write_str)
#
# write_str = write_str.split(":")
# write_str = [x.strip() + "\n" for x in write_str]
# # print(write_str)
# file.writelines(write_str)
# file.close()

with open('main_01.txt', 'r', encoding='utf-8') as file:
    # row = file.readline()
    # print(row)
    # row = file.readline()
    # print(row)
    for line in file.readlines():
        print(line)


" | "
"::"
","
";"
