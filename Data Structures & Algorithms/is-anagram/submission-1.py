class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tAsList = list(t)
        for s_letter in s:
            foundLetter = False
            for t_letter in tAsList:
                if t_letter == s_letter:
                    tAsList.remove(t_letter)
                    foundLetter = True
                    break
            if not foundLetter:
                return False
        return True
                
