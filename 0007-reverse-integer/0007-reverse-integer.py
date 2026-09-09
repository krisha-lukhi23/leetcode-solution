class Solution:
    def reverse(self, x):
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        reversed_num = 0

        while x != 0:
            digit = x % 10
            x = x // 10

            if reversed_num > (INT_MAX - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        reversed_num = reversed_num * sign

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num