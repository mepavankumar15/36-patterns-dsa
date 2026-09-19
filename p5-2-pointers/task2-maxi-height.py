"""┌──────────────────────────────────────────┐
│ 📋 TASK #11                              │
│                                          │
│ Pattern    : Two Pointers                │
│ Difficulty : Medium                      │
│                                          │
│ Problem:                                 │
│ Given an array of integers heights where │
│ heights[i] is the height of a vertical  │
│ line at position i, find two lines that  │
│ together with the x-axis form a          │
│ container that holds the most water.     │
│ Return the maximum amount of water.      │
│                                          │
│ Example:                                 │
│   Input  → heights = [1,8,6,2,5,4,8,3,7]│
│   Output → 49                            │
│                                          │
│   Why?                                   │
│   Lines at index 1(h=8) and index 8(h=7)│
│   width  = 8 - 1 = 7                    │
│   height = min(8, 7) = 7                │
│   area   = 7 × 7 = 49 ✅               │
│                                          │
│   Input  → heights = [1, 1]             │
│   Output → 1                             │
│                                          │
│ Trigger: "two lines" + "most water" +   │
│          "maximize area" → Two Pointers  │
│                                          │
│ Template : use STEP 4                    │
│                                          │
│ Key formula:                             │
│   area = (R - L) × min(h[L], h[R])     │
│                                          │
│ Key twist: which pointer moves?          │
│   → always move the SHORTER line inward │
│   → keeping taller line gives more hope │
│     of finding bigger area              │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

def maxi_height(arr):
    l = 0
    r = len(arr)-1
    result = 0

    while l < r:
        current_area = (r-l) * min(arr[l],arr[r])
        if arr[l] < arr[r]:
            l+=1
        else:
            r-=1
        result = max(result , current_area)
    return result

arr1 = [1,8,6,2,5,4,8,3,7]
print(maxi_height(arr1))