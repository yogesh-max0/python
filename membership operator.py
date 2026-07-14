'''
membership operators are used to check whether the values that present in list ot tuple or dictionary
'''
'''
(IN METHOD)
'''

names = ('yogi','vicky','kumar','selvi')
print('yogi'in names)                    #output ==> true


'''
----------------------------------------------------------------------------------------------------
'''


greet1 = 'Hello'
greet2 = 'world'
print('hello'in greet1)    #output ==> false (h is caps in variable)
print('world' in greet2)  #output ==> true


'''
-----------------------------------------------------------------------------------------------------
'''


age = [22]
print(2 in age)

'''
-----------------------------------------------------------------------------------------------------
'''

'''
(NOT IN METHOD)
'''
print('NOT IN METHOD')

name = ['yogi']
print('Yogi' not in name)

'''
-----------------------------------------------------------------------------------------------
'''


age = [22]
print(2 not in age)

age = [22]
print(22 not in age)