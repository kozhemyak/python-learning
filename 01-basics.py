

# Code tells you how, comments should tell you why.
# Python is case-sensetive
print("Hello World")



"""
This is a multi-line string
"""


# ---------------------------------------------------------
# Lesson 2

age = 34
name = 'Nikolay'

print('{0} was {1} years old when he wrote this line of code.'.format(name, age))
print('{} was {} years old when he wrote this line of code.'.format(name, age))
print('{name} was {age} years old when he wrote this line of code.'.format(name=name, age=age))
print('{name} was {age} years old when he wrote this line of code.'.format(name='Nikolay', age=34))
print(f'{name} was {age} years old when he wrote this line of code.')

# Other format() ways
print('Float:\t {0:.3f}'.format(1.0/3))
print('Formated text:\t {0:_^20}'.format('helloasdasd'))

# No new line
print('a', end='')
print('b', end='')


# Raw strings

print(r"Newlines are indicated by \n")


# ---------------------------------------------------------
# Lesson 3

number = 23

guess = int(input('Enter an interger : '))

if guess == number:
    # new block
    print('It is correct.')
elif guess < number:
    print('No, it is a little higher...')
else:
    print('No, it is a little lower...')

print('Done')