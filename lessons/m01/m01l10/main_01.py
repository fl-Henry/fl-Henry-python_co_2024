# # def greet(name):
# #     return f"Hello, {name}!"
# #
# #
# # def greet2(name):
# #     return f"Hi, {name}!"
# #
# #
# # def call_function(func, value):
# #     return func(value)
# #
# #
# # def return_func(func_name):
# #     if func_name == "greet":
# #         return greet
# #     elif func_name == "greet2":
# #         return greet2
# #     else:
# #         return "I don't know this func"
# #
# # # print(call_function(greet, "Alice"))  # Вывод: Hello, Alice!
# # # print(call_function(greet2, "Alice"))  # Вывод: Hi, Alice!
# #
# #
# # func = return_func("greet")
# # print(func("Alice"))
# # func = return_func("greet2")
# # print(func("Alice"))
#
#
# #
# # from functools import reduce
# #
# # numbers = [1, 2, 3, 4, 5, 6]
# # product = reduce(lambda x, y: x + y, numbers)
# # print(product)  # Вывод: 24
# #
# # class Car:
# #     def __init__(self, make, model):
# #         self.make = make
# #         self.model = model
# #
# #     def display_info(self):
# #         return f"{self.make} {self.model}"
# #
# #
# # my_car1 = Car("Toyota1", "Corolla1")
# # print(my_car1)
# # print(my_car1.display_info())
# #
# # my_car2 = Car("Toyota2", "Corolla2")
# # print(my_car2.display_info())
#
#
#
# class Person:
#
#     param1 = {
#
#     }
#     __param2 = 2
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#         self._params = {
#             "name": name,
#             "age": age,
#         }
#
#     @property
#     def age(self):
#         v1 = self.__param2
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self._age = value
#
#     def __str__(self):
#         return str(self.param1)
#
#
# p1 = Person("N", 2)
# print(p1)
# print(p1.age)
# print(p1.__param2)


class Animal:
    x = 0
    y = x

    def walk_x(self):
        self.x += 1
        print(f'walking x at 1 to {self.x}')

    def speak(self):
        return "Some sound"

    def __str__(self):
        return f"It's an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"

    def __str__(self):
        return f"It's a dog"



animal = Animal()
animal.walk_x()
animal.walk_x()
print(animal.speak())
print(animal)


dog = Dog()
dog.walk_x()
dog.walk_x()
print(dog.speak())

print(repr(str(dog)))