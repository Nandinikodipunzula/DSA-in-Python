class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans= []
        pivotCount = 0

        for num in nums:
            if num < pivot:
                ans.append(num)
            elif num == pivot:
                pivotCount+=1
        while pivotCount > 0:
            ans.append(pivot)
            pivotCount-=1
        for num in nums:
             if num > pivot:
                ans.append(num)
        return ans
