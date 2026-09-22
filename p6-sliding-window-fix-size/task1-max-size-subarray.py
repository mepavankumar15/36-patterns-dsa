"""
┌──────────────────────────────────────────┐
│ 📋 TASK #12                              │
│                                          │
│ Pattern    : Sliding Window Fixed Size   │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given an array of integers and a number  │
│ k, find the maximum sum of any           │
│ contiguous subarray of size k.           │
│                                          │
│ Example:                                 │
│   Input  → arr=[2,1,5,1,3,2], k=3      │
│   Output → 9  (subarray [5,1,3])        │
│                                          │
│   Input  → arr=[2,3,4,1,5], k=2        │
│   Output → 7  (subarray [3,4])          │
│                                          │
│   Input  → arr=[1,2], k=3              │
│   Output → 0  (k > array length)        │
│                                          │
│ Trigger: "maximum sum" +                 │
│          "subarray of size k" →          │
│          Fixed Size Sliding Window       │
│                                          │
│ Template : use STEP 4 above              │
│                                          │
│ Key steps:                               │
│   1. Build first window sum (0 to k-1)  │
│   2. Slide → add arr[i], remove arr[i-k]│
│   3. Track max at every step            │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘
"""
arr = list(map(int, input("enter the array values : ").split()))
k = int(input("enter the K value : "))

def max_sum_array(arr,k):

    if len(arr) < k :
        return 0

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k , len(arr)):
        current_sum += arr[i]
        current_sum -= arr[i-k]

        max_sum = max(current_sum , max_sum)
    return max_sum

print(max_sum_array(arr,k))