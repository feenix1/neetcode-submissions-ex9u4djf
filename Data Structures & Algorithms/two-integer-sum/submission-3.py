class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            complementIndex = indexMap.get(difference)
            if complementIndex is not None:
                output = [i, complementIndex]
                output.sort()
                return output
            else:
                indexMap[nums[i]] = i
        return [0]
