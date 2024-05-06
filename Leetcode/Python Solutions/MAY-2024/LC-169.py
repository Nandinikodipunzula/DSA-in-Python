from typing import List
class Solution:
    #Voore's Voting Algo
    def majorityElement2(self, nums: List[int]) -> int:
        leader = None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                leader = nums[i]
            count+=1 if leader == nums[i] else -1
        return leader
    #Time Complexity - O(n)

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return  nums[len(nums)//2]
    #Time Complexity - O(nlogn)

if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    majorityElement = solution.majorityElement(nums)
    print(majorityElement)

        