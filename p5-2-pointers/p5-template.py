# ── TWO POINTERS TEMPLATE ──────────────────────
# When to use: find pair in SORTED array
# Time: O(n) | Space: O(1)
# ───────────────────────────────────────────────

# common process
"""
if sum == target  → answer found ✅
if sum < target   → L++  (go bigger)
if sum > target   → R--  (go smaller)"""

def two_pointers_template(arr, target):
    # STEP 1: Set pointers at opposite ends
    L = 0
    R = len(arr) - 1

    # STEP 2: Move toward each other
    while L < R:

        # STEP 3: Calculate current sum
        current_sum = arr[L] + arr[R]

        # STEP 4: Three cases — equal, too small, too big
        if current_sum == target:
            return [L, R]        # found the pair!

        elif current_sum < target:
            L += 1               # need larger value → move L right

        else:
            R -= 1               # need smaller value → move R left

    # STEP 5: No pair found
    return []

# ────────────────────────────────────────────────

"""
┌────────────────────────────────────────────────────┐
│ Problem                    → How pattern fits       │
│ ──────────────────────────────────────────────────  │
│ Two Sum (sorted array)     → classic template       │
│                              L+R compare to target  │
│                                                     │
│ Three Sum = 0              → fix one number,        │
│                              two pointers on rest   │
│                              (loop + template)      │
│                                                     │
│ Container with most water  → track max area         │
│                              move pointer with      │
│                              smaller height inward  │
│                                                     │
│ Remove duplicates          → slow pointer tracks    │
│ from sorted array            unique position,       │
│                              fast pointer scans     │
└────────────────────────────────────────────────────┘
"""