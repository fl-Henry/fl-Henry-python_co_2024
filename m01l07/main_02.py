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


def average_grade(number):
    one = students[number].get('grades')
    # a = 0
    # for i in range(len(one)):
    #    a += one[i]

    a = sum(one)

    sr_value = a / len(one)
    return sr_value


def filter_students_by_age(students, age):
    a = []
    for i in range(len(students)):
        two = students[i]
        age_value = two.get('age')
        if age_value == age:
            a.append(two)

    # a = [x for x in students if x.get('age') == age]
    # [{'id': 3, 'name': 'Charlie', 'age': 21, 'grades': [80, 85, 88]}, {'id': 7, 'name': 'Grace', 'age': 21, 'grades': [88, 90, 93]}]
    # [{'id': 3, 'name': 'Charlie', 'age': 21, 'grades': [80, 85, 88]}, {'id': 7, 'name': 'Grace', 'age': 21, 'grades': [88, 90, 93]}]
    return a


def best_student(students):
    best_grade = 0
    for i in range(len(students)):
        two = students[i]
        sr_value = average_grade(i)
        if sr_value > best_grade:
            best_grade = sr_value
            student = two
    return student


def top_5_students(students):
    students = students.copy()
    a = []
    for i in range(5):
        best = best_student(students)
        students.remove(best)
        a.append(best)

    # [{'id': 5, 'name': 'Eve', 'age': 23, 'grades': [95, 88, 91]}, {'id': 2, 'name': 'Bob', 'age': 22, 'grades': [89, 94, 90]}, {'id': 7, 'name': 'Grace', 'age': 21, 'grades': [88, 90, 93]}, {'id': 10, 'name': 'Jack', 'age': 22, 'grades': [92, 85, 88]}, {'id': 9, 'name': 'Ivy', 'age': 24, 'grades': [82, 89, 87]}]
    # [{'id': 2, 'name': 'Bob', 'age': 22, 'grades': [89, 94, 90]}, {'id': 5, 'name': 'Eve', 'age': 23, 'grades': [95, 88, 91]}, {'id': 7, 'name': 'Grace', 'age': 21, 'grades': [88, 90, 93]}, {'id': 9, 'name': 'Ivy', 'age': 24, 'grades': [82, 89, 87]}, {'id': 10, 'name': 'Jack', 'age': 22, 'grades': [92, 85, 88]}]

    # average = [average_grade(x) for x in range(len(students))]
    # average.sort(reverse=True)
    # average = average[:5]
    #
    # a = [students[x] for x in range(len(students)) if average_grade(x) in average]

    return a


# # number = int(input("Укажите номер студента: ")) - 1
# number = 1
# z = average_grade(number)
# print(z)

# age = int(input("Укажите возраст студентов: "))
# age = 21
# c = filter_students_by_age(students, age)
# print(c)

# best = best_student(students)
# print(best)

print(len(students))
best = top_5_students(students)
print(best)
print(len(students))

best = top_5_students(students)
print(best)
print(len(students))
