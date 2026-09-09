"""┌──────────────────────────────────────────┐
│ 📋 TASK #3                               │
│                                          │
│ Pattern    : String Two Pointers         │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given a string s, return true if it is   │
│ a palindrome, considering only           │
│ alphanumeric characters and ignoring     │
│ case.                                    │
│                                          │
│ Example:                                 │
│   Input  → "A man, a plan, a canal: Panama"│
│   Output → True                          │
│                                          │
│   Input  → "race a car"                 │
│   Output → False                         │
│                                          │
│ Trigger: "reads same forwards/backwards" │
│          + ignore non-letters → Two      │
│          Pointers with a skip condition  │
│                                          │
│ Template : use STEP 4 above              │
│                                          │
│ Key twist: What do you do when your      │
│ pointer lands on a space or comma?       │
│ → skip it and move the pointer           │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

s1 = input("enter the string : ")
s= s1.lower()

def valid_palindrome_alnumeric(s) :

    l = 0
    r = len(s)-1
    while l < r :

        while l < r and not s[l].isalnum():
            l+=1

        while l < r and not s[r].isalnum():
            r-=1

        if s[l] != s[r]:
            return False
        
        l+=1
        r-=1
    return True

print(valid_palindrome_alnumeric(s))