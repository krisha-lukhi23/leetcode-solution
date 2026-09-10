class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(False)
            dp.append(row)

        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    prev_char = p[j - 2]
                    if prev_char == '.' or prev_char == s[i - 1]:
                        if dp[i - 1][j]:
                            dp[i][j] = True
                else:
                    dp[i][j] = False

        return dp[m][n]