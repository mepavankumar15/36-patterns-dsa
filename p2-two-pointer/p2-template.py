# ── STRING TWO POINTERS TEMPLATE ───────────────
# When to use: compare/process from both ends
# Time: O(n) | Space: O(1) ← no extra memory!
# ───────────────────────────────────────────────

def two_pointers_template(s):
    # STEP 1: Set up both pointers at opposite ends
    L = 0
    R = len(s) - 1

    # STEP 2: Move toward each other until they meet
    while L < R:

        # STEP 3: Compare characters at both pointers
        if s[L] != s[R]:
            return False      # mismatch → stop early

        # STEP 4: Move both pointers inward
        L += 1
        R -= 1

    # STEP 5: Loop finished → everything matched
    return True

# ────────────────────────────────────────────────

# patterns to modify 
"""┌────────────────────────────────────────────────────┐
│ Problem                    → How pattern fits       │
│ ──────────────────────────────────────────────────  │
│ Palindrome check           → L & R move inward,    │
│                              compare characters     │
│                                                     │
│ Valid palindrome            → skip non-alphanumeric │
│ (spaces, punctuation)        chars, same template   │
│                                                     │
│ Reverse a string           → swap s[L] and s[R],   │
│                              move inward            │
│                                                     │
│ Remove one char,           → try skipping L or R,  │
│ still a palindrome?          run template twice     │
└────────────────────────────────────────────────────┘"""