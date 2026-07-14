marks = int(input('enter marks'))
if marks <1 or marks >100:
    print('ivalid')
elif marks >=35 or marks >=100:
    print('pass')
if marks <35:
    print('you failed')


'''
-----------------------------------------------------------------------------------------------------
'''


income = 7000
if income >=7000:
    print('scholarship not available')
elif income < 7000:
    print('scholarship available') 
else:
    print('invalid')


'''
---------------------------------------------------------------------------------------------------
'''


num = int(input('enter number:'))
if(num%3==0 and num%5==0):
    print('divisible by both')
else:
    print('not divisible by both')


'''
----------------------------------------------------------------------------------------------------
'''


num = int(input('enter number to check even or add:'))
if num%2==0:
    print('even')
else:
    print('odd')

'''
-------------------------------------------------------------------------------------------------
'''

#USING ELIF

mark = int(input('enter mark:'))
if mark<1 or mark>100:
    print('invalid')
if mark<35 :
    print('poor perfomance(fail)')
elif mark>=35 and mark<70:
    print('average perfomance')
elif mark>70 and mark<=100:
    print('excellent perfomance')

'''
--------------------------------------------------------------------------------------------------
'''

a = int(input('enter first  number:'))
b = int(input('enter second number:'))
operators = input('subraction/addition/multiplication/division/modulus:')
if(operators == 'subraction'):
    print(a-b)
elif(operators == 'addition'):
    print(a+b)
elif(operators == 'multiplication'):
    print(a*b) 
elif(operators == 'division'):
    print(a/b)
elif(operators == 'modulus'):
    print(a%b)

'''
------------------------------------------------------------------------------------------------
'''

a = int(input('enter score:'))
if a>=70 and a<101:
    name  =  input('enter your name:')
    age   =  input('enter your age:')
    place =  input('enter your place:')
    print('you are eligible')
else:
    print('you are not eligible')

'''
---------------------------------------------------------------------------------------------------
'''

# NESTED IF
salary = int(input('Salary: '))
age = int(input('Age: '))

if salary>=20000 or age<=25:
    loan= int(input('enter loan amount:'))
    print('loan amount is 50000')

    if loan>50000:
        print('exceeding amount')
    else:
        print('loan approved')
else:
    print('not eligible')