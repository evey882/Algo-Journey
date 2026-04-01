"""
Valid Palindrome - LeetCode Easy
Day 2 of 10,950 | April 1st, 2026

Problem:
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Constraints:
- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

Examples:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

# ============================================
# APPROACH
# ============================================
# The ends need to be compared with each other as the checks are passed, we move inwards.
# if there is a char that doesn't have a match then false is returned otherwise, when they
# cross or meet return true
#
# Brute Force:
# - Since the order matters what we can do is a nested loop. It would check from left to right
# - and right to left, on each turn. Moved up to the left index,
# - Time: O(n^2)
# - Space: O(1)
#
# Optimized:
# - Two pointers, one starts from left to right, the other from right to left, if the pointers meet
# - or the pointers cross each other
# - Time: O(n)
# - Space: O(1)
#
# ============================================

def isPalindrome(s: str) -> bool:
    """
    This function utilizes pointers to verify if the string is a palindrome.
    A left and right pointer, starting from the word ends, moving inward.

    Cleans up the string first
    """
    cleaned_string = []
    for char in s:
        if char.isalpha():
            cleaned_string.append(char.lower())
    s = "".join(cleaned_string)

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    # Test 1: Example from Problem
    assert isPalindrome("A man, a plan, a canal: Panama") == True

    # Test 2: Example from Problem
    assert isPalindrome("race a car") == False

    # Test 3: Edge case - Example from Problem
    assert isPalindrome(" ") == True

    print("All tests passed! ✅")