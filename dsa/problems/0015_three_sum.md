# 0015. 3Sum

[← Back to DSA Index](../index.md)

> LeetCode 15 — Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
> Notice that the solution set must not contain duplicate triplets.

Related notes: [Array](../patterns/array.md), [Sorting](../patterns/sorting.md), [Two Pointers](../patterns/two_pointers.md), [Two Sum](./0001_two_sum.md)

---

## Intuition
The main constraints are
- We cannot reuse the same element, ex. i != j, j != k and i != k
- Even if we're not using the same element, we don't want repeated triplets
    - Ex. [1, 2, 3], [3, 2, 1] should not be in the array
    - If 2 is duplicated in the array, we don't want [1, 2, 3] twice.

Intuition
> For each element (which we can call the **anchor**), perform a 2 sum on the rest of the array

This is quite simple, and would be correct, but it would not satisfy the constraints

For example, for input [-1, 0, 1, 2, -1, -4], we can easily see how [-1, 0, 1] would be generated as 
well as [0, 1, -1]

To avoid the issue of duplication, we can sort the array first.

[-4, -1, -1, 0, 1, 2]

This guarantees that all duplicate elements are now grouped together, which means once we've already
processed x, we will not see x down the line. This is great because it allows us to skip duplicate
anchor elements quite easily by just using something like nums[i] != nums[i - 1]

But even if we skip duplicate anchor elements, we can still get [-1, 0, 1] and then [0, -1, 1],
which is just a permutation of [-1, 0, 1]. You can visualize this by using -1 as the anchor and
performing a 2 sum, then using 0 as the anchor and performing a 2 sum.

To avoid this issue, we want the **first** element we see to always be the anchor. This means for
each anchor element, we *search forward* for a 2 sum. 

[-4, -1, -1, **0**, 1, 2]

Now when we're processing 0, we will not
*look back* to process -1 anymore.

So the intuition becomes:
> Sort the list, skip duplicate anchor elements, and for each anchor element, search for all the 
2-sums **after** the anchor element that would sum with the anchor element to 0.

## Approach

From our intuition, we derive the following approach
- Sort the list
- Start iterating through the list, setting each element as the anchor element (skipping duplicates)
- For each anchor element, search **after** the anchor element for **all** 2 sums that would sum to 0
with the anchor element and all to our list of 3 sums

## Complexity

- Time: O(n^2)
- Space: O(1)

## Solution

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sums = []
        nums.sort()
        # For each num, look ahead to find all 2-sum's that would sum to 0 with num
        for i in range(len(nums)):
            # Skip duplicates
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # find all 2-sum's ahead of num using a 2-pointer approach (see *)
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                # Whenever we find a triplet, add to array immediately
                if cur_sum == 0:
                    three_sums.append([nums[i], nums[left], nums[right]])
                    # Continue the search
                    left += 1
                    right -= 1
                    # Avoid duplicate 2-sum pairs (see **)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1

        return three_sums

# *
# Since the array is sorted, we can start from both ends of the array, calculating the
# sum along the way and move inwards with the following rules:
# If sum > target, decrement right to decrease sum
# If sum < target, increment left to increase sum
# This is a greedy approach, and it works intuitively because at each step, we would
# have the choice of either decreasing our sum or increasing our sum.
# One concern is what if we "step over" our target? Ex. we decremented past the correct
# right index.
# That will not happen, because say that if we landed on the correct right index, then
# we must have sum < target because the array is sorted, so we increment left to
# increase sum until we reach the correct left index.

# **
# If nums[left] == nums[left - 1], then to make the triplet equal
# to 0, then we must have nums[right] == nums[right + 1], in which
# case it will be a duplicate 2-sum pair, so we can move on to the
# next pair (by incrementing left or decrementing right, doesn't
# matter), but if nums[right] != nums[right + 1], then the triplet will not be equal
# to 0 anyways. In either case, we can move on.

```

## Key Takeaways
- Sorting is a good way to remove duplicates from an ordering
