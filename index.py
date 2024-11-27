import random
import time
import matplotlib.pyplot as plt

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swap was made in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break

# Function to generate random arrays and measure execution time
def measure_time_bubble_sort():
    sizes = [1000, 5000, 10000, 15000, 20000]
    times = []

    for size in sizes:
        # Generate random array
        data = [random.randint(1, 100000) for _ in range(size)]

        # Measure sorting time
        start_time = time.time()
        bubble_sort(data)
        end_time = time.time()

        times.append(end_time - start_time)
        print(f"Bubble Sort completed for size {size} in {end_time - start_time:.2f} seconds.")
    print(data)

    return sizes, times

# Measure performance and plot results
sizes, times = measure_time_bubble_sort()

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', color='red', label="Bubble Sort")
plt.title("Bubble Sort Performance")
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.grid()
plt.legend()
plt.show()

7, 12, 12, 14, 18, 18, 22, 31, 32, 33, 37, 43, 45, 47, 55, 57, 63, 74, 86, 87, 92, 93, 94, 95, 96, 101, 104, 114, 114, 118, 127, 132, 133, 134, 140, 143, 150, 156, 160, 169, 170, 172, 173, 174, 185, 190, 191, 193, 197, 215, 232, 237, 238, 243, 244, 244, 258, 267, 273, 274, 274, 279, 282, 282, 284, 291, 293, 304, 306, 308, 314, 318, 320, 323, 328, 328, 334, 334, 336, 343, 343, 361, 362, 371, 382, 392, 409, 419, 423, 427, 428, 428, 428, 430, 431, 441, 442, 446, 455, 457, 460, 462, 463, 464, 468, 470, 478, 481, 483, 489, 499, 499, 501, 523, 523, 524, 530, 534, 546, 546, 547, 556, 557, 562, 562, 567, 567, 583, 589, 589, 589, 595, 604, 607, 609, 612, 617, 617, 632, 636, 640, 642, 642, 649, 668, 673, 677, 682, 694, 696, 701, 705, 709, 719, 720, 722, 723, 728, 730, 730, 736, 742, 743, 744, 746, 765, 767, 771, 780, 782, 791, 796, 797, 801, 803,