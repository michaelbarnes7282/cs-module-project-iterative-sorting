# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps_occured = True

    while swaps_occured:
        swaps_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occured = True

    return arr

    # for i in range(len(arr)):
    #     sorted = True
    #     for j in range(len(arr) - i - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #             sorted = False

    #     if sorted:
    #         break

    # return arr

def recursive_bubble_sort(arr, unsorted_length):

    for i in range(unsorted_length - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    if unsorted_length > 1:
        recursive_bubble_sort(arr, unsorted_length - 1)
    return arr
arr = [13, 154, 1, 6, 3, 7, 8, 5, 300, 64]
print(recursive_bubble_sort(arr, len(arr)))

# def rbs(arr):
#     if len(arr) > 0:
#         return rbs(arr[:len(arr) - 1])

#     for i in range

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if maximum:
        buckets = [0 for i in range(maximum + 1)]
    else:
        if len(arr) > 0:
            maximum = max(arr)
            buckets = [0 for i in range(maximum + 1)]
        else:
            buckets = [0 for i in range(len(arr) + 1)]
    
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[i] += 1

    nums_item_before = 0
    for i, count in enumerate(buckets):
        buckets[i] = nums_item_before
        nums_item_before += count
    
    sorted_arr = [None] * len(arr)

    for item in arr:
        sorted_arr[buckets[item]] = item
    return sorted_arr
    
