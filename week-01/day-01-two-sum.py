"""
Two Sum - LeetCode Easy
Day 1 of 10,950 | March 31, 2025

Problem:
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# ============================================
# APPROACH
# ============================================
# There needs to be a comparison between the numbers found in the array,
# as the sum of these will be used to get the target value.
#
# Brute Force:
# - Utilize two loops, outer loop to compare one num to the other nums (inner loop)
# - once the first solution is found return
# - Time: O(n^2)
# - Space: O(1)
#
# Optimized:
# - Utilize a map, to keep track of what number has been seen and the complement, this way
# - we keep a memory
# - Time: O(n)
# - Space: O(n)
#
# ============================================

def two_sum(nums, target):
    """
    Uses hash map to find two indices that sum to target.
    Stores each number and its index as we iterate.
    For each number, checks if its complement exists in the map.
    Returns indices as a list.
    """
    complement_log = {}

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in complement_log:
            return [complement_log[complement], idx]
        else:
            complement_log[num] = idx
    return -1


# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    # Test 1: Example from problem
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Test 2: Example from problem
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test 3: Example from problem
    assert two_sum([3, 3], 6) == [0, 1]

    print("All tests passed! ✅")