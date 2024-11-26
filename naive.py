import random

# Generate random integers with a fixed seed
def generate_random_numbers(size, min_value, max_value, seed):
    random.seed(seed)
    return [random.randint(min_value, max_value) for _ in range(size)]

# Naive sort implementation (Bubble Sort for simplicity)
def naive_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    # Generate 50 random integers between 0 and 100
    numbers = generate_random_numbers(50, 0, 100, seed=40)
    
    # Perform naive sort
    sorted_numbers = naive_sort(numbers.copy())
    
    print("Original Numbers:")
    print(numbers)
    print("\nNaively Sorted Numbers:")
    print(sorted_numbers)
