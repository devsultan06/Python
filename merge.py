import random
import time
import matplotlib.pyplot as plt

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to generate random arrays and measure execution time
def measure_time_merge_sort():
    sizes = [1000, 5000, 10000, 15000, 20000]
    times = []

    for size in sizes:
        # Generate random array
        data = [random.randint(1, 100000) for _ in range(size)]

        # Measure sorting time
        start_time = time.time()
        merge_sort(data)
        end_time = time.time()

        times.append(end_time - start_time)
        print(f"Merge Sort completed for size {size} in {end_time - start_time:.2f} seconds.")
    print(data)

    return sizes, times

# Measure performance and plot results
sizes, times = measure_time_merge_sort()

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', color='blue', label="Merge Sort")
plt.title("Merge Sort Performance")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid()
plt.legend()
plt.show()
