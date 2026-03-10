"""
LeetCode: 1. Two Sum
Difficulty: Easy
Topics: Array, Hash Map
Link: https://leetcode.com/problems/two-sum/

Approach:
Use a hashmap to store numbers we've seen.
If target - num exists in hashmap we found the pair.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def addTwoNumbers(l1, l2 ):
    reversed_l1 = l1[::-1]
    reversed_l2 = l2[::-1]

    number1 = 0
    number2 = 0

    for i in reversed_l1:
        number1 = number1 * 10 + i

    return number1

print(addTwoNumbers(l1=[1, 2, 3], l2=[7, 8, 9]))