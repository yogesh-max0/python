'''
USING WITH WE DONT NEED TO CLOSE THE FILE AND THIS IS THE PYTHONIC WAY OF FILE HANDLING
'''

'''
with open ('1.txt','r') as file:
    for line in file:
        print(line.upper())
'''


'''
---------------------------------------------------------------------------------------------
'''


'''
feedback = input('enter your feedback:')

with open('feedback.txt','w') as log:
    log.write(feedback+'\n')

print('thanks for your valuable feedback!')
'''


'''
-------------------------------------------------------------------------------------------
'''


'''
with open('feedback.txt','r')as a:
    print(a.readline().strip())
'''


'''
--------------------------------------------------------------------------------------------
'''


with open('feedback.txt','r') as b:
    for _ in range(5):
        print(b.readline().strip())

    