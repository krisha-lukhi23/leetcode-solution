class Solution:
    def myAtoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        number = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            number = number * 10 + digit
            i += 1

            if number > INT_MAX:
                break

        number = number * sign

        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX

        return number