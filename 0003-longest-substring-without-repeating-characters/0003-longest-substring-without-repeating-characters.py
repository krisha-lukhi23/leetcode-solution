class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}

        left = 0

        max_length = 0

        for right in range(len(s)):

            current_char = s[right]

            
            if current_char in seen and seen[current_char] >= left:
              
                left = seen[current_char] + 1

            seen[current_char] = right

            current_length = right - left + 1

            if current_length > max_length:
                max_length = current_length

        return max_length