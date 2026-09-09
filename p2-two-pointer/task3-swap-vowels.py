"""┌──────────────────────────────────────────┐
│ 📋 TASK #5                               │
│                                          │
│ Pattern    : String Two Pointers         │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given a string s, reverse ONLY the       │
│ vowels in the string and return it.      │
│ All other characters stay in place.      │
│                                          │
│ Example:                                 │
│   Input  → s = "hello"                  │
│   Output → "holle"                       │
│   (e and o swapped, h l l untouched)    │
│                                          │
│   Input  → s = "leetcode"               │
│   Output → "leotcede"                   │
│                                          │
│ Trigger: "swap from both ends" +         │
│          "only specific characters"      │
│          → Two Pointers with skip logic  │
│                                          │
│ Template : use STEP 4 above              │
│                                          │
│ Key twist: L and R only STOP when        │
│ both are pointing at vowels.             │
│ Skip non-vowels by moving the pointer.   │
│                                          │
│ Vowels = a e i o u (upper + lower case) │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

s= input("enter the string : ")

def is_vowel(ch):
    vowels = ["a","e" , "i" , "o", "u" , "A", "E" , "I" , "O" , "U"]
    if ch in vowels : 
        return True
    return False

def swap_vowels(s):
    s= list(s)
    l = 0
    r = len(s) -1

    while l < r :
    
        while l < r and not is_vowel(s[l]):
            l+=1
        while l < r and not is_vowel(s[r]):
            r-=1
        if l <r :
            s[l] , s[r] = s[r], s[l]
            l+=1
            r-=1
    return "".join(s)

print(swap_vowels(s))