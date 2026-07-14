try:
    a = int(input())
    b = int(input())
    print('success')
except Exception:
    print('id\'s only allowed in numbers')


try:
    a = int(input())
    b = int(input())
    print('success')
except Exception as a:
    print(a)


try:
    a = int(input())
    b = int(input())
    c = input()
    print(c/a)
except TypeError as e:
    print(e)



try:
    a = int(input())
    b = input()
    print(b/a)
except ValueError:
    print('error occured')


try:
    a = int(input())
    a = input()
except Exception:
    print('wait see below')
finally:
    print('guess the error')
