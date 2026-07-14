# WIHTOUT SUPER KEYWORD

class father:
    def __init__(self):
        print('business man')

class son(father):
    def __init__(self):
        print('software engineer')

s = son()                             #it only gives child class input only


'''
-------------------------------------------------------------------------------------
'''


# WITH SUPER KEYWORD

# SUPER KEYWORD USED TO EXECUTE THE PARENTS ROW
class father:
    def __init__(self):
        print('son')

class son(father):
    def __init__(self):
        super().__init__()
        print('dad')
    
s =son()               


'''
-----------------------------------------------------------------------------
'''


class a:
    def __init__(self):
        print('a')
    
class b:
    def __init__(self):
        print('b')

class c(a,b):
    def __init__(self):
        super().__init__()
        print('c')

c = c()                     # NOW IT GIVES ONLY ONE PARENT CLASS WHICH IS GIVEN IN FIRST (LEFT SIDE)



class a:
    def __init__(self):
        print('hiii')

class b:
    def __init__(self):
        print('how are you')

class c(b,a):
    def __init__(self):
        super().__init__()
        print('yogi')

c = c()                       # NOW WE GAVE B AS FIRST CLASS (LEFT SIDE)

