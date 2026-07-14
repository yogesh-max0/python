# ABSTRACTION HIDES DATA

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print('dog barks')

d = dog()
d.sound()


'''
----------------------------------------------------------------------------
'''


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def display(self):
        self.sound()

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

d = Dog()
d.display()