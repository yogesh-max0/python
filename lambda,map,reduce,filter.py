# LAMBDA USED TO WRITE FUNCTIONS IN SINGLE LINE

add = lambda a,b : a+b
print(add(1,2))


square = lambda a : a*a
print(square(2)) 


multiple = lambda a,b : a*b
print(multiple(2,3))



'''
--------------------------------------------------------------------------------------
'''

# MAP() USED  applies a specific function to each item in an iterable 
# (like a list, tuple, or dictionary) returns a map object (an iterator) containing the results.Syntax

numbers = [1,2,3,4,5]
result = map(lambda x: x*2 ,numbers)
print(list(result))


strings = ['1','2','3','4','5']
integres = map(int,strings)
print(list(integres))


integers = [1,2,3,4,5,6]
strings = map(str,integers)
print(list(strings))


fruits = ['apple','orange']
result = list(map(lambda fruits : fruits.upper(),fruits))
print(result)



'''
---------------------------------------------------------------------------------------
'''

# FILTER 

nums =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda nums: nums %2 ==0,nums))
print(even)


nums =[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda nums: nums %2 !=0,nums))
print(even) 



'''
---------------------------------------------------------------------------------------
'''

# REDUCE() applies a specific function to all elements in an iterable
# cumulatively reducing them to a single value

from functools import reduce

nums = [1,2,3,4]
total = reduce(lambda a,b : a+b,nums)
print(total)                # IT TOTAL ALL VALUES INTO SINGLE VALUE



from functools import reduce

nums = [1,2,3,4,5]
maximum = reduce(lambda a,b : a  if a>b else b , nums)
print(maximum)