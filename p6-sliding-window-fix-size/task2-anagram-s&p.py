"""
┌──────────────────────────────────────────┐
│ 📋 TASK #13                              │
│                                          │
│ Pattern    : Sliding Window Fixed Size   │
│ Difficulty : Medium                      │
│                                          │
│ Problem:                                 │
│ Given two strings s and p, return all   │
│ starting indices of p's anagrams in s.  │
│                                          │
│ Example:                                 │
│   Input  → s="cbaebabacd", p="abc"     │
│   Output → [0, 6]                        │
│                                          │
│   Why?                                   │
│   Index 0: s[0:3] = "cba" → anagram ✅ │
│   Index 6: s[6:9] = "bac" → anagram ✅ │
│                                          │
│   Input  → s="abab", p="ab"            │
│   Output → [0, 1, 2]                    │
│                                          │
│ Trigger: "anagram" + "fixed window"     │
│          = len(p) → Fixed Sliding Window │
│          + HashMap to compare counts    │
│                                          │
│ Template : STEP 4 from Pattern 6        │
│            + HashMap from Pattern 1     │
│                                          │
│ Key twist: this combines TWO patterns!  │
│   → window size = len(p) always fixed   │
│   → use char count map to check if      │
│     current window is anagram of p      │
│                                          │
│ Strategy:                                │
│   1. Build freq map of p                │
│   2. Build freq map of first window     │
│   3. If maps match → anagram found      │
│   4. Slide → update window map          │
│      add new char, remove old char      │
│   5. Compare maps each slide            │
│                                          │
│ Try from memory first.                   │
│ When done → new chat → REVIEW MODE       │
└──────────────────────────────────────────┘"""

# ── Sliding Window Fixed + HashMap — Find Anagrams ──
# Time: O(n) | Space: O(k), k = unique chars ≤ 26

from collections import Counter

def find_anagrams(s, p):
    if len(s) < len(p):
        return []

    window_size = len(p)
    p_count = Counter(p)
    window_count = Counter(s[:window_size])
    result = []

    # Check first windows
    if window_count == p_count:
        result.append(0)

    # Slide window across rest of s
    for i in range(window_size, len(s)):
        # Add incoming right character
        window_count[s[i]] += 1

        # Drop outgoing left character
        old_char = s[i - window_size]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - window_size + 1)

    return result


# ── Driver code ─────────────────────────────────────
print(find_anagrams("cbaebabacd", "abc"))   # [0, 6]
print(find_anagrams("abab", "ab"))          # [0, 1, 2]
print(find_anagrams("aa", "bb"))            # []
print(find_anagrams("ab", "abc"))           # []