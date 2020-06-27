import pickle
import sys

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

# Write to the file in binary mode
file = open(shoplistfile, 'wb')

# Dump the object to a file
# This process is called pickling.
pickle.dump(shoplist, file)

file.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
file = open(shoplistfile, 'rb')

# Load the object from the file
# This process is called unpickling.
storedlist = pickle.load(file)

print(storedlist)

file.close()
