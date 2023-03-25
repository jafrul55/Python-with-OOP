# Multithreading in Python 
# Python work with multiple tasks
from time import sleep, perf_counter
from threading import Thread

start_time = perf_counter()

def task(start, end):
    for i in range(start, end):
        print(f"Starting Task - {i}")
        sleep(1)
        print('\n')

t1 = Thread(target=task, args=(1, 5))
t2 = Thread(target=task, args=(6, 11))

t1.start()
t2.start()

t1.join()
t2.join()# Multithreading in Python 
# Python work with multiple tasks
from time import sleep, perf_counter
from threading import Thread

start_time = perf_counter()

def task(start, end):
    for i in range(start, end):
        print(f"Starting Task - {i}")
        sleep(1)
        print('\n')

t1 = Thread(target=task, args=(1, 5))
t2 = Thread(target=task, args=(6, 11))

# Start the threads
t1.start()
t2.start()

# Join the threads
t1.join()
t2.join()

end_time = perf_counter()
print(f"Total time = {end_time - start_time}")


end_time = perf_counter()
print(f"Total time = {end_time - start_time}")