"""┌──────────────────────────────────────────┐
│ 📋 TASK #4                               │
│                                          │
│ Pattern    : String Two Pointers         │
│ Difficulty : Medium                      │
│                                          │
│ Problem:                                 │
│ Given a string s, return true if you     │
│ can make it a palindrome by removing     │
│ AT MOST one character.                   │
│                                          │
│ Example:                                 │
│   Input  → s = "abca"                   │
│   Output → True                          │
│   (remove 'b' → "aca" OR                │
│    remove 'c' → "aba", both palindromes) │
│                                          │
│   Input  → s = "abc"                    │
│   Output → False                         │
│                                          │
│ Trigger: "remove one character" +        │
│          "still a palindrome?" →         │
│          Two Pointers + one skip chance  │
│                                          │
│ Template : same STEP 4 template          │
│                                          │
│ Key twist: when L and R DON'T match,     │
│   you get ONE chance to skip either      │
│   s[L] or s[R] — try BOTH and see if    │
│   either side becomes a palindrome       │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

s1 = input("enter the string : ")
s= s1.lower()

def valid_palindrome_skip_char(s) :

    l = 0
    r = len(s)-1
    while l < r :

        if s[l] != s[r]:
           return isPalindrome(s, l+1, r) or isPalindrome(s, l , r-1) 
        l+=1
        r-=1
    return True


def isPalindrome(s,l ,r):

    while l < r : 

        if s[l] != s[r] :
            return False
        l+=1
        r-=1
    return True

print(valid_palindrome_skip_char(s))