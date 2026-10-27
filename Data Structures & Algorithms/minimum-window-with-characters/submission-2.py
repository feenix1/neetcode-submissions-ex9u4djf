class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        windowCount = {}
        targetChars = {}
        for char in t:
            targetChars[char] = targetChars.get(char, 0) + 1
        shortest = ""
        setsFound = 0
        need = len(targetChars)
        l, r = 0, 0
        while r < len(s):
            end = s[r]
            windowCount[end] = 1 + windowCount.get(end, 0)

            if end in targetChars:
                if windowCount[end] == targetChars[end]:
                    setsFound += 1
            
            while setsFound == need:
                if shortest == "" or (r - l + 1) < len(shortest):
                    shortest = s[l:r+1]
                windowCount[s[l]] -= 1
                if s[l] in targetChars and windowCount[s[l]] < targetChars[s[l]]:
                    setsFound -= 1
                l += 1
            r += 1
        return shortest

    def worseMinWindow(self, s: str, t: str) -> str:
        targetFreq = dict()
        windowFreq = dict.fromkeys(string.ascii_letters, 0)
        shortest = None
        for char in t:
            if targetFreq.get(char) is None:
                targetFreq[char] = 1
            else:
                targetFreq[char] += 1
        l, r = 0, 0
        while r < len(s):
            windowFreq[s[r]] += 1
            r += 1
            if shortest is not None and (r - l) > len(shortest):
                windowFreq[s[l]] -= 1
                l += 1

            if r - l < len(t):
                continue

            substring = s[l:r]
            valid = True
            for targetChar, targetCount in targetFreq.items():
                count = 0
                for char in substring:
                    if char != targetChar:
                        continue
                    count += 1
                if count != targetCount:
                    valid = False
            
            if valid:
                while targetFreq.get(s[l]) is None:
                    windowFreq[s[l]] -= 1
                    l += 1 
                substring = s[l:r]
                if shortest is None or len(substring) < len(shortest):
                    shortest = substring
            
        if shortest is None:
            return ""
        else:
            return shortest