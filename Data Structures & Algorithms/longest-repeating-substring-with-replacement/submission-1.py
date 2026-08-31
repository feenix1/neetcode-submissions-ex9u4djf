class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        frequency = {}
        for r in range(0, len(s)):
            char = s[r]
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
            maxFreq = 0
            freqSum = 0
            for value in frequency.values():
                if value > maxFreq:
                    maxFreq = value
                freqSum += value
            replacements = freqSum - maxFreq
            while replacements > k:
                leftChar = s[l]
                frequency[leftChar] -= 1
                maxFreq = 0
                freqSum = 0
                for v in frequency.values():
                    if v > maxFreq:
                        maxFreq = v
                    freqSum += v
                replacements = freqSum - maxFreq
                l += 1
            length = r - l + 1
            if length > longest:
                longest = length
        return longest