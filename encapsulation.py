'''
Encapsulation is the process of wrapping data (variables) and methods (functions) 
into a single unit (class) and protecting the data from direct access.
'''

from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    class dog(animal):
        def sound(self):
            print('dog barks')

d = animal()
d.sound()