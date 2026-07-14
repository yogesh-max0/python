class laptop:
    def __init__(self):
        self.price = 0
        self.ram = ''
        self.processor = ''
    def display(self):
        print('display')

hp = laptop()
hp.price = 50000
hp.ram = '8gb'
hp.processor = 'i9'

print(hp.price)
print(hp.ram)
print(hp.processor)


'''
-----------------------------------------------------------------------------------------------
'''


class laptop:
    def __init__(self):
        self.price = 0
        self.ram = ''
    def display(self):
        print('price:',self.price)
        print('ram:',self.ram)

infinix = laptop()

infinix.price=500000
infinix.ram='16gb'

infinix.display()


'''
-----------------------------------------------------------------------------------------------------
'''


