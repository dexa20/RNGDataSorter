# Uclan ID - G21236306
# Name - Dinira Pathirana

import random
import time
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# Generates an array of unique random numbers within a specified range.
def generate_random_array(size, LOWER_LIMIT = 100000, UPPER_LIMIT = 999999):

    # Using random.sample to ensure uniqueness within the specified range
    return random.sample(range(LOWER_LIMIT, UPPER_LIMIT + 1), size)


# Writes the elements of an array into a text file.
def write_to_file(array, file_name):
    try:

        # Open the file in write mode ('w')
        with open(Path(__file__).parent / file_name, 'w') as file:

            # Iterate through each element in the array
            for element in array:

                # Write each element as a string followed by a newline character
                file.write(str(element) + '\n')

    except Exception as e:
        print(f"An error occurred: {e}")




#  ------------- SELECTION SORT ------------- #

# Applies the Selection Sort algorithm to the given array and counts the number of comparisons.
def selection_sort(arr, comparisons_count):

    # Iterate through the array elements
    for i in range(len(arr) - 1):

        # Assume the current index is the minimum
        min_index = i
        
        # Iterate through the remaining elements to find the minimum
        for j in range(i + 1, len(arr)):
            comparisons_count[0] += 1

            # Compare and update the minimum index if a smaller element is found
            if arr[min_index] > arr[j]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

#  ------------- SELECTION SORT ------------- #




#  --------------- MERGE SORT --------------- #

# Merges two subarrays into a single sorted array and counts the number of comparisons.
def merging(arr, left_arr, right_arr, comparisons_count):
    i = j = k = 0

    # Iterate through the left and right subarrays
    while i < len(left_arr) and j < len(right_arr):
        comparisons_count[0] += 1
        
        # Compare elements and merge them into the main array
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        elif left_arr[i] == right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
            arr[k] = right_arr[j]
            j += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy remaining elements from left subarray
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Applies the Merge Sort algorithm to the given array and counts the number of comparisons.
def merge_sort(arr, comparisons_count):
    if len(arr) <= 1:
        return

    # Calculate the midpoint of the array with consideration for even and odd lengths
    mid = (len(arr) + 1) // 2
    
    # Divide the array into left and right subarrays
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    # Recursively apply merge_sort to left and right subarrays
    merge_sort(leftArr, comparisons_count)
    merge_sort(rightArr, comparisons_count)

    # Merge the sorted left and right subarrays into the main array
    merging(arr, leftArr, rightArr, comparisons_count)

#  --------------- MERGE SORT --------------- #




#  --------------- QUICK SORT --------------- #

# Partitions the array and counts the number of comparisons during the Quick Sort process.
def partition(arr, begin, end, comparisons_count):
    pivot = arr[begin]
    i = begin + 1
    j = end

    # Iterate through the array to partition elements
    while i <= j:
        # Find the first element greater than the pivot from the left
        while i <= j and arr[i] <= pivot:
            comparisons_count[0] += 1
            i += 1

        # Find the first element smaller than the pivot from the right
        while i <= j and arr[j] > pivot:
            comparisons_count[0] += 1
            j -= 1
        # Swap elements if not yet crossed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot into its final position
    arr[begin], arr[j] = arr[j], arr[begin]

    return j


# Applies the Quick Sort algorithm to the given array and counts the number of comparisons.
def quick_sort(arr, begin, end, comparisons_count):
    if begin < end:

        # Partition the array and get the pivot index
        pivot = partition(arr, begin, end, comparisons_count)

        # Recursively apply quick_sort to the left and right subarrays
        quick_sort(arr, begin, pivot - 1, comparisons_count)
        quick_sort(arr, pivot + 1, end, comparisons_count)

#  --------------- QUICK SORT --------------- #




