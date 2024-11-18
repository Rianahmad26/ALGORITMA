import time

def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort_ascending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort_ascending(less_than_pivot) + [pivot] + quick_sort_ascending(greater_than_pivot)

def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        greater_than_pivot = [x for x in arr[1:] if x >= pivot]
        less_than_pivot = [x for x in arr[1:] if x < pivot]
        return quick_sort_descending(greater_than_pivot) + [pivot] + quick_sort_descending(less_than_pivot)

# Array A dan B
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Array asli A:", A)
print("Array asli B:", B)

start_time = time.time()
sorted_A_bubble_asc = bubble_sort_ascending(A.copy())
bubble_sort_time_A_asc = time.time() - start_time
print("Bubble Sort (ascending) untuk A:", sorted_A_bubble_asc)
print(f"Waktu komputasi: {bubble_sort_time_A_asc:.6f} detik")

start_time = time.time()
sorted_B_bubble_desc = bubble_sort_descending(B.copy())
bubble_sort_time_B_desc = time.time() - start_time
print("Bubble Sort (descending) untuk B:", sorted_B_bubble_desc)
print(f"Waktu komputasi: {bubble_sort_time_B_desc:.6f} detik")

start_time = time.time()
sorted_A_quick_asc = quick_sort_ascending(A.copy())
quick_sort_time_A_asc = time.time() - start_time
print("Quick Sort (ascending) untuk A:", sorted_A_quick_asc)
print(f"Waktu komputasi: {quick_sort_time_A_asc:.6f} detik")

start_time = time.time()
sorted_B_quick_desc = quick_sort_descending(B.copy())
quick_sort_time_B_desc = time.time() - start_time
print("Quick Sort (descending) untuk B:", sorted_B_quick_desc)
print(f"Waktu komputasi: {quick_sort_time_B_desc:.6f} detik")

#Penjelasan Keefektifitasannya

#Quick Sort lebih efektif daripada Bubble Sort untuk mengurutkan array `A` (descending) dan `B` (ascending) 
# karena Quick Sort bekerja lebih cepat dengan membagi array menjadi bagian-bagian kecil dan mengurutkannya secara efisien. 
# Sementara itu, Bubble Sort lambat karena harus membandingkan dan menukar elemen satu per satu berulang kali, 
# sehingga memakan waktu lama, terutama untuk array besar. Jadi, untuk mengurutkan array seperti `A` dan `B`, 
# Quick Sort jelas lebih cepat dan cocok digunakan dibandingkan Bubble Sort.