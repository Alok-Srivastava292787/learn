from copy import copy, deepcopy
a=[4,6,[7,8]]
b=copy(a)

print(f"shallow copy \na={a}\nb={b}")

a.append(10)
#b=copy(a)
print(f"after appending source output of shallow copy \na={a}\nb={b}")

a[2].append(9)
#b=copy(a)
print(f"after adding nested list copy \na={a}\nb={b}")

b=deepcopy(a)
print(f"using deepcopy copy \na={a}\nb={b}")

from functools import wraps

def decorator_function(func):
    """A simple decorator to announce the function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing the Fibonacci series generator...")
        result = func(*args, **kwargs)
        print("Execution completed.")
        return result
    return wrapper

@decorator_function
def generate_fibonacci_triangular(n):
    """
    Generate Fibonacci series up to `n` numbers and display them in triangular format.
    Demonstrates the use of break, continue, and pass.
    """
    a, b = 0, 1
    count = 0
    fib_series = []

    while count < n:
        if count == 0:
            fib_series.append(a)
            count += 1
            continue  # Skip the rest of the loop for the first iteration
        elif count == 1:
            fib_series.append(b)
            count += 1
            pass  # Does nothing, just a placeholder
        else:
            next_fib = a + b
            if next_fib > 100:  # Example condition to demonstrate break
                print("Breaking the loop as Fibonacci number exceeds 100.")
                break
            fib_series.append(next_fib)
            a, b = b, next_fib
            count += 1

    # Display Fibonacci numbers in triangular format
    print("Fibonacci series in triangular format:")
    for i in range(len(fib_series)):
        print(" ".join(str(fib_series[j]) for j in range(i + 1)))
import random
from functools import wraps

def prime_decorator(func):
    """Decorator to announce the execution of the prime number generator."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting prime number generation...")
        try:
            result = func(*args, **kwargs)
            print("Prime number generation completed.")
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper

@prime_decorator
@prime_decorator
def generate_n_digit_prime(n):
    """
    Generate the smallest and largest n-digit prime numbers.
    Demonstrates try/except for error handling.
    """
    try:
        if n <= 0:
            raise ValueError("The number of digits must be greater than 0.")
        
        # Define the range for n-digit numbers
        lower_bound = 10**(n-1)
        upper_bound = 10**n - 1

        # Find the smallest n-digit prime
        smallest_prime = None
        for num in range(lower_bound, upper_bound + 1):
            if is_prime(num):
                smallest_prime = num
                break

        # Find the largest n-digit prime
        largest_prime = None
        for num in range(upper_bound, lower_bound - 1, -1):
            if is_prime(num):
                largest_prime = num
                break

        if smallest_prime and largest_prime:
            print(f"Smallest {n}-digit prime number: {smallest_prime}")
            print(f"Largest {n}-digit prime number: {largest_prime}")
            return smallest_prime, largest_prime
        else:
            print(f"No {n}-digit prime numbers found.")
            return None, None

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Helper function remains unchanged
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
# Example usage
if __name__ == "__main__":
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    generate_fibonacci_triangular(num)
    try:
        n = int(input("Enter the number of digits for the prime number: "))
        generate_n_digit_prime(n)
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
