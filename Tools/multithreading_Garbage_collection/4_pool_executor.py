# ProcessPoolExecutor  ->  same idea as ThreadPoolExecutor,
# but it uses separate PROCESSES instead of threads
# (like we did by hand in multiprocessing_2.py).
#
# Use processes for heavy CPU work (math, loops, crunching numbers),
# because processes can truly run on multiple CPU cores at once.

from concurrent.futures import ProcessPoolExecutor
import time


# Same simple functions, returning a value so we can collect results.
def square(x):
    return f"Number : {x}  Squared : {x**2}"


def Cube(x):
    return f"Number : {x}  Cubed  : {x**3}"


# IMPORTANT for processes on Windows:
# Everything that actually runs must be inside this "if" block,
# otherwise new processes will re-import the file and run it again.
if __name__ == "__main__":

    time_1 = time.time()

    # "with" closes the pool automatically when we are done.
    # max_workers = how many processes run at the same time.
    with ProcessPoolExecutor(max_workers=2) as executor:

        # executor.map runs the function for every number in range(10)
        # and gives the results back in order.
        square_results = executor.map(square, range(10))
        cube_results = executor.map(Cube, range(10))

        for line in square_results:
            print(line)

        for line in cube_results:
            print(line)

    finished_time = time.time() - time_1

    print(finished_time)
