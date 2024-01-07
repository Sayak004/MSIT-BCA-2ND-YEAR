# ##__init__()
# class Main:
#   def __init__(self, test1, test2):
#     self.x = test1
#     self.y = test2

# p1 = Main(123.69, 36.236)

# print(p1.x)
# print(p1.y)



# ##Inheritance
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(example):
#     print(example.firstname, example.lastname)

# class Student(Person):
#   pass

# class Student2(Student):
#   pass

# x = Student2("Rahul", "Roy")
# x.printname()


##super()


# class Person:
#   def __init__(xyz, fname, lname):
#     xyz.firstname = fname
#     xyz.lastname = lname

#   def printname(abc):
#     print(abc.firstname, abc.lastname)

# class Student(Person):
#   def __init__(xyz,fname, lname):
#     super().__init__(fname, lname)

# x = Student("Rahul", "Roy")
# x.printname()