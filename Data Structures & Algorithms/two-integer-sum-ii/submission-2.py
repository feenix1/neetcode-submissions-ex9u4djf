class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            difference = target - numbers[j]
            if numbers[i] < difference:
                i += 1 
                continue
            if numbers[i] == difference:
                return [i + 1, j + 1]
            j -= 1
        return []