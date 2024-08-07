
# INIT
#
# number = int(input("enter number: "))
#
#
# if  number >= 0:
#     print('ok')
#
# elif number == str():
#      print("not ok")
#
# else:
#    print("not ok")


#
# # number = int(input("enter number: "))
#
# number = input("enter number: ")  # sbsadg
# try:
#     number = int(number)
# except:
#     print("Could not convert to integer")
#
#
# if type(number) is int:
#     print("number is int")
#
# elif type(number) is str:
#     print("number is str")
#
# # elif number >= 0:
# #     print('ok')
# #
# # else:
# #     print("not ok")
# #
# #



#
# #
# # for index in range(8):  # [0, ..., 7]
# #
# #     print("index start for = ", index)
# #     index = 666
# #     j = 2 * index
# #     print("index = ", index, "j = ", j)
#
# print(list(range(8)))
# print(list(range(0, 8)))

#
# import string
# import secrets
#
# letters = string.ascii_letters
# digits = string.digits
# special_chars = string.punctuation
# alphabet = letters + digits + special_chars
#
# a = len(input('Enter password: '))
# try:
#     b = str(a)
# except ValueError:
#     b = int()
#
# psw_length = b
#
# psw = ''
# for i in range(a):
#     psw += ''.join(secrets.choice(alphabet))
#
# print(psw)




"""

1. **Данные:**
   - У вас есть список студентов, где каждый студент представлен в виде словаря (dict)
   с ключами: `id`, `name`, `age`, `grades` (список оценок).

   ```python
   students = [
      {"id": 1, "name": "Alice", "age": 20, "grades": [85, 92, 78]},
      {"id": 2, "name": "Bob", "age": 22, "grades": [89, 94, 90]},
      {"id": 3, "name": "Charlie", "age": 21, "grades": [80, 85, 88]},
      {"id": 4, "name": "Diana", "age": 20, "grades": [70, 75, 80]},
      {"id": 5, "name": "Eve", "age": 23, "grades": [95, 88, 91]},
      {"id": 6, "name": "Frank", "age": 22, "grades": [65, 72, 68]},
      {"id": 7, "name": "Grace", "age": 21, "grades": [88, 90, 93]},
      {"id": 8, "name": "Hannah", "age": 20, "grades": [77, 84, 79]},
      {"id": 9, "name": "Ivy", "age": 24, "grades": [82, 89, 87]},
      {"id": 10, "name": "Jack", "age": 22, "grades": [92, 85, 88]}
    ]
   ```

2. **Задачи:**
   - **Функция 1: Средний балл**. Напишите функцию `average_grade(grades)` для расчета среднего балла конкретного студента.
   - **Функция 2: Фильтрация студентов по возрасту**. Напишите функцию `filter_students_by_age(students, age)` для фильтрации
   студентов по возрасту. Она должна возвращать список студентов, чей возраст совпадает с указанным.
   - **Функция 3: Определение лучшего студента**. Напишите функцию `best_student(students)` для определения студента с наивысшим
   средним баллом. Функция должна возвращать словарь с данными о лучшем студенте.
   - **Функция 4: TOP 5**. Напишите функцию `top_5_students(students)` для определения пяти студентов с наивысшим средним баллом.
    Функция должна возвращать список студентов с их данными (JSON)

"""

#
# def average_grade(grades: list):
#     return sum(grades) / len(grades)


def average_grade(student):
    # print(student)
    return sum(student.get('grades')) / len(grades)


def filter_students_by_age(students, age):
    return [x for x in students if x.get('age') == age]
    # return [x for x in students if x['age'] == age]


def best_student(students):

    best_student_id = -1
    best_student_average = -1
    for student in students:
        average = average_grade(student.get('grades'))
        if average > best_student_average:
            best_student_id = student.get('id')
            best_student_average = average

    # return max(students, key=average_grade)
    return [x for x in students if x.get('id') == best_student_id][0]


def top_5_students(students):

    student_average = [average_grade(x) for x in students]
    student_average.sort(reverse=True)
    student_average = student_average[:5]

    best_students = [x for x in students if average_grade(x) in student_average]

    return best_students


students = [
    {"id": 1, "name": "Alice", "age": 20, "grades": [85, 92, 78]},
    {"id": 2, "name": "Bob", "age": 22, "grades": [89, 94, 90]},
    {"id": 3, "name": "Charlie", "age": 21, "grades": [80, 85, 88]},
    {"id": 4, "name": "Diana", "age": 20, "grades": [70, 75, 80]},
    {"id": 5, "name": "Eve", "age": 23, "grades": [95, 88, 91]},
    {"id": 6, "name": "Frank", "age": 22, "grades": [65, 72, 68]},
    {"id": 7, "name": "Grace", "age": 21, "grades": [88, 90, 93]},
    {"id": 8, "name": "Hannah", "age": 20, "grades": [77, 84, 79]},
    {"id": 9, "name": "Ivy", "age": 24, "grades": [82, 89, 87]},
    {"id": 10, "name": "Jack", "age": 22, "grades": [92, 85, 88]}
]

grades = students[0]['grades']
# result = average_grade(grades)
# print(result)
#
# result = filter_students_by_age(students, 22)
# print(result)

# result = best_student(students)
# print("result", result)

result = top_5_students(students)
print("result", result)


