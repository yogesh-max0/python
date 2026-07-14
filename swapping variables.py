a = 10
b = 5
print('before swapping')
print('a:',a,'b:',b)

a,b = b,a
print('after swapping')
print('a:',a,'b:',b)    #output ==> 


'''
------------------------------------------------------------------------------------------------------
'''


a = 1
b = 2
print('before swapping','a:',a,"b:",b)

temp = a
a = b
b = temp
print('after swapping','a:',a,'b:',b)


'''
------------------------------------------------------------------------------------------------
'''


young = 'vicky'
elder = 'yogi'

print("before swapping")
print('young:',young ,',' ,'elder:',elder)

young,elder = elder,young
print('after swapping')
print('elder:',elder,',','young:',young)



'''
-------------------------------------------------------------------------------------------
'''


young = 'a'
elder = 'b'
print(f"before swapping young:{young} , elder:{elder}")

temp = young
young = elder
elder = temp
print(f'after swapping young:{young} , elder:{elder}')


