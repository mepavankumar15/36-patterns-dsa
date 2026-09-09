"""┌──────────────────────────────────────────┐
│ 📋 TASK #2                               │
│                                          │
│ Pattern    : String + HashMap            │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given a string s, find the FIRST         │
│ character that appears only once         │
│ and return its index.                    │
│ If no such character exists, return -1.  │
│                                          │
│ Example:                                 │
│   Input  → s = "leetcode"               │
│   Output → 0  (first unique is 'l')     │
│                                          │
│   Input  → s = "aabb"                   │
│   Output → -1  (no unique character)    │
│                                          │
│ Trigger: "find character that appears    │
│           only once" = count frequency   │
│           → HashMap                      │
│                                          │
│ Template : use STEP 4 from Pattern 1     │
│                                          │
│ Hint     : You need TWO passes           │
│            through the string.           │
│            Pass 1 → build the map        │
│            Pass 2 → find first count=1  │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""


def first_occurance_char(s):

    freq={}

    for char in s:
        freq[char] = freq.get(char,0) +1

    for i in range(len(s)):
        if freq[s[i]] ==1:
            return i
    return -1



s= input("enter the text : ")

result = first_occurance_char(s)
print(result)