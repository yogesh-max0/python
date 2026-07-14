#LIST , TUPLE , SET , DICTIONARY
# LIST[]
# 1) LIST - allows duplicate any type of data can be stored and add or remove 
# 2) insert(),append(),extend(),pop(),remove(),reverse()

# APPEND
a = [1,2,3]
a.append(True)
a.append('yogi')
a.append(9)
print('append',a)

# INSERT 
a = [1,2,3,4,5]
a.insert(0,9)  #HERE 0 IS INDEXING
print('insert',a)

# POP
a = [1,2,3,4]
a.pop(1)   # HERE 0 IS INDEXING
print('pop',a)

a = [1,2,3]  #POP defaulty removes the last element
a.pop()
print('pop',a)

# REMOVE
a = [1,2,3,4,5,6,7]
a.remove(2)
print('removed',a)

# EXTEND
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

# REVERSE

a = ['yogi','vicky',1,2,3]
a.reverse()
print('reversed',a)


# COUNT
a = ['yogi','vicky',1,2]
print('count:',a.count('vicky'))



'''
---------------------------------------------------------------------------------------------
'''

# TUPLE()
# ALLOWS DUPLICATE ANY TYPE OF DATA CAN BE STORED BUT CANNOT ADD OR CHANGE
# WE CAN CHANGE TUPLE INTO LIST
a = (1,2,3)
b=list(a)
b.pop()
print(b)

'''
---------------------------------------------------------------------------------------------
'''

#SET{}
# DOESNT ALLOW DUPLICATES ALLOW ANY TYPE OF DATA AND CANNOT MODIFY SET BUT WE ADD OR REMOVE
# SETS ARE UNORDERED 
# ADD(),UPDATE(),REMOVE(),POP()

a = {1,2,3,1}
print(a)   # output ==> {1,2,3}

a = {1,2,3}
a.add(4)
print(a)

a = {1,2,3,4}
a.remove(4)
print(a)

a={1,2,3,4,5}
a.pop()
print(a)


a = {1,2,3,4}
a.update([5])
print(a)

'''
------------------------------------------------------------------------------------------
'''


# DICTIONARIES

a = {
    'name':'yogi',
    'age':22,
    'place':'upt'
}
print(a)

a = {
    'name':'yogi',
    'age':22,
    'place':'upt',
}
print(a['name'])


a = {
    'name':'yogi',
    'age':22,
    'place':'upt',
}
print(a.keys())


a = {
    'name':'yogi',
    'age':22,
    'place':'upt',
}
print(a.values())