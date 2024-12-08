import java.util.Random;

public class MergeSort {

    // Merge Sort Implementation
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

            // Merge the sorted halves
            merge(arr, leftHalf, rightHalf);
        }
    }

    // Merge two sorted arrays
    private static void merge(int[] arr, int[] leftHalf, int[] rightHalf) {
        int i = 0, j = 0, k = 0;

        // Compare and merge elements from both halves
        while (i < leftHalf.length && j < rightHalf.length) {
            if (leftHalf[i] < rightHalf[j]) {
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

    // Function to generate random arrays and measure execution time
    public static void measureTimeMergeSort() {
        int[] sizes = {1000, 5000, 10000, 15000, 20000};

        for (int size : sizes) {
            // Generate random array
            int[] data = new Random().ints(size, 1, 100001).toArray();

            // Measure sorting time
            long startTime = System.currentTimeMillis();
            mergeSort(data);
            long endTime = System.currentTimeMillis();

            System.out.printf("Merge Sort completed for size %d in %.2f seconds.%n", size, (endTime - startTime) / 1000.0);
        }
    }

    // Main method to execute the program
    public static void main(String[] args) {
        System.out.println("Measuring Merge Sort Performance:");
        measureTimeMergeSort();
    }
}
