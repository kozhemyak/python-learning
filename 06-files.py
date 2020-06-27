

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open for writing
file = open('poem.txt', 'w')

# Write text to the file
file.write(poem)

# Close the file
file.close()


# Open for reading
file = open('poem.txt')

while True:
    line = file.readline()

    if len(line) == 0:
        break

    print(line, end='')

# close the file
file.close()

# help(open)