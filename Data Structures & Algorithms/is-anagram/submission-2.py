class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countsS = dict()
        for letter in s:
            countsS[letter] = 1 + countsS.get(letter, 0)
        countsT = dict()
        for letter in t:
            countsT[letter] = 1 + countsT.get(letter, 0)
        return countsS == countsT