class laptop:
    price = 0
    processor = ''
    ram = ''

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price = 20000
hp.processor = 'i3'
hp.ram = '4gb'

dell.price = 30000
dell.processor = 'i5'
dell.ram = '8gb'

lenovo.price = 50000
lenovo.processor = 'i9'
lenovo.ram = '16gb'

print('specifications of hp')
print(hp.ram)
print(hp.price)
print(hp.processor)

print('specifications of dell')
print(dell.ram)
print(dell.price)
print(dell.processor)

print('specifications of lenovo')
print(lenovo.ram)
print(lenovo.price)
print(lenovo.processor)


'''
--------------------------------------------------------------------------------------------------
'''


class student:
    def __init__(self):
        self.name = ''
        self.age = 0
    def display(self):
        print('name:',self.name)
        print('age:',self.age)

s1 = student()
s2 = student()

s1.name = 'yogi'
s2.name = 'vicky'

s1.age = 22
s2.age = 26

print('student 1 details:')
s1.display()
print('student 2 details:')
s2.display()


'''
------------------------------------------------------------------------------------------
'''


class fruit:
    def __init__(self,color):
        self.color = color

apple = fruit('apple is red')
orange = fruit('orange is orange')

print(apple.color)
print(orange.color)



'''
----------------------------------------------------------------------------------------
'''


class teacher:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def display(self):
        print('name:',self.name)
        print('regno:',self.regno)
           
t1 = teacher('sindhu','100234')
t2 = teacher('bindhu','100111')

t1.display()
t2.display()


'''
---------------------------------------------------------------------------------------
'''


class calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b

    def add(self):
        print('addition:', self.num1 + self.num2)

    def sub(self):
        print('subtraction:', self.num1 - self.num2)

obj = calculator(10,2)

obj.add()
obj.sub()