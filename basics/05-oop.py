
#* Types of programming:
#* procedure-oriented way of programming
#* object oriented programming paradigm

# integers are treated as objects (int class)
# help(int)
# the boxing and unboxing concept?

# Variables for class or objects are called fields
# Such functions are called methods of the class
# Collectively, the fields and methods can be referred to as the attributes of that class.
# Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. 
# They are called instance variables and class variables respectively.


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my names is {}.'.format(self.name))

p = Person('Nikolay')
p.say_hi()


# -----------------------------------------------
# Class And Object Variables
# All class members (including the data members) are public and all the methods are virtual in Python.

class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    # All class members are public. One exception:
    __privatevar = True

    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print("(initializing {})".format(self.name))

        # Adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot. Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    # We have marked the how_many method as a class method using a decorator.
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("T-1000")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
Robot.die(droid2)

Robot.how_many()



# -----------------------------------------------
# Inheritance

# The SchoolMember class in this situation is known as the base class or the superclass. 
# The Teacher and Student classes are called the derived classes or subclasses.

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    # In contrast, if we have not defined an __init__ method in a subclass, 
    # Python will call the constructor of the base class automatically.
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

# To use inheritance, we specify the base class names in a tuple
# it is called multiple inheritance.
members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
