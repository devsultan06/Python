import random
import time
import matplotlib.pyplot as plt

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to generate random arrays and measure execution time
def measure_time_insertion_sort():
    sizes = [1000, 5000, 10000, 15000, 20000]
    times = []

    for size in sizes:
        # Generate random array
        data = [random.randint(1, 100000) for _ in range(size)]

        # Measure sorting time
        start_time = time.time()
        insertion_sort(data)
        end_time = time.time()

        times.append(end_time - start_time)
        print(f"Insertion Sort completed for size {size} in {end_time - start_time:.2f} seconds.")

    return sizes, times

# Measure performance and plot results
sizes, times = measure_time_insertion_sort()

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', color='blue', label="Insertion Sort")
plt.title("Insertion Sort Performance")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid()
plt.legend()
plt.show()
