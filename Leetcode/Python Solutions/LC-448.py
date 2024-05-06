class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappearedNums = []
        for num in nums:
            index = abs(num)-1
            nums[index] = -1 * abs(nums[index])
        for i,n in enumerate(nums):
            if n > 0:
                disappearedNums.append(i+1)
        return disappearedNums
    