from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices=[]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    indices.extend({i,j})
                    return indices

        indices.extend({-1,-1})
        return indices
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            diff = target - n 
            if diff in map:
                return [i,map[diff]]
            map[n] = i
        return [-1,-1]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([1,3,8,6,5,4,3],11))



    