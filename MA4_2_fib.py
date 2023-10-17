#!/usr/bin/env python3

from person import Person
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter as pc

@njit
def fib_nu(n):
    if n <= 1:
          return n
    else:
          return (fib_nu(n-1) + fib_nu(n-2))
def fib_py(n):
     if n <= 1:
        return n
     else:
        return (fib_py(n-1) + fib_py(n-2))

def main():
     x_val = [x for x in range(30,46)]
     y_py = []
     y_nu = []
     y_c = []
     for n in x_val:
         start = pc()
         fib = fib_py(n)
         end = pc()
         y_py = y_py + [round(end-start, 2)]
         start = pc()
         fib = fib_nu(n)
         end = pc()
         y_nu = y_nu + [round(end-start, 2)]
         f = Person(n)
         start = pc()
         fib = f.fib()
         end = pc()
         y_c = y_c + [round(end-start, 2)]
# create a plot
     plt.figure()
     plt.plot(x_val, y_py, 'ro-', label="pyhton")
     plt.plot(x_val, y_nu, 'bo-', label="numba")
     plt.plot(x_val, y_c, 'go-', label="c++")

     plt.legend()

     plt.xlabel("n")
     plt.ylabel("Time [s]")
# save the plot
plt.savefig("TimeComparison")
x_val = [x for x in range(20,31)]
y_py = []
y_nu = []

for n in x_val:
       start = pc()
       fib = fib_py(n)
       end = pc()
       y_py = y_py + [round(end-start, 2)]
       
       start = pc()
       fib = fib_nu(n)
       end = pc()
       y_nu = y_nu + [round(end-start, 2)]
 # create a plot
       plt.figure()
       plt.plot(x_val, y_py, 'ro-', label="pyhton")
       plt.plot(x_val, y_nu, 'bo-', label="numba")
       plt.legend()
       plt.xlabel("n")
       plt.ylabel("Time [s]")
# save the plot
       plt.savefig("TimeComparisonL")
       start = pc()
       fib = fib_nu(47)
       end = pc()
       print(f"fib(47)={fib} in {end-start} seconds using numba")
       f = Person(47)
       start = pc()
       fib = f.fib()
       end = pc()
       print(f"fib(47)={fib} in {end-start} seconds using c++")
if __name__ == '__main__':
	main()
# fib(47)=2971215073 in 56.32971319905482 seconds using numba
# fib(47)=-1323752223 in 54.728006588993594 seconds using c++