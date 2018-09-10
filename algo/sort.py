# Based on a pivot, split the array into < and > pivot
# not stable, empiraclly fastest, n^2 when choosing bad pivot
# O(n^2) worst case, O(n log n) average case, O(log n) space
def quicksort(lst):
    return lst

# Divide and conquer recursion
# stable
# O(n log n) time, O(n) space (recursive stack)
def mergesort(lst):
    return lst

# Build a heap to find each minimum in log n time
# not stable
# O(n log n) time, O(1) space (in-place heapify)
def heapsort(lst): 
    return lst

# For each element, swap it backwards into the right place
# stable, fastest on very small or partially sorted arrays 
# O(n^2) time, O(1) space
def insertionsort(lst):
    for i in range(1, len(lst)):
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i = i - 1
    return lst

# Find the minimum of each subarray and swap with the start of subarray
# O(n^2) time, O(1) space
def selectionsort(lst):
    min = float('inf')
    pos = 0
    for start in range(len(lst)):    
        for i in range(start,len(lst)):
            if lst[i] < min:
                min = lst[i]
                pos = i
        lst[start], lst[pos] = lst[pos], lst[start]
        pos = start
        min = float('inf')
    return lst

# Runs linear time if already sorted, but insertion sort does this too
# and works better on partially sorted arrays, so should be avoided
# O(n^2) time, O(1) space
def bubblesort(lst):
    for _ in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i+1] < lst[i]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

# Sort integers or strings of average digit/char size k by grouping each
# digit/char from least to most signifant
# O(nk) time, O(n + k) space 
def radixsort(lst):
    return lst

# Sort integers in a certain range length k by counting the number of integers
# for each integer in range
# O(n + k) time, O(k) space
def countingsort(lst):
    return lst

if __name__ == "__main__":
    print(selectionsort([5,2,4,1,3]))
    print(insertionsort([5,2,4,1,3]))
    print(bubblesort([5,2,4,1,3]))
