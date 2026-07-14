'''
(AND(all given conditions needs to be true) | , OR(any one of the condition must be true) | 
 NOT(not operator is a unary operator placed before a single condition to flip its Boolean outcome))
'''

'''
(OR)
'''

age = 22
area = 'tn'
if(age>18 or area == 'Tn'):
    print('eligible to vote')
else:
    print('not eligible to vote')      # output ==> eligible


a = 10
b = 5
one = (a==10)
two = (b==10)
print(one or two)    # output ==> True

'''
----------------------------------------------------------------------------------------------
'''

'''
(AND)
'''

age = 18
has_license = True
if(age>=18 and has_license):
    print('eligible to drive')
else:
    print('not eligible to drive')  # output ==> eligible to drive


a = 10
b = 1
one = (a==10)
two = (b==10)
print(one and two)      # output ==> False



'''
---------------------------------------------------------------------------------------------
'''



'''
(NOT)
'''

logged_out = True
if(logged_out):
    print('need to login first')
else:
    print('dont need to login')      # output ==>  need to login first


print(not(True))
print(not(False))
