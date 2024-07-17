class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for c in s:
            if c.isalnum():
                word += c.lower()

        return word == word[::-1]   # can be used to check reverse

        # L = 0
        # R = len(word) - 1

        # while L < R:
        #     if word[L] != word[R]:
        #         return False
        #     L += 1
        #     R -= 1
        # return True