class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = []
        l = 0
        for r in range(0, len(nums)):
            new = nums[r]
            heapq.heappush_max(heap, [new, r])
            if r - l + 1 < k:
                continue
            maxVal, index = heap[0]
            while index < l:
                heapq.heappop_max(heap)
                maxVal, index = heap[0]
            output.append(maxVal)
            l += 1
        return output
