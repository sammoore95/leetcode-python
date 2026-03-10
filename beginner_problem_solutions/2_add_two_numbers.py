"""
LeetCode #2 - Add Two Numbers

Difficulty: Medium
Topic: Linked List

Problem:
https://leetcode.com/problems/add-two-numbers/

Notes:
Practicing linked list traversal and carry handling.
"""

def addTwoNumbers(l1, l2):
    reversed_l1 = l1[::-1]
    reversed_l2 = l2[::-1]

    number1 = 0
    number2 = 0

    for i in reversed_l1:
        number1 = number1 * 10 + i

    for i in reversed_l2:
        number2 = number2 * 10 + i

    new_number = number1 + number2

    new_list = list(map(int, str(new_number)))

    reversed_new_list = new_list[::-1]

    return reversed_new_list


def test_addTwoNumbers():
    assert addTwoNumbers(l1=[2,4,3], l2=[5,6,4]) == [7,0,8]
    assert addTwoNumbers(l1 = [0], l2 = [0]) == [0]
    assert addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]) == [8,9,9,9,0,0,0,1]


if __name__ == "__main__":
    test_addTwoNumbers()
    print("All tests passed!")