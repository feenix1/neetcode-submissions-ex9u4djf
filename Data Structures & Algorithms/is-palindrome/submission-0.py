class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        for i in range(0, len(s) // 2):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return False
        return True
        