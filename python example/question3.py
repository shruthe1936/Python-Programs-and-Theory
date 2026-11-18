import gc

# Reference Counting
a = [10, 20, 30]
b = a

del a
print(b)

del b

# Cyclic Garbage Collection
class Student:
    pass

a = Student()
b = Student()

a.friend = b
b.friend = a

del a
del b

print(gc.collect())