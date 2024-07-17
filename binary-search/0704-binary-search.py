class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)   #(low + high) // 2 was not used as the given one can be used for very large numbers which might hit the 32 byte mark

            if nums[mid] > target: 
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1