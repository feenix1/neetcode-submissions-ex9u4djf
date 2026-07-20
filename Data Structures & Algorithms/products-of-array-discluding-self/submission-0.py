class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefixProduct = 1
        for i in range(0, len(nums)):
            output.append(prefixProduct)
            prefixProduct *= nums[i]
        postfixProduct = 1
        for i in reversed(range(0, len(nums))):
            output[i] *= postfixProduct
            postfixProduct *= nums[i]
        return output