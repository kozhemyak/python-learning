import sys
import time

file = None

try:
    file = open("poem.txt")
    while True:
        line = file.readline()
        if len(line) == 0:
            break

        print(line, end='')

        # note that we use sys.stdout.flush() 
        # after print so that it prints to the screen immediately.
        sys.stdout.flush()

        time.sleep(2)

except IOError:
    print("Could not find file!")

except KeyboardInterrupt:
    print("You cancelled the reading from the file.")

finally:
    if file:
        file.close()
    print("(Cleaning up: Closed the file)")

