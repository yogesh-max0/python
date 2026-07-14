def hello():
    return "'how'\s you doing'"
print(hello())  


'''
-------------------------------------------------------------------------------------------
'''


def mul(n):
    return[n*n,n*n*n]
print(mul(4))


'''
-------------------------------------------------------------------------------------------
'''


def maths():
    x = 10
    y = 20
    return x,y
a,b = maths()
print(a)
print(b)


'''
-------------------------------------------------------------------------------------------
'''


def job():
    return 'im software engineer'
msg = job()
print(msg)


'''
---------------------------------------------------------------------------------------------
'''


def valuesofA():
    return 10
a = valuesofA()
print(a)


'''
------------------------------------------------------------------------------------------------
'''


name = 'yogi'
password = '1234'

def validate():
    uname = input("Enter username: ")
    pwd = input("Enter password: ")

    if uname == name and pwd == password:
        return True
    else:
        return False

a = validate()
print(a)


'''
------------------------------------------------------------------------------------------
'''

name = 'yogi'
password = '1234'

def validate():
    uname = input("Enter username: ")
    pwd = input("Enter password: ")
    
    if uname == name and pwd == password:
        print('accessible')
    else:
        print('not accessible')
        
validate()


'''
------------------------------------------------------------------------------------------
'''


def add(num1,num2):
    return num1+num2

a = int(input('enter A:'))
b = int(input('enter B:'))
c = int(input('enter C:'))

added = add(a,b)

total = added*c

print(total)