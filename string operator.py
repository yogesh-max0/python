# STRING REPLICATION
print('hi'*10)

a = 'hello'
print(a*10)


# STRING CONCADENATION
str1 = 'hi hello'
str2 = 'welcome'
print(str1 + str2)


a = '*'*20
b = "happy" + " diwali"
print(a,b,a,sep='\n')

'''
-------------------------------------------------------------------------------------
'''

name = 'yogeshwaran'
print(name.upper())
print(name.capitalize())
print(name.lower())    

'''
--------------------------------------------------------------------------------------
'''

number = '1234567890'
masked = number[:2]
print(masked)



number = '1234567890'
masked = number[-2:]
print(masked)



number = '1234567890'
masked = number[:2] + '******' + number[-2:]
print(masked)

'''
----------------------------------------------------------------------------------------
'''

song = 'sHApe OF you'
aritst = 'YOGesh'
formatted  = f"{song.title()} - {aritst.title()}"   # GIVES TITLE LIKE STRINGS
print(formatted)
                  

song = 'wanNA be YOURs'
artist ='YOgesH'
print(song.title(),aritst.capitalize())       # SAME LIKE TITLE

'''
--------------------------------------------------------------------------------------
'''

location = 'mumbai'
change_location = location.replace('mumbai','chennai')  # IT REPLACES OLD WITH NEW (REPLACE)
print(change_location)

'''
---------------------------------------------------------------------------------------
'''

aadhar = 'your aadhar number is: 1234 5678 1290 dont share it'
num = aadhar.split(':')[1]                             #  1234 5678 1290 dont share it                             #  1234 5678 1290 dont share it
print(num) 

aadhar = 'your aadhar number is: 1234 5678 1290 dont share it'
num = aadhar.split(':')[1].split('d')[0]
print(num)                                            #1234 5678 1290


aadhar = 'your aadhar number is: 1234 5678 1290 dont share it'
num = aadhar.split(':')[1].split('d')[0].strip()     # STRIP CLEARS ANY SPACE
print(num)                


'''
-----------------------------------------------------------------------------------------
'''

# MEMBERSHIP STRING FUNCTION (IN and NOT IN)

offer = 'your promocode for this offer available'
if 'promocode' in offer:
    print('available for discount')


'''
--------------------------------------------------------------------------------------
'''


# POSITION FINDING

feedback = 'this was very good and enjoyable'
print('position of enjoyable is:',feedback.find('enjoyable'))  # ENJOYABLE STARTS FROM 23RD POSTION


'''
------------------------------------------------------------------------------------
'''


name = 'yogesh waran'
initial =([word[0].upper() for word in name.split()])
print(initial)


name = 'yogesh waran yogesh'
initals = ''.join([word[0].upper() for word in name.split()])
print(initals)



'''
------------------------------------------------------------------------------------------
'''


# STRIP

name = '    yogeshwaran    '
strip = name.strip()
print(name)             # IT HAVE SPACES IN OUTPUT
print(strip)            # STRIPS USED TO GET RID OF SPACES


'''
--------------------------------------------------------------------------------------------
'''


# LEN

sentence = 'sunday is holiday'
len = len(sentence.split('holiday'))
print(len)


