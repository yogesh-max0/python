'''
'r' read only      | ( file must exist ) 
'w  write only     | ( overwrites or creates )
'a' append-only    | ( adds to end of file )
'r+' read + write  | ( file must exist )
'w+' write + read  | ( overwrites or creates )
'a+' append + read | ( creates if not exists )
'rb'               | (read binary)
'wb'               | (write binary)
'ab'               | (append binary)
'''

# CREATING FILE 

file = open('1.txt','w')
file.write('hi \n')
file.write('this is file handling\n')
file.close()


# READ FILE

file = open('1.txt','r')
content = file.read()
print('file content:\n',content)
file.close()


# APPEND (ADDS IN LAST LINE)

file = open('1.txt','a')
file.write('this is appending in file handling\n')
file.close()


'''
----------------------------------------------------------------------------------------
'''

