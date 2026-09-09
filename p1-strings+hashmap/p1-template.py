# ── STRING + HASHMAP TEMPLATE ──────────────────
# When to use: count/track characters in a string
# Time: O(n) | Space: O(k) where k = unique chars
# ───────────────────────────────────────────────

def string_hashmap_template(s):
    # STEP 1: Create an empty frequency map
    freq = {}

    # STEP 2: Scan the string, count each character
    for char in s:
        # If char exists, add 1. If not, start at 0 then add 1.
        freq[char] = freq.get(char, 0) + 1

    # STEP 3: Use the map to answer your question
    # (this part changes per problem)
    for char, count in freq.items():
        if count == 1:
            return char   # example: first unique char

    return -1  # default if nothing found

# ────────────────────────────────────────────────

# patterns to modify 
"""
┌───────────────────────────────────────────────────┐
│ Problem                   → How pattern fits       │
│ ─────────────────────────────────────────────────  │
│ Anagram check             → count both strings,   │
│                             compare maps           │
│                                                    │
│ First unique character    → count all chars,       │
│                             scan again for count=1 │
│                                                    │
│ Find common characters    → count string 1,        │
│                             check string 2 against │
│                             the map                │
│                                                    │
│ Group anagrams            → sorted word as key,    │
│                             group originals        │
└───────────────────────────────────────────────────┘ 
"""