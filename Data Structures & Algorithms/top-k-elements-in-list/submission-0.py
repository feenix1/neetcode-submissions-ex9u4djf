class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freqCount = freq.get(num)
            if freqCount is None:
                freq[num] = 1
            else:
                freq[num] += 1
        maxFreq = []
        for num, count in freq.items():
            heapq.heappush(maxFreq, (-count, num))
        
        output = []
        for i in range(0, k):
            output.append(heapq.heappop(maxFreq)[1])
        
        return output

            