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