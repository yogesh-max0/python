def painter():
    print('painter had come')
painter()

'''
-----------------------------------------------------------------------------
'''

def add():
    print('addition')
    a = int(input('enter 1st number:'))
    b = int(input('enter 2nd number:'))
    c = int(input('enter 3rd number:'))
    print(a+b+c)
def sub():
    print('subraction')
    a = int(input('enter 1st number:'))
    b = int(input('enter 2nd number:'))
    c = int(input('enter 3rd number:'))
    print(a-b-c)
def mul():
    print('multiplication')
    a = int(input('enter 1st number:'))
    b = int(input('enter 2nd number:'))
    c = int(input('enter 3rd number:'))
    print(a*b*c)
def div():
    print('division')
    a = int(input('enter 1st number:'))
    b = int(input('enter 2nd number:'))
    c = int(input('enter 3rd number:'))
    print(a/b/c)
add()
sub()
mul()
div()

'''
-----------------------------------------------------------------------------------------------
'''

def evenorodd(num):
    if num%2==0:
        print('even')
    else:
        print('odd')
a=int(input('enter number:'))
evenorodd(a)


def passfail():
    if score>=35 and score<101:
        print('pass')
    else:
        print('fail')
score = int(input())
passfail()


def printrange(a,b):
    for i in range(a,b):
        print(i)
a = int(input())
b = int(input())
printrange(a,b)