class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        max_water = 0

        while left < right:
            width = right - left

            if height[left] < height[right]:
                current_height = height[left]
            else:
                current_height = height[right]

            current_area = width * current_height

            if current_area > max_water:
                max_water = current_area

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_water