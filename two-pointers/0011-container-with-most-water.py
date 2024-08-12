class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res


# Given below is the Brute Force solution which throws Time Limit Exceeded error.

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0

#         for L in range(len(height)):
#             for R in range(L + 1, len(height)):
#                 area = (R - L) * min(height[L], height[R])
#                 res = max(res, area)
#         return res
