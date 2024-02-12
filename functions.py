# inbuilt functions
number = max(89, 70, 12, 30)
print(number)

x = min(78, 43, 34, 1)
print(x)

z = pow(2, 3)
print(z)


# user-defined functions
def name():
    print("Mark")


name()  # calling a function


def student():
    name = "vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# parameters/variables
def students(name, age, course):
    print(name, age, course)


students("vincent", 18, "MIT")
students("Grace", 17, "Cyber security")
students("Allan", 19, "MIT")
students("Mark", 16, "Full stack")
students("Dedan", 18, "MIT")
students("vincent", 18, "MIT")
students("vincent", 18, "MIT")


# employees
def employees(Fullname, age, gender, position, salary, ):
    print(Fullname, age, gender, position, salary)


employees("vincent", 18, "male", "manager", "ksh 20,000")
employees("Joy", 17, "female", "Clerk", "ksh 10,000")
employees("Dedan", 19, "male", "CEO", "ksh 450,000")
employees("Stacey", 17, "female", "worker", "ksh 35,000")
employees("Lewis", 20, "male", "manager", "ksh 305,000")
