
with open("poem.txt") as file:
    for line in file:
        print(line, end='')

# we leave the closing of the file to be done automatically by with open.
# It always calls the thefile.__enter__ function before starting
# and always calls thefile.__exit__ after finishing 

# http://www.python.org/dev/peps/pep-0343/

