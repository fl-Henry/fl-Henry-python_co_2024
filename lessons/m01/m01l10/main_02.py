# # # # # # def greet(name):
# # # # # #     return f"Hello, {name}!"
# # # # # #
# # # # # #
# # # # # # def greet1(name):
# # # # # #     return f"Hi, {name}!"
# # # # # #
# # # # # #
# # # # # # def call_function(func, value):
# # # # # #     return func(value)
# # # # # #
# # # # # #
# # # # # # print(call_function(greet, "Alice"))
# # # # # # print(call_function(greet1, "Alice"))
# # # # #
# # # # #
# # # # # from functools import reduce
# # # # #
# # # # #
# # # # # def mult(x, y):
# # # # #     print(f"x={x}; y={y}")
# # # # #     return x * y
# # # # #
# # # # #
# # # # # numbers = [1, 2, 3, 4]
# # # # # product = reduce(mult, numbers)
# # # # # print(product)  # Вывод: 24
# # # #
# # # #
# # # # from functools import partial
# # # #
# # # #
# # # # def power(base, exponent):
# # # #     return base ** exponent
# # # #
# # # #
# # # # square = partial(power, exponent=2)
# # # # print(square(5))  # Вывод: 25
# # #
# # #
# # class Car:
# #
# #     param1 = 1
# #     __param2 = "Don't use it"
# #
# #     def __init__(self, make, model):
# #         self.__param2 = ...
# #         self.make = make + str(self.param1)
# #         self.model = model
# #
# #     def display_info(self):
# #         return f"{self.make} {self.model}"
# #
# #     def horn(self):
# #         return 'Ду ду ти'
# # #
# # #
# # my_car = Car("Toyota", "Corolla")
# # print(my_car.__param2)
# # # print(my_car.display_info())  # Вывод: Toyota Corolla
# # # print(my_car.horn())
# # # print(my_car.param1)
# # #
# # # my_car2 = Car("BMW", "M3")
# # # print(my_car2.display_info())
# # # print(my_car2.horn())
# # #
# #
# #
# # # class Rectangle:
# # #     def __init__(self, width, height):
# # #         self.width = width
# # #         self.height = height
# # #
# # #     def area(self):
# # #         return self.width * self.height
# # #
# # #     def perimeter(self):
# # #         return (self.width + self.height) * 2
#
#
# # class BankAccount:
# #     def __init__(self, balance):
# #         self.__balance = balance  # Приватный атрибут
# #
# #     def deposit(self, amount):
# #         if amount > 0:
# #             self.__balance += amount
# #
# #     def __deposit(self, amount):
# #         if amount > 0:
# #             self.__balance += amount
# #
# #     def get_balance(self):
# #         return self.__balance
#
#
class Animal:
    x = 0
    y = 0

    def walk_x(self):
        self.x += 1
        return self.x

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"

    def __str__(self):
        return f"I'm a Dog, {self.speak()}"


animal = Animal()
dog = Dog()
#
# print(animal.speak())
# print(dog.speak())
#
# print(animal.walk_x())
# print(dog.walk_x())
#
# print(animal.walk_x())
# print(dog.walk_x())

print(dog)


class MyList:

    def __init__(self, data):
        self._data1 = data[0]
        self._data2 = self._add(data[1], data[0])
        self._data3 = data[2]

    def _add(self, x, y):
        return x + y

    def display(self):
        print(self._data1)
        print(self._add(self._data2, 2))
        print(self._data3)


x = 666
a = 12
str_ = "Some string"

# mm = MyList([1, 2, 3])
mm = MyList([3, 4, 5])
# mm = MyList()
mm.display()
mm.display()
mm.display()
mm.display()

