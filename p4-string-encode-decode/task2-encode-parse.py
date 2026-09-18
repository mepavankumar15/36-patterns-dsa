"""┌──────────────────────────────────────────┐
│ 📋 TASK #9                               │
│                                          │
│ Pattern    : String Encoding & Parsing   │
│ Difficulty : Easy                        │
│                                          │
│ Problem:                                 │
│ Given a string s, perform Run Length     │
│ Encoding and return the compressed       │
│ string. If the compressed string is NOT  │
│ shorter than original → return original. │
│                                          │
│ Example:                                 │
│   Input  → "aabcccdddd"                 │
│   Output → "a2b1c3d4"                   │
│   (shorter → return compressed)          │
│                                          │
│   Input  → "abcd"                       │
│   Output → "abcd"                        │
│   (a1b1c1d1 is longer → return original)│
│                                          │
│   Input  → "aaabbc"                     │
│   Output → "a3b2c1"                     │
│                                          │
│ Trigger: "compress repeated characters" │
│          "run length encoding" →         │
│          Encoding & Parsing              │
│                                          │
│ Template : STEP 4 from Pattern 4         │
│                                          │
│ Key twist: after encoding, compare       │
│   lengths → return shorter one           │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

def encode_string(s):

    if not s:
        return ""

    result = []
    count = 1

    for i in range (1,len(s)):
        if s[i] == s[i-1]:
            count +=1

        else: 
            result.append(s[i -1] + str(count))
            count = 1

    result.append(s[-1] + str(count))
    encoded = "".join(result)
    return encoded if len(encoded) < len(s) else s


def parse_string(k):
    result = []
    i = 0


    while i < len(k):
        char = k[i]
        i += 1

        count = ""
        while i < len(k) and k[i].isdigit():
            count +=k[i]
            i +=1


        result.append(char * int(count))
    return "".join(result)

s = input("enter the data : ")

print("the encoded data",encode_string(s))
k = encode_string(s)
print("the parsed data : " , parse_string(k))