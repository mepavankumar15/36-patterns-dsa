"""┌──────────────────────────────────────────┐
│ 📋 TASK #6                               │
│                                          │
│ Pattern    : String Sliding Window       │
│ Difficulty : Medium                      │
│                                          │
│ Problem:                                 │
│ Given a string s, find the length of     │
│ the longest substring that contains      │
│ no repeating characters.                 │
│                                          │
│ Example:                                 │
│   Input  → s = "abcabcbb"               │
│   Output → 3  ("abc")                   │
│                                          │
│   Input  → s = "bbbbb"                  │
│   Output → 1  ("b")                     │
│                                          │
│   Input  → s = "pwwkew"                 │
│   Output → 3  ("wke")                   │
│                                          │
│ Trigger: "longest substring" +           │
│          "no repeating" → Sliding Window │
│                                          │
│ Template : use STEP 4 above              │
│                                          │
│ Shrink condition:                        │
│   when any char appears more than once  │
│   inside your window → move L forward   │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

s = input("enter the string : ") #abcabcbb

def longest_string_norp (s):  # here L, R starts at index 0
    s= s.lower()

    window = {}
    L = 0
    result = 0 

    for R in range(len(s)):
        char = s[R]
        window[char] = window.get(char, 0) + 1

        while window[char] > 1 :
            left_char = s[L]
            window[left_char] -=1
            L+=1
        result = max(result , R - L + 1)
    return result 

print(longest_string_norp(s))

        

