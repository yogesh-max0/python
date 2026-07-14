'''
---bitwise operators are used to perform bit-level operations directly on 
the binary representations of integers
bitwise or (|) , bitwise and (&) , bitwise not(~) , bitwise xor(^)
'''

'''
not rules = 1 = -2 , 2 = -3 , 3 = -4
'''
a = 1
print(~a )     #output ==> -2


'''
And rules(&)
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = =
'''
a = 1
b = 2
print(a & b)   #output ==> 0


'''
or rules (|)
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
'''

a = 2
b =4
print(a | b)    #output ==> 6



'''
xor rules(^)
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
'''

a = 5
b = 11
print(a ^ b)   #output ==> 14