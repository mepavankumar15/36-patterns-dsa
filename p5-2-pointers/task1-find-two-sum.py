"""┌──────────────────────────────────────────┐
│ 📋 TASK #10                              │
│                                          │
│ Pattern    : Two Pointers                │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given a sorted array of integers and a  │
│ target integer, return the indices of   │
│ the two numbers that add up to target.  │
│ Assume exactly one solution exists.     │
│ Indices are 1-based.                    │
│                                          │
│ Example:                                 │
│   Input  → nums=[2,7,11,15], target=9  │
│   Output → [1, 2]                       │
│   (nums[1] + nums[2] = 2 + 7 = 9)      │
│                                          │
│   Input  → nums=[2,3,4], target=6      │
│   Output → [1, 3]                       │
│                                          │
│ Trigger: "sorted array" + "two numbers" │
│          + "sum to target" → classic    │
│          Two Pointers                   │
│                                          │
│ Template : use STEP 4 above             │
│                                          │
│ Key twist: output is 1-based indices    │
│   so return [L+1, R+1] not [L, R]      │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE      │
└──────────────────────────────────────────┘"""

def two_sum(arr,target):
    
    l = 0
    r = len(arr) -1

    while l < r :

        current_sum = arr[l]+arr[r]
        if current_sum == target:
            return [l+1 ,r+1]
        elif current_sum < target:
            l+=1
        else:
            r-=1
    return []

arr = [2,7,9,15]
target = 9
print(two_sum(arr,target))

