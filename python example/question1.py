import threading
import multiprocessing

def task1():
    print("Writing notes")

def task2():
    print("Listening to lecture")

def task3():
    print("Studying Python")

def task4():
    print("Studying Java")

if __name__ == "__main__":

    # Multithreading
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Multiprocessing
    p1 = multiprocessing.Process(target=task3)
    p2 = multiprocessing.Process(target=task4)

    p1.start()
    p2.start()

    p1.join()
    p2.join()