# Regular Class
class Student:
    pass

s1 = Student()

s1.name = "Arun"
s1.age = 20

print(s1.name)
print(s1.age)


# Class Using __slots__
class StudentSlots:
    __slots__ = ['name', 'age']

s2 = StudentSlots()

s2.name = "Arun"
s2.age = 20

print(s2.name)
print(s2.age)