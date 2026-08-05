class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindowSize = 0
        seenBefore = {}
        l = 0
        for r in range(0, len(s)):
            if s[r] in seenBefore:
                l = max(seenBefore[s[r]] + 1, l)
            windowSize = r - l + 1
            if maxWindowSize < windowSize:
                maxWindowSize = windowSize
            seenBefore[s[r]] = r
        return maxWindowSize
            