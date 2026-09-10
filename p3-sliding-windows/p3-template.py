# ── STRING SLIDING WINDOW TEMPLATE ─────────────
# When to use: longest/shortest substring problem
# Time: O(n) | Space: O(k) where k = unique chars
# ───────────────────────────────────────────────

def sliding_window_template(s):
    # STEP 1: Set up window tracking map + pointers
    window = {}       # tracks chars inside window
    L = 0             # left edge of window
    result = 0        # store best answer so far

    # STEP 2: R expands the window every iteration
    for R in range(len(s)):

        # STEP 3: Add new character into window
        char = s[R]
        window[char] = window.get(char, 0) + 1

        # STEP 4: SHRINK from left if condition broken
        # (condition changes per problem)
        while window[char] > 1:        # duplicate found
            left_char = s[L]
            window[left_char] -= 1     # remove leftmost
            L += 1                     # shrink window

        # STEP 5: Update result with current window size
        result = max(result, R - L + 1)

    return result

# ────────────────────────────────────────────────
#remember this
""" for R in range(len(s)):
        while condition_broken:
"""


"""┌────────────────────────────────────────────────────┐
│ Problem                      → How pattern fits     │
│ ────────────────────────────────────────────────── │
│ Longest substring            → shrink when any      │
│ no repeating chars             char count > 1       │
│                                                     │
│ Longest substring with       → shrink when          │
│ at most K distinct chars       distinct keys > K    │
│                                                     │
│ Minimum window substring     → shrink when all      │
│                                target chars found   │
│                                                     │
│ Find all anagrams            → fixed size window,   │
│                                compare char counts  │
└────────────────────────────────────────────────────┘"""