# Evaluates the execution time of a sorting algorithm, prints information about the sorting process, and writes the sorted array to a text file.
def evaluate_and_write_sorting_results(sort_function, array, *args, MILLISECONDS_PER_SECOND = 1000):

    # Initialize a list to store the number of comparisons during sorting
    comparisons_list = [0]

    # Record the start time
    start_time = time.perf_counter()

    # Make a copy of the original array for sorting
    sorted_array = array.copy()

    # Call the sorting function with the appropriate arguments
    if sort_function == quick_sort:
        sort_function(sorted_array, *args, comparisons_list)
    else:
        sort_function(sorted_array, comparisons_list)

    # Record the end time
    end_time = time.perf_counter()

    # Print information about the sorting process
    size = len(array)
    print(f"Array Size: {size}, Comparisons: {comparisons_list[0]}, Time: {(end_time - start_time) * MILLISECONDS_PER_SECOND:.6f} milliseconds")

    # Write sorted array to a file
    write_to_file(sorted_array, f"_{sort_function.__name__}_sorted_array_{size}")

    # Return the execution time of the sorting algorithm
    return (end_time - start_time) * MILLISECONDS_PER_SECOND


# Plots a bar chart comparing the execution times of three sorting algorithms for different dataset sizes.
def plot_execution_time(sizes, selection_sort_times, merge_sort_times, quick_sort_times):

    # Set the width of the bars
    bar_width = 0.2
    
    # The label locations
    index = np.arange(len(sizes))
    
    # Create a bar chart with execution times for each sorting algorithm
    plt.figure(figsize=(10, 6))
    plt.bar(index - bar_width, selection_sort_times, width=bar_width, label='Selection Sort')
    plt.bar(index, merge_sort_times, width=bar_width, label='Merge Sort')
    plt.bar(index + bar_width, quick_sort_times, width=bar_width, label='Quick Sort')

    # Set chart title and labels
    plt.title('Sorting Algorithm Performance')
    plt.xlabel('Dataset Size')
    plt.ylabel('Execution Time (miliseconds)')
    
    # Set x-axis ticks to be the dataset sizes
    plt.xticks(index, sizes)
    
    # Display legend, grid, and show the plot
    plt.legend()
    plt.grid(True)
    plt.show()

# Check if all numbers in the list are unique.
def are_all_datasets_unique(datasets, sizes):

    # Iterate through the datasets.
    for i, data in enumerate(datasets):

        # Create a name for the array.
        array_name = f"Array Size {sizes[i]}"
        
        # Initialize an empty list to keep track of seen numbers.
        seen_numbers = []

        # Iterate through each number in the current dataset.
        for num in data:

            # Check if the current number is already in the seen_numbers list.
            if num in seen_numbers:

                # If duplicate found, print a message and return False.
                print(f"\nThere are duplicate elements in the {array_name}.")
                return False
            
            # If the number is unique, append it to the seen_numbers list.
            seen_numbers.append(num)

        # If the loop completes without finding duplicates, print a message.
        print(f"\nAll elements in the {array_name} are unique.")

    # If no duplicates are found in any dataset, return True.
    return True



# Main function to demonstrate sorting algorithms' performance evaluation and plot the results.
def main():
    
    # Define dataset sizes
    sizes = [100, 1000, 10000]
    
    # Lists to store execution times for each sorting algorithm
    selection_sort_times = []
    merge_sort_times = []
    quick_sort_times = []

    # Generate arrays for each dataset size
    datasets = [generate_random_array(size) for size in sizes]

    # Evidence of a mechanism ensuring uniqueness in randomly generated arrays.
    are_all_datasets_unique(datasets, sizes)

    # Evaluate and print results for Selection Sort
    print("\nSelection Sort:")
    for data in datasets:
        execution_time = evaluate_and_write_sorting_results(selection_sort, data)
        selection_sort_times.append(execution_time)

    # Evaluate and print results for Merge Sort 
    print("\nMerge Sort:")
    for data in datasets:
        execution_time = evaluate_and_write_sorting_results(merge_sort, data)
        merge_sort_times.append(execution_time)

    # Evaluate and print results for Quick Sort
    print("\nQuick Sort:")
    for data in datasets:
        execution_time = evaluate_and_write_sorting_results(quick_sort, data, 0, len(data) - 1)
        quick_sort_times.append(execution_time)

    # Plot the execution times of sorting algorithms
    plot_execution_time(sizes, selection_sort_times, merge_sort_times, quick_sort_times)

# This block ensures that the 'main' function is called only if the script is executed as the main program.
if __name__ == "__main__":
    main()
