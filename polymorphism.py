'''
What is Polymorphism?
Poly = Many
Morph = Forms
Polymorphism = One thing → Many forms
Programming-ல,
ஒரே method name இருந்தாலும், different classes-ல different behavior கொடுப்பது.
'''

#METHOD OVERRIDING

class animal:
    def sound(self):
        print('animals makes sound')

class dog(animal):
    def sound(self):
        print('dog barks')

class bird(animal):
    def sound(self):
        print('birds singing')
    
a = animal()
d = dog()
b = bird()
a.sound()
d.sound()
b.sound()


'''
------------------------------------------------------------------------------------
'''


class person:
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self, name,grade):
        super().__init__(name)
        self.grade =grade

    def display(self):
        print('name:',self.name)
        print('grade:',self.grade)

s = student('yogi',1)
s.display()


'''
-----------------------------------------------------------------------------------
'''

