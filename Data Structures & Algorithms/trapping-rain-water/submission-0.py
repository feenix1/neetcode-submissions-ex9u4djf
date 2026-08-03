class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        lMax, rMax = 0, 0
        for l in range(0, len(height)):
            r = len(height) - 1 - l
            prefix.append(lMax)
            suffix.insert(0, rMax)
            if lMax < height[l]:
                lMax = height[l] 
            if rMax < height[r]:
                rMax = height[r]
        waterSum = 0
        for i in range(0, len(height)):
            waterSum += max(min(prefix[i], suffix[i]) - height[i], 0)
        return waterSum