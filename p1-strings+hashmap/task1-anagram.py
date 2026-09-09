"""┌──────────────────────────────────────────┐
│ 📋 TASK #1                               │
│                                          │
│ Pattern    : String + HashMap            │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given two strings s and t, return true   │
│ if t is an anagram of s, false otherwise.│
│                                          │
│ Example:                                 │
│   Input  → s = "anagram", t = "nagaram" │
│   Output → True                          │
│                                          │
│   Input  → s = "rat", t = "car"         │
│   Output → False                         │
│                                          │
│ Trigger: "anagram" = count characters    │
│          and compare → HashMap           │
│                                          │
│ Template: use STEP 4 above               │
│ Hint: You need TWO maps OR one map       │
│       with +1 for s and -1 for t         │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""



def string_anagram_compare(s,t):

        
        if(len(s)!=len(t)):
            return False
        
        freqs = {}

        for char in s : 
            freqs[char] = freqs.get(char,0) + 1

        for char in t:
             freqs[char] = freqs.get(char,0) - 1
        return all(freq==0 for freq in freqs.values())

s = input("enter the first string : ")
t = input("enter the second string : ")
print(string_anagram_compare(s,t))