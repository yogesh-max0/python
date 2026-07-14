# PURE FUNCTIONS
'''
A Pure Function satisfies 2 rules:

For the same input, it always returns the same output.
It does not modify or depend on anything outside the function 
(no global variables, files, databases, user input, etc.)
'''

def add(a,b):
    return a*b
print(add(10,2))
print(add(10,2))  # ALWAYS GETS SAME VALUES NO CHANGES IN VALUES


def area(length,width):
    return length*width
print(area(2,4))         # NO CHANGES IN VALUES


'''
----------------------------------------------------------------------------------------
'''


# IMPURE FUNCTIONS
'''
An Impure Function is a function that:

Changes something outside itself, or
Depends on something outside itself.

These are called side effects.
'''

total = 0     # ASSIGNING GLOBAL VARIABLE IT CAN CHANGE THE VALUES AND GIVES SIDE EFFECTS
def add(amount):
    global total
    total += amount
    return total

print(add(100))
print(add(100))

