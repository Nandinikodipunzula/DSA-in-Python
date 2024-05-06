class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1 :
            return n
        writer=1
        for reader in range(1,n):
            if nums[reader-1]!=nums[reader]:
                nums[writer]=nums[reader]
                writer+=1
        return writer
        