# This solution was inspired by neetcode's video solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Sort elements by frequency and get the top k elements
        most_common = freq.most_common(k)
        
        # Step 3: Extract just the elements
        result = [item[0] for item in most_common]

        return result




# This is the solution I came up with, but it does not work with all testcases (especially negative numbers)

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}

#         for n in nums:
#             freq[n] = freq.get(n, 0) + 1

#         sorted_dict = {key: freq[key] for key in sorted(freq, reverse = True)}

#         result = []

#         for value in sorted_dict.values():
#             result.append(value)

#         return result[:k]