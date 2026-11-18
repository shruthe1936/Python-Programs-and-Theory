from functools import lru_cache

@lru_cache(maxsize=10)
def get_student(name):
    print("Fetching data from database")
    return "Student Name: " + name

print(get_student("Abc"))
print(get_student("Abc"))