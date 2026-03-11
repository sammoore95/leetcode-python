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