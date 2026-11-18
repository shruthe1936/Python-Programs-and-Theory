class Age:
    def __get__(self, obj, owner):
        return obj._age

    def __set__(self, obj, value):
        if value < 0:
            print("Age cannot be negative")
        else:
            obj._age = value


class Student:
    age = Age()


s = Student()

s.age = 20
print(s.age)

s.age = -5