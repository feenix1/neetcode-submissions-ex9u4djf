class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindowSize = 0
        seenBefore = set()
        l = 0
        for r in range(0, len(s)):
            while s[r] in seenBefore:
                seenBefore.remove(s[l])
                l += 1
            windowSize = r - l + 1
            if maxWindowSize < windowSize:
                maxWindowSize = windowSize
            seenBefore.add(s[r])
        return maxWindowSize
            