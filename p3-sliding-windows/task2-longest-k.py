"""┌──────────────────────────────────────────┐
│ 📋 TASK #8                               │
│                                          │
│ Pattern    : String Sliding Window       │
│ Difficulty : Medium                      │
│                                          │
│ Problem:                                 │
│ Given a string s and an integer k,       │
│ find the length of the longest substring │
│ that contains at most K distinct         │
│ characters.                              │
│                                          │
│ Example:                                 │
│   Input  → s = "eceba", k = 2           │
│   Output → 3  ("ece")                   │
│                                          │
│   Input  → s = "aaabbb", k = 1          │
│   Output → 3  ("aaa" or "bbb")          │
│                                          │
│   Input  → s = "aabbcc", k = 2          │
│   Output → 4  ("aabb" or "bbcc")        │
│                                          │
│ Trigger: "longest substring" +           │
│          "at most K distinct" →          │
│          Sliding Window                  │
│                                          │
│ Template : STEP 4 from Pattern 3         │
│                                          │
│ Key twist: shrink condition is now       │
│   len(window) > k                        │
│   (too many distinct chars in window)   │
│   → remove leftmost char, move L        │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

s = input("enter the string : ") # s = aaabbb , k = 1
k = int(input("enter the K : "))

def longest_k(s, k):

    if k <=0:
        return 0

    windows = {}
    l = 0
    result = 0

    for r in range(len(s)):
        char = s[r]
        windows[char] = windows.get(char,0) + 1

        while len(windows) > k :
            left_char = s[l]
            windows[left_char] -=1
            if windows[left_char] == 0:
                del windows[left_char]
            l+=1 
        result = max(result , r - l +1)
    return result

print(longest_k(s,k)) # output is 3 the length of it




