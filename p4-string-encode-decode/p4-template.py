# ── STRING ENCODING & PARSING TEMPLATE ─────────
# When to use: compress or parse formatted strings
# Time: O(n) | Space: O(n)
# ───────────────────────────────────────────────

# input aabcccdddd
# output a2b1c3d4 

"""
# Building strings → always use list + join (faster!)
result = []
result.append(something)
return "".join(result)

# Checking if char is digit
s[i].isdigit()   # True if '0'-'9'
"""

# ── ENCODE (Run Length Encoding) ────────────────
def encode(s):
    # STEP 1: Handle empty string edge case
    if not s:
        return ""

    result = []       # build result as list (faster than string concat)
    count = 1         # count current char streak

    # STEP 2: Walk through string starting from index 1
    for i in range(1, len(s)):

        # STEP 3: Same char as before → keep counting
        if s[i] == s[i - 1]:
            count += 1

        # STEP 4: Different char → flush current count+char
        else:
            result.append(str(count) + s[i - 1])
            count = 1   # reset count for new char

    # STEP 5: Don't forget the LAST group!
    result.append(str(count) + s[-1])

    return "".join(result)

# Decode
# input a2b1c3d4
# output aabcccdddd 

# ── DECODE (Run Length Decoding) ────────────────
def decode(s):
    result = []
    i = 0             # pointer walks through encoded string

    # STEP 1: Walk through encoded string
    while i < len(s):

        # STEP 2: Read the number (may be multi-digit!)
        count = ""
        while i < len(s) and s[i].isdigit():
            count += s[i]   # collect all digit characters
            i += 1

        # STEP 3: Next character is the letter to repeat
        char = s[i]
        i += 1 

        # STEP 4: Repeat char by count times
        result.append(char * int(count))

    return "".join(result)

# ────────────────────────────────────────────────

#pattern to recognise
"""┌────────────────────────────────────────────────────┐
│ Problem                    → How pattern fits       │
│ ──────────────────────────────────────────────────  │
│ Run length encoding        → count streaks,         │
│                              write count+char       │
│                                                     │
│ Encode/decode string list  → use length+delimiter   │
│ ["hi","world"]               "2#hi5#world"          │
│                              read length, skip #,   │
│                              slice that many chars  │
│                                                     │
│ Valid IP address           → split by '.', validate │
│                              each part (0-255)      │
│                                                     │
│ Deserialize a path         → split by '/', rebuild  │
│ "/a/b/../c"                  step by step           │
└────────────────────────────────────────────────────┘"""