'''
THERE ARE SEVERAL METHODS  IN METHODS
'''

# INSTANCE METHOD
class student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print('name:',self.name)

s=student('yogi')
s.display()


'''
-----------------------------------------------------------------------------
'''

# CLASS METHOD

class school:

    school = 'this school'

    @classmethod
    def show_school(cls):
        print(cls.school)

school.show_school()


'''
---------------------------------------------------------------------------------------------------
'''


# STATIC METHOD

class calci:

    @staticmethod
    def add(a,b):
        print(a+b)

calci.add(10,2)


'''
----------------------------------------------------------------------------------------------
'''


# ALL COMBINED

class method:
    def instance(self):
        print('instancce method')

    @classmethod
    def class_method(cls):
        print('class method')

    @staticmethod
    def static_method():
        print('static method')

obj = method()
obj.instance()
obj.class_method()
obj.static_method()
