#!/usr/bin/env python3

# from person import Person
import random
import math
import matplotlib.pyplot as plt
from functools import reduce
from concurrent.futures import ProcessPoolExecutor
import time


# Function to implement MA4 1.2

def monte_carlo_volume_estimate(n, d):
    if d <= 0:
        return 0.0

    def is_inside(point):
        return sum(x ** 2 for x in point) <= 1

    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    inside_points = filter(is_inside, points)

    volume_estimate = reduce(lambda x, _: x + 1, inside_points, 0)

    return (volume_estimate / n) * (2 ** d)


def exact_volume(d):
    r = 1.0
    volume = (math.pi ** (d / 2)) / math.gamma(d / 2 + 1) * (r ** d)
    return volume


# Function to implement MA4 1.3 parallel
def monte_carlo_chunk(start, chunk_size, d):
    chunk_estimate = monte_carlo_volume_estimate(chunk_size, d)
    return chunk_estimate


def parallel_monte_carlo(n, d, num_processes):
    chunk_size = n // num_processes

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(
            executor.map(monte_carlo_chunk, range(0, n), [chunk_size] * num_processes, [d] * num_processes))

    return sum(results) / num_processes


# Function to implement MA4 1.1
def estimate_pi(n):
    inside_circle = 0

    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = math.sqrt(x ** 2 + y ** 2)

        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_approximation = 4 * inside_circle / n

    print("Number of points inside the circle:", inside_circle)
    print("Approximation of π ≈", pi_approximation)
    print("built-in constant π value:", math.pi)

    plt.figure(figsize=(6, 6))
    plt.scatter(x_inside, y_inside, color='red', s=1, label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='blue', s=1, label='Outside Circle')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.legend()
    filename = f'random_points_{n}_{pi_approximation}.png'
    plt.savefig(filename)  # save to disk as required
    plt.show()


def main():
    # f = Person(5)
    # print(f.get())
    # f.set(7)
    # print(f.get())

    # codes to run estimate_pi func
    n = int(input("Enter the number of random points (n): "))
    estimate_pi(n)

    # codes to run estimated_volume func
    n = int(input("Enter the number of random points (n): "))
    d = int(input("Enter the dimension (d): "))
    #
    estimated_volume = monte_carlo_volume_estimate(n, d)
    accurate_volume = exact_volume(d)
    #
    # print(f"Estimated volume of {d}-dimensional unit sphere (Monte Carlo): {estimated_volume}")
    # print(f"Accurate volume of {d}-dimensional unit sphere: {accurate_volume}")

    # codes to run estimated_volume func sequentially and parallely
    n = 1000000  # sample number
    d = 11  # d
    num_processes = 10  # parallel number

    start_time = time.perf_counter()
    estimated_volume = monte_carlo_volume_estimate(n, d)
    end_time = time.perf_counter()

    print(f"Estimated volume of {d}-dimensional unit sphere (Sequential): {estimated_volume}")
    print(f"Sequential Execution Time: {end_time - start_time} seconds")

    start_time = time.perf_counter()
    estimated_volume_parallel = parallel_monte_carlo(n, d, num_processes)
    end_time = time.perf_counter()

    print(
        f"Estimated volume of {d}-dimensional unit sphere (Parallel - {num_processes} processes): {estimated_volume_parallel}")
    print(f"Parallel Execution Time: {end_time - start_time} seconds")

    # MA4 1.3 Question 2: Which one was the fastest? How much faster and why? Answer: The parallel version is faster
    # than the serial version and uses multiple processes to compute Monte Carlo estimates simultaneously,
    # thus taking full advantage of the performance of multicore processors. Each process can generate random points
    # and perform estimation independently, which reduces overall computing time.


if __name__ == '__main__':
    main()
