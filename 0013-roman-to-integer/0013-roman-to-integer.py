
class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0

        for i in range(len(s) - 1):
            current_value = values[s[i]]
            next_value = values[s[i + 1]]

            if current_value < next_value:
                num -= current_value
            else:
                num += current_value

        num += values[s[-1]]

        return num

