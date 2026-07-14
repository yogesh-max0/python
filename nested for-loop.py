for a in range(1,4):
    for b in range(1,3):
        print(b,'yogi')


'''
-------------------------------------------------------------------------------------
'''

for i in range(1,3):
    print('week:',i)
    for j in range(1,8):
        print('day:',j)

'''
-----------------------------------------------------------------------------------------------------
'''

#STRAIGHT
for a in range(1,6):
    print('*')
    for b in range(1,a+1):
        print(b,end='')

for i in range(6):
    print('#'*i)


#REVERSE
for i in range(5,0,-1):
    print('#'*i)

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

