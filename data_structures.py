# data_structures.py

# 📌 1. Prefix Sum Array
def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

# 📌 2. Suffix Sum Array
def suffix_sum(arr):
    suffix = [0] * (len(arr) + 1)
    for i in range(len(arr) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]
    return suffix[:-1]

# 📌 3. Two Pointers Technique (Find Pair with Target Sum)
def two_pointers(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (arr[left], arr[right])
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

# 📌 4. Sliding Window (Find max sum of subarray of size k)
def sliding_window(arr, k):
    max_sum = float('-inf')
    window_sum = sum(arr[:k])  # Initial window sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# 📌 5. Kadane's Algorithm (Maximum Subarray Sum)
def max_subarray_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# 📌 6. Binary Search (Iterative)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right -= 1
    return -1  # Target not found

# 📌 7. Dutch National Flag Algorithm (Sort 0s, 1s, 2s)
def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# 📌 8. Rotate Array (Using Reversal Algorithm)
def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

# 📌 9. Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# 📌 10. Moore’s Voting Algorithm (Find Majority Element)
def majority_element(arr):
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate if arr.count(candidate) > len(arr) // 2 else None

# 📌 11. Merge Intervals
def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # Overlapping
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# 📌 12. Function to Print Example Outputs
def print_example_outputs():
    arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    target = 7

    print("Prefix Sum:", prefix_sum(arr))
    print("Suffix Sum:", suffix_sum(arr))
    print("Two Pointers (Sum 7):", two_pointers(arr, target))
    print("Sliding Window (Max sum of 3 elements):", sliding_window(arr, 3))
    print("Max Subarray Sum:", max_subarray_sum(arr))
    print("Binary Search (index of 3):", binary_search(arr, 3))
    print("Dutch National Flag:", dutch_national_flag([2, 0, 1, 2, 1, 0]))
    print("Rotate Array (2 positions):", rotate_array(arr, 2))
    print("Merge Sort:", merge_sort(arr))
    print("Majority Element:", majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]))
    print("Merge Intervals:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print()
    print()
    print("""
    arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    target = 7

    print("Prefix Sum:", prefix_sum(arr))
    print("Suffix Sum:", suffix_sum(arr))
    print("Two Pointers (Sum 7):", two_pointers(arr, target))
    print("Sliding Window (Max sum of 3 elements):", sliding_window(arr, 3))
    print("Max Subarray Sum:", max_subarray_sum(arr))
    print("Binary Search (index of 3):", binary_search(arr, 3))
    print("Dutch National Flag:", dutch_national_flag([2, 0, 1, 2, 1, 0]))
    print("Rotate Array (2 positions):", rotate_array(arr, 2))
    print("Merge Sort:", merge_sort(arr))
    print("Majority Element:", majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]))
    print("Merge Intervals:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    """)
