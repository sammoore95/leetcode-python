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

    numerals = []

    for n in str(s):
        numerals.append(n)

    number = 0

    for i in numerals:
        for key, value in dict_numerals.items():
            if i == key:
                number += value
            else:
                number += 0

    return number

tests = ["III", "LVIII", "MCMXCIV"]

for i in tests:
    result = romanToInt(i)
    print(result)

