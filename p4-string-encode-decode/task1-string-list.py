"""┌──────────────────────────────────────────┐
│ 📋 TASK #7                               │
│                                          │
│ Pattern    : String Encoding & Parsing   │
│ Difficulty : Medium                      │
│                                          │
│ Problem:                                 │
│ Design an algorithm to encode a list of  │
│ strings into ONE single string, and      │
│ decode that single string back into the  │
│ original list.                           │
│                                          │
│ Example:                                 │
│   Input  → ["hello", "world", "hi"]     │
│   Encoded → "5#hello5#world2#hi"        │
│   Decoded → ["hello", "world", "hi"]    │
│                                          │
│   Tricky case:                           │
│   Input  → ["a#b", "cd"]               │
│   Encoded → "3#a#b2#cd"                │
│   (# inside word doesn't confuse us     │
│    because we use LENGTH to navigate)   │
│                                          │
│ Trigger: "encode list → single string"  │
│          "decode back → original list"  │
│          → Encoding & Parsing pattern   │
│                                          │
│ Template : use STEP 4 above             │
│                                          │
│ Key insight: use LENGTH as your guide   │
│   encode → str(len(word)) + "#" + word  │
│   decode → read number, skip #,         │
│             slice exactly that many     │
│             characters forward          │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

def encode(strs): #encoding
    if not strs:
        return ""
    result = []
    for word in strs:
        result.append(str(len(word)) + "#" + word)
    return "".join(result)

# s= input("enter the string : ") # 5#hello5#world2#hi

def decode(s):
    result = []
    i =0

    while i < len(s):
        count = ""

        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1

        if i < len(s) and s[i] == "#":
            i+=1

        length = int(count)

        word = s[i:i+length]

        result.append(word)
        i += length

    return result


original = ["hello", "world", "hi"]
encoded = encode(original)
print(encoded)                         # 5#hello5#world2#hi
print(decode(encoded))
