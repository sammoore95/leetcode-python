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

class Solution:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in lookup:
                return [lookup[diff], i]

            lookup[num] = i