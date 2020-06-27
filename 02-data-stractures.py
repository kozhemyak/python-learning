# help(int)

#! ***************************************
#! * Rules:
#! * - Explicit is better than implicit.
#! *
#! ***************************************

## List -----------------------------------------
# a sequence of items.
# this type can be altered.

shoplist = ['apple', 'mango', 'carrot']

print("I have", len(shoplist), 'items to purchase.')

print('These itens are:', end = ' ')
for item in shoplist:
    print(item, end = ' ')

# append list
shoplist.append('banana')

# sort list
shoplist.sort()

# delete
olditem = shoplist[0]
del shoplist[0]

print('My shopping list is now', shoplist)

## Tuple ----------------------------------------
# hold together multiple objects.
# they are immutable like strings i.e. you cannot modify tuples.

zoo = ('python', 'mouse', 'chicken')
singleton = (2 , )
myempty = ()

## Dictionary -----------------------------------
# we associate keys (name) with values (details)
# the key must be unique
# you should use only simple objects for keys.
# key-value pairs in a dictionary are not ordered in any manner
# dict class

addressBook = {
    'Nikolay': 'n@com',
    'Dmitriy': 'd@com'
}

print("Nikolay's address is", addressBook['Nikolay'])

# Deleting a key-value pair
del addressBook['Nikolay']

# Adding
addressBook['Yana'] = 'y@com'

# Foreach
for name, address in addressBook.items():
    print('Contact {} at {}'.format(name, address))

# Check
if 'Yana' in addressBook:
    pass


# help(dict)


## Sequence -------------------------------------
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
# START : END : STEP

print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])



## Set ------------------------------------------
# Sets are unordered collections of simple objects
# you can google "set theory" and "Venn diagram" to better understand our use of sets in Python.

bri = set(['Astana', 'Almaty'])

'Karaganda' in bri

bric = bri.copy()
bric.add('China')
bric.issuperset(bri)

# intersection
print(bri & bric)


## References -----------------------------------
# the variable name points to that part of your computer's memory where the object is stored.
# This is called binding the name to the object.
# there is a subtle effect due to references which you need to be aware of:

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print('shoplist is', shoplist)  # Same object
print('mylist is', mylist)      # Same object

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
del mylist[0]

print('shoplist is', shoplist)  # One object
print('mylist is', mylist)      # Second object



