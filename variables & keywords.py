# RULE 1 :
'''
we cant set anything as a variable name because there might be a keywords so we cant use 
keywords as a variable names
'''

import keyword
print(keyword.kwlist)

output = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
      'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'while', 'is',
      'from', 'global', 'if', 'import', 'in', 'lambda', 'try','with','return','nonlocal',
      'not', 'or', 'pass', 'raise', 'while', 'yield'] 


# RULE 2 :
'''
identifiers (variable are case sensitive)
example:
'''

name = 'yogi --- starts with small n'
Name = 'yogi --- starts with capital N'



# RULE 3 :
'''
we can use numbers and names as variables but with some conditions 
example:
'''
hasmyname = 'yogesh' '---valid'
has_my_name = 'yogesh' '---valid' "its also called as snakecase(usinng underscore _)"

# has my name = not valid
'''
1 - we cant leave space for variables
2 - we cant start variables name with numbers
example:
1name = --invalid
name1 = --valid

3 - we can also assing underscore(_) as variable name
'''
_ = 'yogi'
print(_)
