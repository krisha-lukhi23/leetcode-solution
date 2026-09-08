class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        rows = []
        for i in range(numRows):
            rows.append("")

        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] = rows[current_row] + char

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            if going_down:
                current_row = current_row + 1
            else:
                current_row = current_row - 1

        result = ""
        for row in rows:
            result = result + row

        return result