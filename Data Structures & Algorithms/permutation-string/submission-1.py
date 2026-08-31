import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        targetFreq = dict.fromkeys(string.ascii_lowercase, 0)
        for char in s1:
            targetFreq[char] += 1
        l, r = 0, len(s1) - 1
        windowFreq = dict.fromkeys(string.ascii_lowercase, 0)
        for i in range(l, r + 1):
            char = s2[i]
            windowFreq[char] += 1
        while True:
            if targetFreq == windowFreq:
                return True
            if r == len(s2) - 1:
                break
            r += 1
            newChar = s2[r]
            windowFreq[newChar] += 1
            oldChar = s2[l]
            windowFreq[oldChar] -= 1
            l += 1
        return False