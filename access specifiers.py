# ACCESS SPECIFIERS ARE USED TO CONTROL WHO CAN ACCESS VARIABLES AND METHODS IN A CLASS

'''
House
│
├── Hall        → Everyone can enter
├── Bedroom     → Family members only
└── Locker      → Only Owner
'''

# 1) public
# 2) protected
# 3) private

# NORMAL 

class Car:

    def __init__(self):
        self.brand = "BMW"  # PUBLIC VARIABLE

car = Car()
print(car.brand)



# 2. Protected Access Specifier

class person:
    def __init__(self):
        self._age = 22    # PROTECTED VARIABLE

class student(person):
    def display(self):
        print(self._age)

s = student()
s.display()
print(s._age)



# 3. PRIVATE ACCESS SPECIFIERS

class Bank:
    def __init__(self):
        self.__balance = 50000   # Private variable

    def display(self):
        print(self.__balance)

b = Bank()
b.display()
print(b.__balance)


'''
| Access Specifier | Variable         | Inside Class | Child Class     | Outside Class       |
| ---------------- | ---------------- | ------------ | --------------- | ------------------- |
| Public           | `self.name`      | ✅            | ✅               | ✅                   |
| Protected        | `self._age`      | ✅            | ✅               | ✅ (not recommended) |
| Private          | `self.__balance` | ✅            | ❌ Direct access | ❌                   |

'''