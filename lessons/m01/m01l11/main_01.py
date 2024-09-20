
import pathlib

import requests


global_var_int = 1
global_var_str = "some string"


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

print(__file__)
