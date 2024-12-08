import java.util.Random;

public class ModifiedMergeSort {

    // Modified Merge Sort with Priority Merge
    public static void mergeSort(int[] arr) {
        if (arr.length > 1) {
            // Find the middle point
            int mid = arr.length / 2;

            // Split the array into two halves
            int[] leftHalf = new int[mid];
            int[] rightHalf = new int[arr.length - mid];

            System.arraycopy(arr, 0, leftHalf, 0, mid);
            System.arraycopy(arr, mid, rightHalf, 0, arr.length - mid);

            // Recursively sort both halves
            mergeSort(leftHalf);
            mergeSort(rightHalf);

            // Merge the sorted halves using priority-based merge
            priorityMerge(arr, leftHalf, rightHalf);
        }
    }

    // Modified merge logic with priority
    private static void priorityMerge(int[] arr, int[] leftHalf, int[] rightHalf) {
        int i = 0, j = 0, k = 0;

        // Compare and merge elements based on priority
        while (i < leftHalf.length && j < rightHalf.length) {
            if (hasHigherPriority(leftHalf[i], rightHalf[j])) {
                arr[k++] = leftHalf[i++];
            } else {
                arr[k++] = rightHalf[j++];
            }
        }

        // Copy remaining elements from leftHalf
        while (i < leftHalf.length) {
            arr[k++] = leftHalf[i++];
        }

        // Copy remaining elements from rightHalf
        while (j < rightHalf.length) {
            arr[k++] = rightHalf[j++];
        }
    }

    // Function to determine priority (e.g., odd numbers have higher priority than even)
    private static boolean hasHigherPriority(int a, int b) {
        // Priority: odd numbers > even numbers; if equal, compare values directly
        if ((a % 2 == 1) && (b % 2 == 0)) {
            return true;
        } else if ((a % 2 == 0) && (b % 2 == 1)) {
            return false;
        }
        return a <= b; // Fall back to normal comparison if priorities are equal
    }

    // Function to generate random arrays and measure execution time
    public static void measureTimeModifiedMergeSort() {
        int[] sizes = {1000, 5000, 10000, 15000, 20000};

        for (int size : sizes) {
            // Generate random array
            int[] data = new Random().ints(size, 1, 100001).toArray();

            // Measure sorting time
            long startTime = System.currentTimeMillis();
            mergeSort(data);
            long endTime = System.currentTimeMillis();

            System.out.printf("Modified Merge Sort completed for size %d in %.2f seconds.%n", size, (endTime - startTime) / 1000.0);
        }
    }

    // Main method to execute the program
    public static void main(String[] args) {
        System.out.println("Measuring Modified Merge Sort Performance:");
        measureTimeModifiedMergeSort();
    }
}
