class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        left_sum =0
        for i , num in enumerate(nums):
            if left_sum == nums_sum-left_sum-num:
                return i
            left_sum+=num
        return -1