class RomanToNumber:

    def __init__(self, roman_number):
        self.r_num = roman_number
        self.sum = 0
        self.roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToNumber(self):
        i = 0
        r_num = self.r_num
        sum = self.sum
        roman_values = self.roman_values
        # iterating through every value in roman_number
        while i in range(len(r_num)):
            # if 'i' is the last letter then it simply adds to sum
            if i == len(r_num)-1:
                sum += roman_values[r_num[i]]
            # checks if next char is higher than 'i', eg: ix = 10-1 = 9 and adds the value to sum
            elif roman_values[r_num[i]] < roman_values[r_num[i + 1]]:
                sum += roman_values[r_num[i + 1]] - roman_values[r_num[i]]
                i += 1  # since 2 chars are added here, we don't need next 'i' (next char) to be checked
            else:
                sum += roman_values[r_num[i]]

            i += 1

        return sum


selfr_num = input("Enter a roman number to convert into number: ").upper()
rnum = RomanToNumber(selfr_num)
print(rnum.romanToNumber())

# Input: s = "III"
# Output: 3

# Input: s = "LVIII"
# Output: 58

# Input: s = "MCMXCIV"
# Output: 1994
# M = 1000, CM = 900, XC = 90 and IV = 4.
