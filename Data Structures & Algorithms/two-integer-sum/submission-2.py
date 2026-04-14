class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                sum = nums[i] + nums[j]
                if sum == target:
                    return [min(i, j), max(i, j)]
        return []