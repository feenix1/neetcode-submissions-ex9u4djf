class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxFound = (r - l) * min(heights[l], heights[r])
        while l < r:
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            amount = (r - l) * min(heights[l], heights[r])
            if amount > maxFound:
                maxFound = amount
        return maxFound