# Quicksort (qsort)

## What is a Quicksort?
Quicksort is a sorting algorithm which is faster than selection sort. It works via paritioning sub-arrays relative to a pivot value. 

Quicksort is also a _divide and conquer_ algorithm, where a problem is divided or decreased until it becomes the base case; illustrates the usefulness of recursive solutions.

## How Does Quicksort Work?
0. Set a base case
    - If the array is less than two elements, the array is already considered sorted (the qsort will already know how to sort this).
1. Pick a pivot value
2. Partition the array into a left and right sub-arrays
	- Left partition represents all values less than pivot value.
	- Right partition represent all values greater than pivot value.
3. Call quicksort recursively on the sub array, concatenate like this:
    - `qsort(leftPartition) + [pivotValue] + qsort(rightPartition)`

## How fast is Quicksort?
The speed of the sort is dependent upon the pivot value, which determines the elements of both the left and right partitions. Also, Quicksort (at best case) happens in `O(n log n) ` time, making it faster (on average) than selection sort. At worst case, Quicksort requires `O(n squared)` time.