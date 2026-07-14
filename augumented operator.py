a = 10
b = a+5
c = b*2
d = c-10
e = d/5
print(e)   #output ==> 4

'''
-----------------------------------------------------------------------------------------------------
'''

greeting = 'hello'
b = greeting+" world"
print(b)              #output ==> hello world

'''
-------------------------------------------------------------------------------------------------------
'''

greeting = 'hello'
greeting += 'world'
print(greeting)       #output ==> helloworld

'''
-----------------------------------------------------------------------------------------------------
'''

numbers = [1,2]
numbers += [3,4]
print(numbers)        #output ==> [1,2,3,4]

'''
-----------------------------------------------------------------------------------------------------
'''

balance = 500
print('before balance:',balance)
interest = (7/100*balance+balance)
print('after interest',interest) 