# simple datatypes
'''
(string , integers , floats , boolean)

string = alphabets, -ex(names)

int(integer) = numbers, - ex(1,2,3,4)

floats = digits - ex(1.2,4.666)

boolean = true or false 
'''


#complex datatypes
'''
(list , tuple , dictionary , set)

list = ['yogi',22,15.000,true]
---List items are ordered, changeable, and allow duplicate values.
---List items are indexed, the first item has index [0], the second item has index [1] etc.

tuple = (1,hi,1.50,false)
---Tuple items are ordered, unchangeable, and allow duplicate values.
---Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

dictinories = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
---A dictionary is a collection which is ordered, changeable and do not allow duplicates.

myset = {"apple", "banana", "cherry"}
---A set is a collection which is unordered, unchangeable*, and unindexed.
'''

'''
name = ('yogi')
name is variable and variable's another name is called identifier
'''

name = 'yogi'
print(type(name))

age = 22
print(type(age))

salary = 17.4444
print(type(salary))

good = True
print(type(good))
