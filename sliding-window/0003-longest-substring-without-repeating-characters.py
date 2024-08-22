class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            res = max(res, R - L + 1)
        return res