import random


def generate_random_numbers(size, min_value, max_value, seed):
    random.seed(seed)
    return [random.randint(min_value, max_value) for _ in range(size)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

  
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquer (merge the two halves)
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    numbers = generate_random_numbers(50, 0, 100, seed=40)
    
    # Perform merge sort
    sorted_numbers = merge_sort(numbers.copy())
    
    print("Original Numbers:")
    print(numbers)
    print("\nConquer-Sorted (Merge Sort) Numbers:")
    print(sorted_numbers)
