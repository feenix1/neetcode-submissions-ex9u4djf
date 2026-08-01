class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in numsSet:
                continue
            length = 1
            current = num
            while True:
                current += 1
                if current not in numsSet:
                    break
                length += 1
            if length > longest:
                longest = length
        return longest
            
                
                
            
