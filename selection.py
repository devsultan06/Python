import random
import time
import matplotlib.pyplot as plt

# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Function to measure execution time
def measure_time_selection_sort(data_sizes):
    times = []
    for size in data_sizes:
        # Generate random data
        data = [random.randint(0, 10000) for _ in range(size)]
        # Measure time
        start_time = time.time()
        selection_sort(data)
        end_time = time.time()
        times.append(end_time - start_time)
    print(data)
    return times

# Data sizes
data_sizes = [1000, 5000, 10000, 15000, 20000]

# Measure times for Selection Sort
selection_sort_times = measure_time_selection_sort(data_sizes)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, selection_sort_times, label="Selection Sort", marker='o', color='green')
plt.xlabel("Array Size")
plt.ylabel("Time Taken (seconds)")
plt.title("Performance of Selection Sort")
plt.legend()
plt.grid(True)
plt.savefig("selection_sort_performance.png")  # Save the graph as a PNG file
plt.show()

# Display Results
print("Data Sizes:", data_sizes)
print("Selection Sort Times:", selection_sort_times)

0, 0, 0, 0, 0, 1, 2, 2, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 15, 15, 15, 16, 16, 16, 16, 17, 17, 18, 18, 19, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 29, 30, 31, 31, 31, 31, 31, 32, 32, 33, 34, 34, 35, 36, 36, 36, 36, 37, 37, 37, 38, 39, 39, 40, 41, 41, 42, 42, 42, 43, 43, 44, 45, 45, 46, 46, 46, 46, 47, 47, 47, 48, 48, 49, 50, 50, 50, 51, 52, 52, 52, 53, 54, 55, 55, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 60, 61, 61, 61, 62, 62, 62, 62, 63, 64, 65, 65, 65, 66, 66, 67, 67, 68, 69, 69, 70, 70, 72, 72, 74, 74, 75, 75, 75, 75, 76, 76, 76, 77, 77, 79, 79, 80, 80, 80, 80, 82, 82, 82, 82, 83, 83, 84, 85, 85, 85, 86, 86, 86, 87, 88, 88, 88, 88, 89, 89, 89, 90, 90, 91, 92, 93, 95, 95, 95, 95, 96, 97, 98, 99, 100, 101, 102, 102,