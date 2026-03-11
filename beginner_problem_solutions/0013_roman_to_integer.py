"""
LeetCode Problem 13: Roman to Integer

Description:
Given a string representing a Roman numeral, convert it to an integer.

Roman numerals use the following symbols:

```
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
```

Normally numerals are added together. However, if a smaller numeral appears
before a larger numeral, the smaller value should be subtracted.

Examples:
III     -> 3
IV      -> 4
IX      -> 9
LVIII   -> 58
MCMXCIV -> 1994

Parameters:
s (str): A string representing a valid Roman numeral.

Returns:
int: The integer value of the Roman numeral.

Approach:
1. Create a dictionary that maps Roman numerals to their integer values.
2. Iterate through the string.
3. Compare the value of the current symbol with the next symbol.
4. If the current value is less than the next value, subtract it.
5. Otherwise, add it to the total.
"""


def romanToInt(s):
    dict_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = 0

    for i in range(len(s)):

        # check if last character and if current value is smaller than the next value
        if i < len(s) - 1 and dict_numerals[s[i]] < dict_numerals[s[i+1]]:
            number -= dict_numerals[s[i]]
        else:
            number += dict_numerals[s[i]]

    return number


# tests = ["III", "LVIII", "MCMXCIV"]

# for i in tests:
#     result = romanToInt(i)
#     print(result)

def test_romanToInt():
    assert romanToInt(s="III") == 3
    assert romanToInt(s="LVIII") == 58
    assert romanToInt(s="MCMXCIV") == 1994

if __name__ == "__main__":
    test_romanToInt()
    print("All tests passed")