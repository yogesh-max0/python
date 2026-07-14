'''
THERE IS 2 TYPES IN VARIABLES (CLASS VARIABLE) AND (INSTANCE VARIABLE) 
'''
# INSTANCE VARIABLE

class phone:
    def __init__(self,brand,price,ram):
        self.brand = brand
        self.price = price
        self.ram = ram
    def display(self):
        print('brand:',self.brand)
        print('price:',self.price)
        print('ram:',self.ram)

print('samsung specifications;')        
samsung = phone('samsung',20000,'8gb')
samsung.display()

print('redmi specifications;')
redmi = phone('redmi',25000,'8gb')
redmi.display()



'''
-------------------------------------------------------------------------------------------------
'''


# CLASS VARIABLE 

class students:
    batch = 2021
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('students:',self.name)
        print('age:',self.age)
        print('batch:',self.batch)

s1 = students('dholu',21)
s2 = students('bholu',21)

s1.display()
s2.display()
        


'''
------------------------------------------------------------------------------------------------
'''


