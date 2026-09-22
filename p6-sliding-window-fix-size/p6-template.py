# ── SLIDING WINDOW FIXED SIZE TEMPLATE ─────────
# When to use: max/min/sum of every window size k
# Time: O(n) | Space: O(1)
# ───────────────────────────────────────────────

def fixed_window_template(arr, k):
    # STEP 1: Handle edge case
    if len(arr) < k:
        return 0

    # STEP 2: Build the first window (index 0 to k-1)
    window_sum = sum(arr[:k])
    max_sum = window_sum          # best answer so far

    # STEP 3: Slide the window from index k to end
    for i in range(k, len(arr)):

        # STEP 4: Add new element on right
        #         Remove old element on left
        window_sum += arr[i]          # add incoming
        window_sum -= arr[i - k]      # remove outgoing

        # STEP 5: Update best answer
        max_sum = max(max_sum, window_sum)

    return max_sum

# ────────────────────────────────────────────────

"""
window_size += arr[i] - arr[i-k]
"""

# pattern to recognise 
"""
┌────────────────────────────────────────────────────┐
│ Problem                    → How pattern fits       │
│ ──────────────────────────────────────────────────  │
│ Max sum of size k          → track running sum      │
│                              update max each slide  │
│                                                     │
│ Average of size k          → same as above          │
│                              divide sum by k        │
│                                                     │
│ Find all anagrams          → fixed window = len(p)  │
│ of pattern p in string       compare char counts    │
│                              each slide             │
│                                                     │
│ Max of each window         → need deque for O(n)    │
│ (harder version)             → that's Pattern 16!   │
└────────────────────────────────────────────────────┘
"""