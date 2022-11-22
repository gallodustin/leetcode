# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Constraints
# * n == height.length
# * 2 <= n <= 105
# * 0 <= height[i] <= 104

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # initialize
        max_area = -1
        start_index = 0
        end_index = len(height) - 1
        
        # iterate from the widest possible area inwards
        while start_index < end_index:
            width = end_index - start_index
            area = width * min(height[start_index], height[end_index])
            if area > max_area:
                max_area = area
            if height[start_index] < height[end_index]:
                start_index += 1
            else:
                end_index -= 1
        
        # return final answer
        return max_area