for i in 'apple':
    print(i)

'''
---------------------------------------------------------------------------------------
'''

for i in range(1,11):
    print(i,'x2=',i*2)

'''
----------------------------------------------------------------------------------------
'''

for i in range(1,5):
    print('hi')

'''
-----------------------------------------------------------------------------------------
'''

for i in range(1,5):
    print('hi')
    print(i)

'''
-------------------------------------------------------------------------------------------
'''



a = int(input('enter first number:'))
b = int(input('enter second number:'))
for i in range(a+1,b):
    print(i)

    
'''
-------------------------------------------------------------------------------------------------
'''

#EVEN NUMBER FINDING
for i in range(0,11):
    if(i%2!=0):
        print(i)


#TOTAL EVEN OR ODD NUMBER FINDING
count  = 0
for i in range(1,11):
    if(i%2==0):
        count = count+1
print(count) 

'''
----------------------------------------------------------------------------------
'''

e_count = 0
o_count = 0
for i in range(1,11):
    if(i%2==0):
        e_count = e_count+1
    if(i%2!=0):
        o_count = o_count+1
print(e_count)
print(o_count)

'''
---------------------------------------------------------------------------------------
'''

count = 0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count = count+1
print('count is:',count)


#AVERAGE FINDING
average = 0
for i in range(1,6):
    average = average+i
print('average:',average)
    
'''
-----------------------------------------------------------------------------------------------------
'''

a = []
for  i in range(10):
    num = int(input('enter number'+str(i)))
    a.append(num)
print(a)
sum = 0
for i in a:
    sum += i
print(sum)