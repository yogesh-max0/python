class dad:
    def narayanan(self):
        print('narayanan\'s son is rishi')

class son(dad):
    def rishi(self):
        print('rishi is narayanan\'s son')

s = son()
s.narayanan()
s.rishi()


'''
---------------------------------------------------------------------------------
'''


class animal:
    def dog(self):
        print('dog is barking')

class cat(animal):
    def cat(self):
        print('cat is meowing')

c = cat()
c.dog()
c.cat()


'''
--------------------------------------------------------------------------------------
'''

# MULTIPLE INHERITANCE

class dad:
    def house(self):
        print('dad has a house')

class son:
    def bakery(self):
        print('son has a bakery')

class mom(dad,son):
    def factory(self):
        print('mom runs a factory')

m = mom()
m.house()
m.bakery()
m.factory()



'''
-----------------------------------------------------------------------------------------
'''


# MULTI LEVEL INHERITANCE

class grandpa:
    def land(self):
        print('grandpa\'s land')
    
class dad(grandpa):
    def shop(self):
        print('dad\'s shop')
    
class son(dad):
    def house(self):
        print('son\'s house')

s = son()
s.land()
s.shop()
s.house()


'''
-----------------------------------------------------------------------------------
'''

# HEIRARCHY INHERITANCE

class dad:
    def money(self):
        print('dad\'s money')

class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

s1 = son1()
s1.money()
s2 = son2()
s2.money()
s3 = son3()
s3.money()


'''
----------------------------------------------------------------------------------
'''


# HYBRID INHERITANCE

class a:
    def methoda(self):
        print('class a')
    
class b(a):
    def methodb(self):
        print('class b')

class c(a):
    def methodc(self):
        print('class c')

class d(b,c):
    def methodall(self):
        print('class d')

d = d()

d.methoda()
d.methodb()
d.methodc()
d.methodall()
