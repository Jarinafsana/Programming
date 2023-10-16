import random
import math
import matplotlib.pyplot as plt

def monte_carlo_pi(n):
    inside_circle = 0

    x_inside = []  # Lists to store coordinates for the plot
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(n):
        x = random.uniform(0, 1)  # Generate a random x-coordinate between 0 and 1
        y = random.uniform(0, 1)  # Generate a random y-coordinate between 0 and 1
        distance = x**2 + y**2  # Calculate the distance from the origin (0,0)

        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # Approximation of π
    pi_approximation = (inside_circle / n) * 4

    return inside_circle, pi_approximation, x_inside, y_inside, x_outside, y_outside

def main(n):
    inside_circle, pi_approximation, x_inside, y_inside, x_outside, y_outside = monte_carlo_pi(n)

    # Print the number of points inside the circle and the approximation of π
    print(f"Number of points inside the circle: {inside_circle}")
    print(f"Approximation of π ≈ {pi_approximation}")

    # Print the built-in constant π (math.pi) for comparison
    print(f"Builtin constant π (math.pi): {math.pi}")

    # Create a figure to visualize points inside and outside the circle
    plt.figure(figsize=(8, 8))
    plt.scatter(x_inside, y_inside, color='red', marker='o', label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='blue', marker='o', label='Outside Circle')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Monte Carlo π Approximation')
    plt.legend()
    plt.savefig('monte_carlo_pi.png')
    plt.show()

if __name__ == "__main__":
    n_values = [1000, 10000, 100000]
    for n in n_values:
        print(f"Results for n = {n}:")
        main(n)
        print()

