# ThreadPoolExecutor  ->  an easy way to run many THREADS without
# creating each Thread by hand (like we did in multithread_1.py).
#
# A "pool" is just a group of ready-to-use worker threads.
# We hand tasks to the pool, and it runs them for us.

from concurrent.futures import ThreadPoolExecutor
import time


# Same simple functions we used before.
# This time each function returns a value instead of only printing,
# so we can collect the results back from the pool.
def square(x):
    return f"Number : {x}  Squared : {x**2}"


def Cube(x):
    return f"Number : {x}  Cubed  : {x**3}"


time_1 = time.time()

# "with" makes sure the pool is closed/cleaned up automatically.
# max_workers = how many threads can run at the same time.
with ThreadPoolExecutor(max_workers=2) as executor:

    # executor.map runs the function for every item in range(10).
    # It returns the results in the SAME order as the input.
    square_results = executor.map(square, range(10))
    cube_results = executor.map(Cube, range(10))

    # Loop through the results and print them.
    for line in square_results:
        print(line)

    for line in cube_results:
        print(line)


finished_time = time.time() - time_1

print(finished_time)
